from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from notice.models import Notice


class NoticeListView(View):
    def get(self, request):
        return render(request, 'notice/list.html')

# Create your views here.
class NoticeListAPI(APIView):
    def get(self, request):
        posts = Notice.objects.all()
        return Response(posts)


class NoticeDetailView(View):
    def get(self, request):
        return render(request, 'notice/detail.html')


