import json
import math

from django.db.models import F, Subquery
from django.forms import model_to_dict
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from notice.models import Notice, NoticeFile
from notice.serializers import NoticeSerializer


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
        posts = list(Notice.objects.order_by('-id').all())[offset:limit + 1]
        # posts = list(Notice.objects.order_by('-id').all())[offset:limit + 1]
        hasNext = False

        if len(posts) > size:
            hasNext = True
            posts.pop(size)


        context = {
            'posts': NoticeSerializer(posts, many=True).data,
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
            'member': post.member
        }

        return render(request, 'notice/detail.html', context)


