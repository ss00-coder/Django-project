import math
import os

from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from event.models import Event, EventFile
from helpers.models import Helpers, HelpersFile
from lesson.models import Lesson, LessonFile
from member.models import Member, MemberFile
from message.models import ReceiveMessage, SendMessage
from notice.models import Notice, NoticeFile
from payment.models import Payment
from review.models import Review
from review.serializers import ReviewSerializer


# Create your views here.
# 이벤트 목록
class BoardEventListView(View):
    def get(self, request, keyword=None, page=1):
        if keyword == "None":
            keyword = None

        if keyword:
            posts = Event.objects.filter(Q(post_title__contains=keyword) | Q(post_content__contains=keyword) | Q(
                member__member_nickname__contains=keyword) | Q(event_location__contains=keyword)).order_by(
                '-id').all()
        else:
            posts = Event.objects.order_by('-id').all()

        size = 7
        offset = (page - 1) * size
        limit = page * size
        total = len(posts)
        pageCount = 5
        endPage = math.ceil(page / pageCount) * pageCount
        startPage = endPage - pageCount + 1
        realEnd = math.ceil(total / size)
        endPage = realEnd if endPage > realEnd else endPage
        if endPage == 0:
            endPage = 1

        context = {
            'posts': list(posts)[offset:limit],
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'keyword': keyword
        }
        return render(request, 'admin/board/event/list.html', context)


# 이벤트 조회
class BoardEventDetailView(View):
    def get(self, request, post_id, keyword=None, page=1):
        if keyword == "None":
            keyword = None

        post = Event.objects.get(id=post_id)
        context = {
            'post': post,
            'post_files': list(post.eventfile_set.all()),
            'page': page,
            'keyword': keyword
        }
        return render(request, 'admin/board/event/detail.html', context)


class BoardEventDeleteAPI(APIView):
    def post(self, request):
        post_ids = request.data['post_ids']
        EventFile.objects.filter(event_id__in=post_ids).delete()
        Event.objects.filter(id__in=post_ids).delete()



# 헬퍼스 목록
class BoardHelpersListView(View):
    def get(self, request, keyword=None, page=1):
        if keyword == "None":
            keyword = None

        if keyword:
            posts = Helpers.objects.filter(Q(post_title__contains=keyword) | Q(post_content__contains=keyword) | Q(
                member__member_nickname__contains=keyword)).order_by(
                '-id').all()
        else:
            posts = Helpers.objects.order_by('-id').all()

        size = 7
        offset = (page - 1) * size
        limit = page * size
        total = len(posts)
        pageCount = 5
        endPage = math.ceil(page / pageCount) * pageCount
        startPage = endPage - pageCount + 1
        realEnd = math.ceil(total / size)
        endPage = realEnd if endPage > realEnd else endPage
        if endPage == 0:
            endPage = 1

        context = {
            'posts': list(posts)[offset:limit],
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'keyword': keyword
        }
        return render(request, 'admin/board/helpers/list.html', context)


# 헬퍼스 조회
class BoardHelpersDetailView(View):
    def get(self, request, post_id, keyword=None, page=1):
        if keyword == "None":
            keyword = None

        post = Helpers.objects.get(id=post_id)
        context = {
            'post': post,
            'post_files': list(post.helpersfile_set.all()),
            'page': page,
            'keyword': keyword
        }
        return render(request, 'admin/board/helpers/detail.html', context)

class BoardHelpersDeleteAPI(APIView):
    def post(self, request):
        post_ids = request.data['post_ids']
        HelpersFile.objects.filter(helpers_id__in=post_ids).delete()
        Helpers.objects.filter(id__in=post_ids).delete()


# 과외 목록
class BoardLessonListView(View):
    def get(self, request, keyword=None, page=1):
        if keyword == "None":
            keyword = None

        if keyword:
            posts = Lesson.objects.filter(Q(post_title__contains=keyword) | Q(post_content__contains=keyword) | Q(member__member_nickname__contains=keyword)).order_by(
                '-id').all()
        else:
            posts = Lesson.objects.order_by('-id').all()

        size = 7
        offset = (page - 1) * size
        limit = page * size
        total = len(posts)
        pageCount = 5
        endPage = math.ceil(page / pageCount) * pageCount
        startPage = endPage - pageCount + 1
        realEnd = math.ceil(total / size)
        endPage = realEnd if endPage > realEnd else endPage
        if endPage == 0:
            endPage = 1

        context = {
            'posts': list(posts)[offset:limit],
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'keyword': keyword
        }
        return render(request, 'admin/board/lesson/list.html', context)


# 과외 조회
class BoardLessonDetailView(View):
    def get(self, request, post_id, keyword=None, page=1):
        if keyword == "None":
            keyword = None

        post = Lesson.objects.get(id=post_id)
        context = {
            'post': post,
            'post_files': list(post.lessonfile_set.all()),
            'page': page,
            'keyword': keyword
        }
        return render(request, 'admin/board/lesson/detail.html', context)


class BoardLessonDeleteAPI(APIView):
    def post(self, request):
        post_ids = request.data['post_ids']
        LessonFile.objects.filter(lesson_id__in=post_ids).delete()
        Lesson.objects.filter(id__in=post_ids).delete()


# 과외 매칭 목록
class BoardLessonMatchListView(View):
    def get(self, request, keyword=None, page=1):
        if keyword == "None":
            keyword = None

        if keyword:
            posts = Payment.objects.filter(Q(teacher__member_nickname__contains=keyword) | Q(member__member_nickname__contains=keyword)).order_by('-id').all()
        else:
            posts = Payment.objects.order_by('-id').all()

        size = 7
        offset = (page - 1) * size
        limit = page * size
        total = len(posts)
        pageCount = 5
        endPage = math.ceil(page / pageCount) * pageCount
        startPage = endPage - pageCount + 1
        realEnd = math.ceil(total / size)
        endPage = realEnd if endPage > realEnd else endPage
        if endPage == 0:
            endPage = 1

        context = {
            'posts': list(posts)[offset:limit],
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'keyword': keyword
        }
        return render(request, 'admin/board/lesson-match/list.html', context)


# 과외 매칭 조회
class BoardLessonMatchDetailView(View):
    def get(self, request, post_id, keyword=None, page=1):
        if keyword == "None":
            keyword = None

        post = Payment.objects.get(id=post_id)
        teacher = Member.objects.get(id=post.teacher_id)
        student = Member.objects.get(id=post.member_id)
        context = {
            'post': post,
            'teacher_profile': teacher.memberfile_set.get(file_type='P') if teacher.memberfile_set.filter(file_type='P') else "",
            'student_profile': student.memberfile_set.get(file_type='P') if student.memberfile_set.filter(file_type='P') else "",
            'page': page,
            'keyword': keyword
        }
        return render(request, 'admin/board/lesson-match/detail.html', context)


# 과외 매칭 결제 취소
class BoardLessonMatchDeleteAPI(APIView):
    def post(self, request):
        post_ids = request.data['post_ids']
        Payment.objects.filter(id__in=post_ids).update(pay_status="N")


# 과외 매칭 후기 유무
class BoardLessonReviewExistAPI(APIView):
    def get(self, request, member_id, reviewed_member_id):
        # datas = request.data
        review = Review.objects.filter(member_id=member_id, reviewed_member_id=reviewed_member_id).order_by('-id').first()
        # return Response(review)
        return Response(ReviewSerializer(review, many=False).data)

# 과외 매칭 후기 조회
class BoardLessonReviewDetailView(View):
    def get(self, request, post_id, keyword=None, page=1):
        if keyword == "None":
            keyword = None

        post = Review.objects.get(id=post_id)
        context = {
            'post': post,
            'post_files': list(post.reviewfile_set.all()),
            'page': page,
            'keyword': keyword
        }
        return render(request, 'admin/board/lesson-match/review_detail.html', context)


# 공지사항 목록
class BoardNoticeListView(View):
    def get(self, request, keyword=None, page=1):
        if keyword == "None":
            keyword = None

        if keyword:
            posts = Notice.objects.filter(Q(post_title__contains=keyword)|Q(post_content__contains=keyword)).order_by('-id').all()
        else:
            posts = Notice.objects.order_by('-id').all()

        size = 7
        offset = (page - 1) * size
        limit = page * size
        total = len(posts)
        pageCount = 5
        endPage = math.ceil(page / pageCount) * pageCount
        startPage = endPage - pageCount + 1
        realEnd = math.ceil(total / size)
        endPage = realEnd if endPage > realEnd else endPage
        if endPage == 0:
            endPage = 1

        context = {
            'posts': list(posts)[offset:limit],
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'keyword': keyword
        }
        return render(request, 'admin/board/notice/list.html', context)


# 공지사항 조회
class BoardNoticeDetailView(View):
    def get(self, request, post_id, keyword=None, page=1):
        if keyword == "None":
            keyword = None

        post = Notice.objects.get(id=post_id)
        context = {
            'post': post,
            'post_files': list(post.noticefile_set.all()),
            'page': page,
            'keyword': keyword
        }
        return render(request, 'admin/board/notice/detail.html', context)


# 공지사항 쓰기
class BoardNoticeWriteView(View):
    def get(self, request, keyword=None, page=1):
        if keyword == "None":
            keyword = None
        return render(request, 'admin/board/notice/write.html', {'page': page, 'keyword': keyword})

    def post(self, request, page=1):
        datas = request.POST
        files = request.FILES

        datas = {
            'member_id': Member.objects.filter(member_email=request.session['member_email']).get().id,
            'post_title': datas['post_title'],
            'post_content': datas['post_content']
        }

        post = Notice.objects.create(**datas)

        for file in files.getlist('file'):
            NoticeFile.objects.create(notice=post, image=file)

        return redirect(post.get_absolute_url(page))


# 공지사항 수정
class BoardNoticeModifyView(View):
    def get(self, request, post_id, keyword=None, page=1):
        if keyword == "None":
            keyword = None
        post = Notice.objects.get(id=post_id)
        context = {
            'post': post,
            'post_files': list(post.noticefile_set.all()),
            'page': page,
            'keyword': keyword
        }
        return render(request, 'admin/board/notice/modify.html', context)

    def post(self, request, post_id, page=1):
        datas = request.POST
        files = request.FILES

        post = Notice.objects.get(id=post_id)
        post.post_title = datas['post_title']
        post.post_content = datas['post_content']
        post.save()

        print(datas)

        if 'file_name' in datas:
            prevFiles = dict(datas)['file_name']
            print(prevFiles)
            NoticeFile.objects.filter(Q(notice=post) & ~Q(image__in=prevFiles)).delete()
        else:
            NoticeFile.objects.filter(notice=post).delete()

        for file in files.getlist('file'):
            print(file)
            NoticeFile.objects.create(notice=post, image=file)
        return redirect(post.get_absolute_url(page))


# 공지사항 삭제
class BoardNoticeDeleteAPI(APIView):
    def post(self, request):
        post_ids = request.data['post_ids']
        NoticeFile.objects.filter(notice_id__in=post_ids).delete()
        Notice.objects.filter(id__in=post_ids).delete()
        # return redirect('admin:board-notice-list-init')


# 문의 목록
class BoardInquiryListView(View):
    def get(self, request, keyword=None, page=1):
        if keyword == "None":
            keyword = None

        if keyword:
            posts = ReceiveMessage.objects.filter(member__member_type='A').filter(Q(message_title__contains=keyword) | Q(message_content__contains=keyword) | Q(send_member__member_nickname__contains=keyword)).order_by(
                '-id').all()
        else:
            posts = ReceiveMessage.objects.filter(member__member_type='A').order_by('-id').all()

        size = 7
        offset = (page - 1) * size
        limit = page * size
        total = len(posts)
        pageCount = 5
        endPage = math.ceil(page / pageCount) * pageCount
        startPage = endPage - pageCount + 1
        realEnd = math.ceil(total / size)
        endPage = realEnd if endPage > realEnd else endPage
        if endPage == 0:
            endPage = 1

        context = {
            'posts': list(posts)[offset:limit],
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'keyword': keyword
        }
        return render(request, 'admin/board/inquiry/list.html', context)


# 문의 조회
class BoardInquiryDetailView(View):
    def get(self, request, post_id, keyword=None, page=1):
        if keyword == "None":
            keyword = None

        post = ReceiveMessage.objects.get(id=post_id)


        context = {
            'post': post,
            'post_files': list(post.receivemessagefile_set.all()),
            'page': page,
            'keyword': keyword
        }

        if SendMessage.objects.filter(message_id=post_id):
            answer = SendMessage.objects.filter(message_id=post_id).order_by('-id').first()
            context['answer'] = answer
            context['answer_files'] = list(answer.sendmessagefile_set.all())
        return render(request, 'admin/board/inquiry/detail.html', context)


# 문의 답변
class BoardInquiryWriteView(View):
    def get(self, request, post_id, keyword=None, page=1):
        if keyword == "None":
            keyword = None

        post = ReceiveMessage.objects.get(id=post_id)

        context = {
            'post': post,
            'post_files': list(post.receivemessagefile_set.all()),
            'page': page,
            'keyword': keyword
        }

        return render(request, 'admin/board/inquiry/answer.html', context)

    def post(self, request, post_id, page=1):
        datas = request.POST
        message = ReceiveMessage.objects.get(id=post_id)

        send_datas = {
            'member': Member.objects.filter(member_email=request.session['member_email']).get(),
            'receive_member': message.send_member,
            'message': message,
            'message_title': datas['post_title'],
            'message_content': datas['post_content']
        }

        SendMessage.objects.create(**send_datas)

        receive_datas = {
            'send_member': Member.objects.filter(member_email=request.session['member_email']).get(),
            'member': message.send_member,
            'message_title': datas['post_title'],
            'message_content': datas['post_content']
        }

        ReceiveMessage.objects.create(**receive_datas)
        ReceiveMessage.objects.filter(id=post_id).update(message_status='Y')

        return redirect(f'/administrator/board/inquiry/detail/{post_id}/{page}')



# 회원 목록
class MemberListView(View):
    def get(self, request, keyword=None, page=1):
        if keyword == "None":
            keyword = None

        if keyword:
            members = Member.objects.filter(Q(member_nickname__contains=keyword) | Q(member_email__contains=keyword)).order_by(
                '-id').all()
        else:
            members = Member.objects.order_by('-id').all()

        size = 7
        offset = (page - 1) * size
        limit = page * size
        total = len(members)
        pageCount = 5
        endPage = math.ceil(page / pageCount) * pageCount
        startPage = endPage - pageCount + 1
        realEnd = math.ceil(total / size)
        endPage = realEnd if endPage > realEnd else endPage
        if endPage == 0:
            endPage = 1

        context = {
            'members': list(members)[offset:limit],
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'keyword': keyword
        }
        return render(request, 'admin/member/list.html', context)


# 회원 조회
class MemberDetailView(View):
    def get(self, request, member_id, keyword=None, page=1):
        if keyword == "None":
            keyword = None

        member = Member.objects.get(id=member_id)
        # member_profile = member.memberfile_set.filter(file_type="P")
        lesson_match_count = Payment.objects.filter(Q(member_id=member_id) | Q(teacher_id=member_id)).count()
        lesson_count = Lesson.objects.filter(member_id=member_id).count()
        helpers_count = Helpers.objects.filter(member_id=member_id).count()
        event_count = Event.objects.filter(member_id=member_id).count()
        context = {
            'member': member,
            'member_profile': member.memberfile_set.get(file_type='P') if member.memberfile_set.filter(file_type='P') else "",
            'lesson_match_count': lesson_match_count,
            'lesson_count': lesson_count,
            'helpers_count': helpers_count,
            'event_count': event_count,
            'page': page,
            'keyword': keyword
        }
        return render(request, 'admin/member/detail.html', context)


# 회원 삭제(탈퇴회원)
class MemberDeleteAPI(APIView):
    def post(self, request):
        member_ids = request.data['member_ids']
        Member.objects.filter(id__in=member_ids).update(member_type="N")
        # member.member_type = 'N'
        # member.save()


# 회원 수정
# class MemberModifyView(View):
#     def get(self, request, page=1):
#         return render(request, 'admin/member/modify.html', {'page': page})
