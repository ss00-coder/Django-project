from django.db.models import F
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from lesson.models import Lesson, LessonFile
from member.models import Member, MemberFile
from payment.models import Payment
from review.models import Review, ReviewFile


# Create your views here.
class ProfileView(View):
    def get(self, request, member_id):
        member = Member.objects.get(id=member_id)

        context = {
            'member': member,
            'login_member': "None"
        }

        if member.memberfile_set.filter(file_type='P'):
            context['member_profile'] = member.memberfile_set.get(file_type='P')

        if member.memberfile_set.filter(file_type='B'):
            context['member_background'] = member.memberfile_set.get(file_type='B')

        if 'member_email' in request.session:
            login_member = Member.objects.get(member_email=request.session['member_email'])
            context['login_member'] = login_member
            if login_member.memberfile_set.filter(file_type='P'):
                context['login_member_profile'] = login_member.memberfile_set.get(file_type='P')

        return render(request, 'profile/profile.html', context)


# 후기 탭
class ProfileReviewListAPI(APIView):
    def get(self, request, member_id, page=1):
        size = 5
        offset = (page - 1) * size
        limit = page * size
        all_posts = list(Review.objects.filter(reviewed_member=member_id, post_status='Y').order_by('-id').all())
        posts = []
        for i in range(len(all_posts)):
            id = all_posts[i].id
            review_file = ReviewFile.objects.filter(review_id=id)
            member_file = all_posts[i].member.memberfile_set.filter(file_type='P')
            post = Review.objects.filter(id=id)\
                .annotate(member_nickname=F('member__member_nickname'), post_file=review_file.values('image')[:1], member_file=member_file.values('image')[:1])\
                .values('id', 'member_id', 'member_nickname', 'post_title', 'post_content', 'post_file', 'member_file', 'created_date', 'post_view_count')
            posts.append(post)

        posts = posts[offset:limit + 1]
        hasNext = False

        if len(posts) > size:
            hasNext = True
            posts.pop(size)


        context = {
            'posts': posts,
            'hasNext': hasNext
        }

        return Response(context)


# 과외글 탭
class ProfileLessonListAPI(APIView):
    def get(self, request, member_id, page=1):
        size = 5
        offset = (page - 1) * size
        limit = page * size
        all_posts = list(Lesson.objects.filter(member=member_id, post_status='Y').order_by('-id').all())
        posts = []
        for i in range(len(all_posts)):
            id = all_posts[i].id
            post_file = LessonFile.objects.filter(lesson_id=id)
            member_file = all_posts[i].member.memberfile_set.filter(file_type='P')
            post = Lesson.objects.filter(id=id) \
                .annotate(member_nickname=F('member__member_nickname'), post_file=post_file.values('image')[:1],
                          member_file=member_file.values('image')[:1]) \
                .values('id', 'member_id', 'member_nickname', 'post_title', 'post_content', 'post_file', 'member_file',
                        'created_date', 'post_view_count')
            posts.append(post)

        posts = posts[offset:limit + 1]
        hasNext = False

        if len(posts) > size:
            hasNext = True
            posts.pop(size)

        context = {
            'posts': posts,
            'hasNext': hasNext
        }

        return Response(context)


class HostView(View):
    def get(self, request, member_id):
        member = Member.objects.get(id=member_id)

        if not member.member_address:
            return redirect(f'/profile/{member.id}')

        context = {
            'member': member,
            'login_member': None
        }

        if member.memberfile_set.filter(file_type='P'):
            context['member_profile'] = member.memberfile_set.get(file_type='P')

        if member.memberfile_set.filter(file_type='B'):
            context['member_background'] = member.memberfile_set.get(file_type='B')

        if 'member_email' in request.session:
            login_member = Member.objects.get(member_email=request.session['member_email'])
            context['login_member'] = login_member
            if login_member.memberfile_set.filter(file_type='P'):
                context['login_member_profile'] = login_member.memberfile_set.get(file_type='P')

        return render(request, 'profile/host.html', context)


class PayView(View):
    def post(self, request):
        datas = request.POST
        member_id = datas['member_id']
        teacher_id = datas['teacher_id']
        lesson_type = datas['lesson_type']

        datas = {
            'member_id': member_id,
            'teacher_id': teacher_id,
            'lesson_type': lesson_type
        }

        Payment.objects.create(**datas)

        return redirect(f'/profile/{teacher_id}')

