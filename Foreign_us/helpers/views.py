from django.db.models import F
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from helpers.models import Helpers, HelpersFile, HelpersReply, HelpersLike
from member.models import MemberFile, Member


# Create your views here.
class HelpersListView(View):
    def get(self, request):
        return render(request, 'helpers/list.html')


class HelpersListAPI(APIView):
    def get(self, request, page, type):
        size = 7
        offset = (page - 1) * size
        limit = page * size
        posts = []

        all_posts = list(Helpers.objects.order_by('-id').all())

        if type == 'popular_post':
            all_posts = list(Helpers.objects.order_by('-post_view_count').all())

        for i in range(len(all_posts)):
            id = all_posts[i].id
            member_id = all_posts[i].member_id
            member_files = MemberFile.objects.filter(member_id=member_id, file_type="P")
            helpers_file = HelpersFile.objects.filter(helpers_id=id)
            post = Helpers.objects.filter(id=id).annotate(post_file=helpers_file.values('image')[:1], member_file=member_files.values('image')[:1]).values('id', 'post_title', 'post_content', 'post_file', 'member__member_nickname', 'post_view_count', 'created_date', 'member_file')
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


class HelpersDetailView(View):
    def get(self, request, post_id):
        post = Helpers.objects.get(id=post_id)
        post.post_view_count = post.post_view_count + 1
        post.save()

        all_posts = Helpers.objects.filter(member_id=post.member.id).order_by("-id").all()[:5]
        posts = []
        for i in range(len(all_posts)):
            id = all_posts[i].id
            writer_helpers_file = HelpersFile.objects.filter(helpers_id=id)
            writer_post = Helpers.objects.filter(id=id).annotate(post_file=writer_helpers_file.values('image')[:1]).values(
                'id', 'post_title', 'post_content', 'post_file', 'member__member_nickname', 'post_view_count',
                'created_date')
            posts.append(writer_post)
            # print(post)

        context = {
            'post': post,
            'post_files': list(post.helpersfile_set.all()),
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

        return render(request, 'helpers/detail.html', context)


class HelpersWriteView(View):
    def get(self, request, post_id=None):
        # 멤버 정보
        member = Member.objects.get(member_email=request.session['member_email'])

        # 멤버 프로필 이미지 없으면 기본 이미지로
        member_profile_img = "member/profile_icon.png"

        # 멤버의 프로필 이미지가 있으면 해당 이미지로
        if member.memberfile_set.filter(file_type='P'):
            member_profile_img = member.memberfile_set.get(file_type="P").image

        if Helpers.objects.filter(id=post_id):
            post = Helpers.objects.get(id=post_id)
            post_img = post.helpersfile_set.first()

            # 수정할 게시글 아이디가 맞다면 해당 게시글 수정
            context = {
                'member_file': member_profile_img,
                'post_title': post.post_title,
                'post_content': post.post_content,
                'post_status': post.post_status,
                'member': member,
                'member_profile_img': member_profile_img,
                'post_id': post_id,
                'post_img': post_img
            }

            return render(request, 'helpers/write.html', context)  # 데이터가 있으면 수정 페이지 렌더링

        else:
            # 데이터가 없으면 새로운 게시글 작성 페이지 렌더링
            context = {
                'member_file': member_profile_img,
                'post_title': "",
                'post_content': "",
                'post_status': "",
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


        # helpers(게시글) 생성 및 업데이트 할때 넣을 데이터
        helpers_datas = {
            'post_title': datas['post_title'],
            'post_content': datas['post_content'],
            'post_status': datas['post_status'],
            'member': member,
        }
        print(helpers_datas)

        # 수정할 게시글 아이디가 맞다면 해당 게시글 수정
        if Helpers.objects.filter(id=post_id):
            Helpers.objects.filter(id=post_id).update(**helpers_datas)
            helpers_post = Helpers.objects.get(id=post_id)

            # 파일 업로드 시 전에 있던 파일 삭제 후 새로 받은 파일로 생성
            if files:
                HelpersFile.objects.filter(helpers=helpers_post).delete()
                for file in files.getlist('post_file'):
                    HelpersFile.objects.create(image=file, helpers=helpers_post)

        # 수정할 게시글이 없다면 새로운 게시글 생성
        else:
            helpers_post = Helpers.objects.create(**helpers_datas)
            if files:
                for file in files.getlist('post_file'):
                    HelpersFile.objects.create(image=file, helpers=helpers_post)

        return redirect('helpers:list-init')


class HelpersReplyListAPI(APIView):
    def get(self, request, post_id, page=1):
        size = 5
        offset = (page - 1) * size
        limit = page * size

        all_replies = list(HelpersReply.objects.filter(helpers_id=post_id).order_by("-id").all())
        total = len(all_replies)

        replies = []
        for i in range(len(all_replies)):
            id = all_replies[i].member.id
            reply_id = all_replies[i].id
            reply_writer_file = MemberFile.objects.filter(member_id=id, file_type="P")
            reply = HelpersReply.objects.filter(id=reply_id).order_by("-id").annotate(member_nickname=F('member__member_nickname'), reply_writer_file=reply_writer_file.values('image')[:1]).values('id', 'reply_content', 'member_id', 'member_nickname', 'created_date', 'reply_writer_file')
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


class HelpersReplyWriteAPI(APIView):
    def post(self, request):
        datas = request.data
        datas = {
            'helpers': Helpers.objects.get(id=datas.get('post_id')),
            'member': Member.objects.get(member_email=request.session['member_email']),
            'reply_content': datas.get('reply_content')
        }
        HelpersReply.objects.create(**datas)
        return Response('success')


class HelpersReplyModifyAPI(APIView):
    def post(self, request):
        datas = request.data

        HelpersReply.objects.filter(id=datas['id']).update(reply_content=datas['reply_content'])
        return Response('success')


class HelpersReplyDeleteAPI(APIView):
    def get(self, request, id):
        print(id)
        HelpersReply.objects.filter(id=id).delete()
        return Response('success')


class HelpersLikeAddAPI(APIView):
    def post(self, request):
        datas = request.data
        datas = {
            'helpers': Helpers.objects.get(id=datas['id']),
            'member': Member.objects.get(member_email=request.session['member_email']),
        }
        HelpersLike.objects.create(**datas)
        return Response('success')


class HelpersLikeDeleteAPI(APIView):
    def post(self, request):
        datas = request.data
        member = Member.objects.get(member_email=request.session['member_email'])
        HelpersLike.objects.filter(helpers_id=datas['id'], member=member).delete()
        return Response('success')


class HelpersLikeCountAPI(APIView):
    def get(self, request, id):
        return Response(HelpersLike.objects.filter(helpers_id=id).count())


class HelpersLikeExistAPI(APIView):
    def get(self, request, id):
        # datas = request.data
        member = Member.objects.get(member_email=request.session['member_email'])
        check = HelpersLike.objects.filter(helpers_id=id, member=member).exists()
        return Response(check)