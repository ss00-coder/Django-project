from django.shortcuts import render
from django.views import View


# Create your views here.
class MyProfileView(View):
    def get(self, request):
        return render(request, 'mypage/myprofile.html')


class MyLessonView(View):
    def get(self, request):
        return render(request, 'mypage/mylesson.html')


class MyLessonReviewView(View):
    def get(self, request):
        return render(request, 'mypage/mylesson-review.html')


class MyHelpersView(View):
    def get(self, request):
        return render(request, 'mypage/myhelpers.html')


class MyEventView(View):
    def get(self, request):
        return render(request, 'mypage/myevent.html')


class MyMessageListView(View):
    def get(self, request):
        return render(request, 'message/list.html')


class MyMessageDetailView(View):
    def get(self, request):
        return render(request, 'message/detail.html')


class MyMessageWriteView(View):
    def get(self, request):
        return render(request, 'message/write.html')


class MyPayView(View):
    def get(self, request):
        return render(request, 'mypage/mypay.html')
