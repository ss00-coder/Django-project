import math
import os

from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View

from member.models import Member
from notice.models import Notice, NoticeFile


# Create your views here.
# 이벤트 목록
class BoardEventListView(View):
    def get(self, request):
        return render(request, 'admin/board/event/list.html')


# 이벤트 조회
class BoardEventDetailView(View):
    def get(self, request):
        return render(request, 'admin/board/event/detail.html')


# 헬퍼스 목록
class BoardHelpersListView(View):
    def get(self, request):
        return render(request, 'admin/board/helpers/list.html')


# 헬퍼스 조회
class BoardHelpersDetailView(View):
    def get(self, request):
        return render(request, 'admin/board/helpers/detail.html')


# 과외 목록
class BoardLessonListView(View):
    def get(self, request):
        return render(request, 'admin/board/lesson/list.html')


# 과외 조회
class BoardLessonDetailView(View):
    def get(self, request):
        return render(request, 'admin/board/lesson/detail.html')


# 공지사항 목록
class BoardNoticeListView(View):
    def get(self, request, page=1):
        size = 7
        offset = (page - 1) * size
        limit = page * size
        total = Notice.objects.all().count()
        pageCount = 5
        endPage = math.ceil(page / pageCount) * pageCount
        startPage = endPage - pageCount + 1
        realEnd = math.ceil(total / size)
        endPage = realEnd if endPage > realEnd else endPage
        if endPage == 0:
            endPage = 1

        context = {
            'posts': list(Notice.objects.order_by('-id').all())[offset:limit],
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
        }
        return render(request, 'admin/board/notice/list.html', context)


# 공지사항 조회
class BoardNoticeDetailView(View):
    def get(self, request, post_id, page):
        post = Notice.objects.get(id=post_id)
        context = {
            'post': post,
            'post_files': list(post.noticefile_set.all()),
            'page': page
        }
        return render(request, 'admin/board/notice/detail.html', context)


# 공지사항 쓰기
class BoardNoticeWriteView(View):
    def get(self, request, page):
        return render(request, 'admin/board/notice/write.html', {'page': page})

    def post(self, request, page):
        datas = request.POST
        files = request.FILES

        datas = {
            'member_id': Member.objects.filter(member_type='A').get().id,
            'post_title': datas['post_title'],
            'post_content': datas['post_content']
        }

        post = Notice.objects.create(**datas)

        for file in files.getlist('file'):
            NoticeFile.objects.create(notice=post, image=file)

        return redirect(post.get_absolute_url(page))


# 공지사항 수정
class BoardNoticeModifyView(View):
    def get(self, request, post_id, page):
        post = Notice.objects.get(id=post_id)
        context = {
            'post': post,
            'post_files': list(post.noticefile_set.all()),
            'page': page
        }
        return render(request, 'admin/board/notice/modify.html', context)


    def post(self, request, post_id, page):
        datas = request.POST
        files = request.FILES

        post_data = {
            'post_title': datas['post_title'],
            'post_content': datas['post_content']
        }

        Notice.objects.filter(id=post_id).update(**post_data)
        post = Notice.objects.filter(id=post_id).get()
        if 'file_name' in datas:
            prevFiles = dict(datas)['file_name']
            NoticeFile.objects.filter(Q(notice=post) & ~Q(image__in=prevFiles)).delete()
        for file in files.getlist('file'):
            NoticeFile.objects.create(notice=post, image=file)
        return redirect(post.get_absolute_url(page))


# 문의 목록
class BoardInquiryListView(View):
    def get(self, request):
        return render(request, 'admin/board/inquiry/list.html')


# 문의 조회
class BoardInquiryDetailView(View):
    def get(self, request):
        return render(request, 'admin/board/inquiry/detail.html')


# 문의 쓰기
class BoardInquiryWriteView(View):
    def get(self, request):
        return render(request, 'admin/board/inquiry/answer.html')


# 회원 목록
class MemberListView(View):
    def get(self, request):
        return render(request, 'admin/member/list.html')


# 회원 조회
class MemberDetailView(View):
    def get(self, request):
        return render(request, 'admin/member/detail.html')


# 회원 수정
class MemberModifyView(View):
    def get(self, request):
        return render(request, 'admin/member/modify.html')

