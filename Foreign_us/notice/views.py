import json
import math

from django.forms import model_to_dict
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from notice.models import Notice
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

        posts = list(Notice.objects.order_by('-id').all())[offset:limit + 1]
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
    def get(self, request):
        return render(request, 'notice/detail.html')


