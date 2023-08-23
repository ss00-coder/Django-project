from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from lesson.models import Lesson, LessonFile
from member.models import Member
from review.models import Review, ReviewFile


# Create your views here.
class ProfileView(View):
    def get(self, request, member_id):
        member = Member.objects.get(id=member_id)
        context = {
            'member': member,
            'member_profile': member.memberfile_set.filter(file_type="P"),
            'member_background': member.memberfile_set.filter(file_type="B"),
        }
        return render(request, 'profile/profile.html', context)


# 후기 탭
class ProfileReviewListAPI(APIView):
    def get(self, request, page):
        size = 5
        offset = (page - 1) * size
        limit = page * size
        all_posts = list(Review.objects.order_by('-id').all())
        posts = []
        for i in range(len(all_posts)):
            id = all_posts[i].id
            review_file = ReviewFile.objects.filter(notice_id=id)
            post = ReviewFile.objects.filter(id=id).annotate(post_file=review_file.values('image')[:1]).values('id', 'post_title', 'post_content', 'post_file')
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
    def get(self, request, page):
        size = 5
        offset = (page - 1) * size
        limit = page * size
        all_posts = list(Lesson.objects.order_by('-id').all())
        posts = []
        for i in range(len(all_posts)):
            id = all_posts[i].id
            lesson_file = LessonFile.objects.filter(notice_id=id)
            post = ReviewFile.objects.filter(id=id).annotate(post_file=lesson_file.values('image')[:1]).values('id', 'post_title', 'post_content', 'post_file')
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
        context = {
            'member': member,
            'member_profile': member.memberfile_set.filter(file_type="P"),
            'member_background': member.memberfile_set.filter(file_type="B")
        }
        return render(request, 'profile/host.html', context)
