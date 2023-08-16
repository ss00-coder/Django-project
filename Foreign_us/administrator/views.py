from django.shortcuts import render
from django.views import View


# Create your views here.
class BoardEventListView(View):
    def get(self, request):
        return render(request, 'admin/board/event/list.html')


class BoardEventDetailView(View):
    def get(self, request):
        return render(request, 'admin/board/event/detail.html')


class BoardHelpersListView(View):
    def get(self, request):
        return render(request, 'admin/board/helpers/list.html')


class BoardHelpersDetailView(View):
    def get(self, request):
        return render(request, 'admin/board/helpers/detail.html')


class BoardLessonListView(View):
    def get(self, request):
        return render(request, 'admin/board/lesson/list.html')


class BoardLessonDetailView(View):
    def get(self, request):
        return render(request, 'admin/board/lesson/detail.html')


class BoardNoticeListView(View):
    def get(self, request):
        return render(request, 'admin/board/notice/list.html')


class BoardNoticeDetailView(View):
    def get(self, request):
        return render(request, 'admin/board/notice/detail.html')


class BoardNoticeWriteView(View):
    def get(self, request):
        return render(request, 'admin/board/notice/write.html')


class BoardNoticeModifyView(View):
    def get(self, request):
        return render(request, 'admin/board/notice/modify.html')


class BoardInquiryListView(View):
    def get(self, request):
        return render(request, 'admin/board/inquiry/list.html')


class BoardInquiryDetailView(View):
    def get(self, request):
        return render(request, 'admin/board/inquiry/detail.html')


class BoardInquiryWriteView(View):
    def get(self, request):
        return render(request, 'admin/board/inquiry/answer.html')


class MemberListView(View):
    def get(self, request):
        return render(request, 'admin/member/list.html')


class MemberDetailView(View):
    def get(self, request):
        return render(request, 'admin/member/detail.html')


class MemberModifyView(View):
    def get(self, request):
        return render(request, 'admin/member/modify.html')

