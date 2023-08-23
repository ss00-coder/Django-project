import json
import math

from django.db.models import F, Subquery
from django.forms import model_to_dict
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member, MemberFile
from notice.models import Notice, NoticeFile, NoticeReply, NoticeLike
from notice.serializers import NoticeSerializer, NoticeReplySerializer


class NoticeListView(View):
    def get(self, request):
        return render(request, 'notice/list.html')

# Create your views here.
class NoticeListAPI(APIView):
    def get(self, request, page):
        size = 5
        offset = (page - 1) * size
        limit = page * size
        # post = Notice.objects.filter(id=post_id).annotate(member_nickname=F('member__member_nickname'),
        #                                                   post_file=Subquery(post_file.values('image')[:1])).values(
        #     'id', 'post_title', 'post_content', 'post_view_count', 'post_status', 'member_nickname', 'post_file')
        all_posts = list(Notice.objects.order_by('-id').all())
        posts = []
        for i in range(len(all_posts)):
            id = all_posts[i].id
            notice_file = NoticeFile.objects.filter(notice_id=id)
            post = Notice.objects.filter(id=id).annotate(post_file=notice_file.values('image')[:1]).values('id', 'post_title', 'post_content', 'post_file')
            posts.append(post)

        posts = posts[offset:limit + 1]
        # posts = list(Notice.objects.order_by('-id').all())[offset:limit + 1]
        hasNext = False

        if len(posts) > size:
            hasNext = True
            posts.pop(size)


        context = {
            # 'posts': NoticeSerializer(posts, many=True).data,
            'posts': posts,
            'hasNext': hasNext
        }

        # return Response(posts)
        return Response(context)


class NoticeDetailView(View):
    def get(self, request, post_id):
        post = Notice.objects.get(id=post_id)
        post.post_view_count = post.post_view_count + 1
        post.save()

        context = {
            'post': post,
            'post_files': list(post.noticefile_set.all()),
            'writer': post.member,

        }
        if post.member.memberfile_set.filter(file_type='P'):
            context['writer_profile'] = post.member.memberfile_set.get(file_type='P')

        if 'member_email' in request.session:
            member = Member.objects.get(member_email=request.session['member_email'])
            context['member'] = member
            if member.memberfile_set.filter(file_type='P'):
                context['member_profile'] = member.memberfile_set.get(file_type='P')

        return render(request, 'notice/detail.html', context)



# 댓글
class NoticeReplyListAPI(APIView):
    def get(self, request, post_id, page=1):
        size = 5
        offset = (page - 1) * size
        limit = page * size

        all_replies = list(NoticeReply.objects.filter(notice_id=post_id).order_by("-id").all())
        total = len(all_replies)

        replies = []
        for i in range(len(all_replies)):
            id = all_replies[i].member.id
            reply_id = all_replies[i].id
            reply_writer_file = MemberFile.objects.filter(member_id=id, file_type="P")
            reply = NoticeReply.objects.filter(id=reply_id).order_by("-id").annotate(member_nickname=F('member__member_nickname'), reply_writer_file=reply_writer_file.values('image')[:1]).values('id', 'reply_content', 'member_nickname', 'created_date', 'reply_writer_file')
            replies.append(reply)
        #
        # posts = posts[offset:limit + 1]



        # replies = list(NoticeReply.objects.filter(notice_id=post_id).order_by("-id").annotate(member_nickname=F('member__member_nickname')).values('id', 'reply_content', 'member_nickname', 'created_date'))
        # total = len(replies)

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


class NoticeReplyWriteAPI(APIView):
    def post(self, request):
        datas = request.data
        datas = {
            'notice': Notice.objects.get(id=datas.get('post_id')),
            'member': Member.objects.get(member_email=request.session['member_email']),
            'reply_content': datas.get('reply_content')
        }
        NoticeReply.objects.create(**datas)
        return Response('success')


class NoticeReplyModifyAPI(APIView):
    def post(self, request):
        datas = request.data

        NoticeReply.objects.filter(id=datas['id']).update(reply_content=datas['reply_content'])
        return Response('success')


class NoticeReplyDeleteAPI(APIView):
    def get(self, request, id):
        print(id)
        NoticeReply.objects.filter(id=id).delete()
        return Response('success')


class NoticeLikeAddAPI(APIView):
    def post(self, request):
        datas = request.data
        datas = {
            'notice': Notice.objects.get(id=datas['id']),
            'member': Member.objects.get(member_email=request.session['member_email']),
        }
        NoticeLike.objects.create(**datas)
        return Response('success')


class NoticeLikeDeleteAPI(APIView):
    def post(self, request):
        datas = request.data
        member = Member.objects.get(member_email=request.session['member_email'])
        NoticeLike.objects.filter(notice_id=datas['id'], member=member).delete()
        return Response('success')


class NoticeLikeCountAPI(APIView):
    def get(self, request, id):
        return Response(NoticeLike.objects.filter(notice_id=id).count())


class NoticeLikeExistAPI(APIView):
    def get(self, request, id):
        # datas = request.data
        member = Member.objects.get(member_email=request.session['member_email'])
        check = NoticeLike.objects.filter(notice_id=id, member=member).exists()
        return Response(check)