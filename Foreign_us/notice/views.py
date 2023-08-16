from django.shortcuts import render
from django.views import View


# Create your views here.
class NoticeListView(View):
    def get(self, request):
        return render(request, 'notice/list.html')


class NoticeDetailView(View):
    def get(self, request):
        return render(request, 'notice/detail.html')


