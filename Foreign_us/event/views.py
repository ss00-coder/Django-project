from django.db.models import F
from django.shortcuts import render, redirect
from django.views import View
from geopy import Nominatim
from rest_framework.response import Response
from rest_framework.views import APIView

from event.models import Event, EventFile, EventLike, EventReply
from member.models import Member, MemberFile


# Create your views here.

class EventListView(View):
    def get(self, request):
        return render(request, 'event/list.html')


class EventListAPI(APIView):
    def get(self, request, page, type):
        size = 7
        offset = (page - 1) * size
        limit = page * size
        posts = []

        all_posts = list(Event.objects.order_by('-id').all())

        if type == 'popular_post':
            all_posts = list(Event.objects.order_by('-post_view_count').all())

        for i in range(len(all_posts)):
            id = all_posts[i].id
            member_id = all_posts[i].member_id
            member_files = MemberFile.objects.filter(member_id=member_id, file_type="P")
            # member_files = Member.objects.get(id=Event.objects.get(id=id).member_id).memberfile_set.filter(file_type="P").values('image')
            event_file = EventFile.objects.filter(event_id=id)
            post = Event.objects.filter(id=id).annotate(post_file=event_file.values('image')[:1], member_file=member_files.values('image')[:1]).values('id', 'post_title', 'post_content', 'post_file', 'member__member_nickname', 'post_view_count', 'created_date', 'member_file')
            posts.append(post)

        posts = posts[offset:limit]  # Remove +1 from the limit

        hasNext = False

        if len(posts) > size:
            hasNext = True
            posts.pop(size)

        context = {
            # 'posts': NoticeSerializer(posts, many=True).data,
            'posts': posts,
            'hasNext': hasNext
        }

        return Response(context)


class EventDetailView(View):
    def get(self, request, post_id):
        post = Event.objects.get(id=post_id)
        post.post_view_count = post.post_view_count + 1
        post.save()

        all_posts = Event.objects.filter(member_id=post.member.id).order_by("-id").all()[:5]
        posts = []
        for i in range(len(all_posts)):
            id = all_posts[i].id
            writer_event_file = EventFile.objects.filter(event_id=id)
            writer_post = Event.objects.filter(id=id).annotate(post_file=writer_event_file.values('image')[:1]).values('id', 'post_title', 'post_content', 'post_file', 'member__member_nickname', 'post_view_count', 'created_date')
            posts.append(writer_post)
            # print(post)

        context = {
            'post': post,
            'post_files': list(post.eventfile_set.all()),
            'writer': post.member,
            'post_list': posts
        }

        if post.member.memberfile_set.filter(file_type='P'):
            context['writer_profile'] = post.member.memberfile_set.get(file_type='P')

        if 'member_email' in request.session:
            member = Member.objects.get(member_email=request.session['member_email'])
            context['member'] = member
            if member.memberfile_set.filter(file_type='P'):
                context['member_profile'] = member.memberfile_set.get(file_type='P')

        return render(request, 'event/detail.html', context)


class EventWriteView(View):
    def get(self, request, post_id=None):
        # 멤버 정보
        member = Member.objects.get(member_email=request.session['member_email'])

        # 멤버 프로필 이미지 없으면 기본 이미지로
        member_profile_img = "member/profile_icon.png"

        # 멤버의 프로필 이미지가 있으면 해당 이미지로
        if member.memberfile_set.filter(file_type='P'):
            member_profile_img = member.memberfile_set.get(file_type="P").image

        if Event.objects.filter(id=post_id):
            post = Event.objects.get(id=post_id)
            post_img = post.eventfile_set.first()

            # 수정할 게시글 아이디가 맞다면 해당 게시글 수정
            context = {
                'member_file': member_profile_img,
                'post_title': post.post_title,
                'post_content': post.post_content,
                'post_status': post.post_status,
                'event_location': post.event_location,
                'member': member,
                'member_profile_img': member_profile_img,
                'post_id': post_id,
                'post_img': post_img
            }

            return render(request, 'event/write.html', context)  # 데이터가 있으면 수정 페이지 렌더링

        else:
            # 데이터가 없으면 새로운 게시글 작성 페이지 렌더링
            context = {
                'member_file': member_profile_img,
                'post_title': "",
                'post_content': "",
                'post_status': "",
                'event_location': "",
                'member': "",
                'post_id': 0,
                'post_img': ""
            }

            return render(request, 'event/write.html', context)

    def post(self, request, post_id):
        # 멤버 정보
        member = Member.objects.get(member_email=request.session['member_email'])

        # 작성 및 수정페이지에서 받아온 데이터 및 파일,태그
        datas = request.POST
        files = request.FILES

        # 주소 데이터 -> 위도, 경도로 변경
        geolocator = Nominatim(user_agent='heesu')
        location = geolocator.geocode(datas['event_location'])

        # event(게시글) 생성 및 업데이트 할때 넣을 데이터
        event_datas = {
            'post_title': datas['post_title'],
            'post_content': datas['post_content'],
            'post_status': datas['post_status'],
            'event_location': datas['event_location'],
            'member': member,
        }
        print(event_datas)
        # 데이터에 주소가 있으면 위도와 경도를 데이터로
        if location:
            event_datas['event_latitude'] = location.latitude
            event_datas['event_longitude'] = location.longitude

        # 수정할 게시글 아이디가 맞다면 해당 게시글 수정
        if Event.objects.filter(id=post_id):
            Event.objects.filter(id=post_id).update(**event_datas)
            event_post = Event.objects.get(id=post_id)

            # 파일 업로드 시 전에 있던 파일 삭제 후 새로 받은 파일로 생성
            if files:
                EventFile.objects.filter(event=event_post).delete()
                for file in files.getlist('post_file'):
                    EventFile.objects.create(image=file, event=event_post)

        # 수정할 게시글이 없다면 새로운 게시글 생성
        else:
            event_post = Event.objects.create(**event_datas)
            if files:
                for file in files.getlist('post_file'):
                    EventFile.objects.create(image=file, event=event_post)

        return redirect('event:list-init')


# 댓글
class EventReplyListAPI(APIView):
    def get(self, request, post_id, page=1):
        size = 5
        offset = (page - 1) * size
        limit = page * size

        all_replies = list(EventReply.objects.filter(event_id=post_id).order_by("-id").all())
        total = len(all_replies)

        replies = []
        for i in range(len(all_replies)):
            id = all_replies[i].member.id
            reply_id = all_replies[i].id
            reply_writer_file = MemberFile.objects.filter(member_id=id, file_type="P")
            reply = EventReply.objects.filter(id=reply_id).order_by("-id").annotate(member_nickname=F('member__member_nickname'), reply_writer_file=reply_writer_file.values('image')[:1]).values('id', 'reply_content', 'member_id', 'member_nickname', 'created_date', 'reply_writer_file')
            replies.append(reply)

        replies = replies[offset:limit + 1]
        hasNext = False

        if len(replies) > size:
            hasNext = True
            replies.pop(size)

        context = {
            # 'posts': NoticeSerializer(posts, many=True).data,
            'replies': replies,
            'hasNext': hasNext,
            'total': total
        }
        return Response(context)
        # return Response(NoticeReplySerializer(replies, many=True).data)


class EventReplyWriteAPI(APIView):
    def post(self, request):
        datas = request.data
        datas = {
            'event': Event.objects.get(id=datas.get('post_id')),
            'member': Member.objects.get(member_email=request.session['member_email']),
            'reply_content': datas.get('reply_content')
        }
        EventReply.objects.create(**datas)
        return Response('success')


class EventReplyModifyAPI(APIView):
    def post(self, request):
        datas = request.data

        EventReply.objects.filter(id=datas['id']).update(reply_content=datas['reply_content'])
        return Response('success')


class EventReplyDeleteAPI(APIView):
    def get(self, request, id):
        print(id)
        EventReply.objects.filter(id=id).delete()
        return Response('success')


class EventLikeAddAPI(APIView):
    def post(self, request):
        datas = request.data
        datas = {
            'event': Event.objects.get(id=datas['id']),
            'member': Member.objects.get(member_email=request.session['member_email']),
        }
        EventLike.objects.create(**datas)
        return Response('success')


class EventLikeDeleteAPI(APIView):
    def post(self, request):
        datas = request.data
        member = Member.objects.get(member_email=request.session['member_email'])
        EventLike.objects.filter(event_id=datas['id'], member=member).delete()
        return Response('success')


class EventLikeCountAPI(APIView):
    def get(self, request, id):
        return Response(EventLike.objects.filter(event_id=id).count())


class EventLikeExistAPI(APIView):
    def get(self, request, id):
        # datas = request.data
        member = Member.objects.get(member_email=request.session['member_email'])
        check = EventLike.objects.filter(event_id=id, member=member).exists()
        return Response(check)