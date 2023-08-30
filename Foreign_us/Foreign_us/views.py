from itertools import count

from django.db.models import Count, F, Q
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

import member
from event.models import Event, EventFile
from helpers.models import Helpers, HelpersFile
from helpers.serializers import HelpersSerializer
from member.models import Member, MemberFile
from payment.models import Payment


# Create your views here.
class MainView(View):
    def get(self, request):
        all_popular_teachers = list(Payment.objects.values("teacher_id").annotate(count=Count("teacher_id")).order_by('-count').values('count', 'teacher_id'))
        popular_teachers = []

        for temp in all_popular_teachers:
            teacher_id = temp['teacher_id']
            member_files = MemberFile.objects.filter(member_id=teacher_id, file_type="P")
            teacher = Member.objects.filter(id=teacher_id).annotate(member_file=member_files.values('image')).first()
            popular_teachers.append(teacher)

        pop_events = []
        new_events = Event.objects.order_by("-id").all()

        for event in new_events:
            event_file = EventFile.objects.filter(event_id=event.id)
            post = Event.objects.filter(id=event.id).annotate(post_file=event_file.values('image')[:1]).values('id', 'post_title', 'post_content', 'post_file')
            pop_events.append(post)

        new_members_list = list(Member.objects.order_by('-id').values('id'))

        new_members = []
        for temp in new_members_list:
            temp_id = temp['id']
            member_files = MemberFile.objects.filter(member_id=temp_id, file_type="P")
            member_temp = Member.objects.filter(id=temp_id).annotate(member_file=member_files.values('image')).first()
            new_members.append(member_temp)

        # members = Member.objects.order_by('-id').all()
        # print(members)
        # new_members = members.values('member_nickname', 'member_intro', 'memberfile__file_type="P"')
        # member_info = Member.objects.annotate(member_profile=member_files.values('image')[:1]).values('member_nickname','member_intro','member_profile')
        # new_members.append(member_info)
        # print(Post.objects.filter(member_id=9).values('id', 'post_title', 'post_content', 'member__member_name'))
        # members = Member.objects.order_by('-id').filter(Q(memberfile__file_type='P')|Q(memberfile__isnull=True)).values("memberfile__image","memberfile__file_type","member_nickname","member_intro")
        # members = Member.objects.order_by('-id').values("memberfile__file_type")
        # print(members)
        # print(members)

        first_event = pop_events[0]

        second_event = pop_events[1]
        # print(second_event)

        context = {
            'session_key': request.session.session_key,
            'popular_teachers': popular_teachers,
            'first_event': first_event,
            'second_event': second_event,
            'new_members': new_members,
        }
        return render(request, 'main/main.html', context)


class AboutUsView(View):
    def get(self, request):
        return render(request, 'about_us/about_us.html')


# 헬퍼스 최근 목록
class MainHelpersListAPI(APIView):
    def get(self, request, page):
        size = 5
        offset = (page - 1) * size
        limit = page * size
        posts = []

        all_posts = list(Helpers.objects.order_by('-id').all())

        for i in range(len(all_posts)):
            id = all_posts[i].id
            member_id = all_posts[i].member_id
            member_files = MemberFile.objects.filter(member_id=member_id, file_type="P")
            helpers_file = HelpersFile.objects.filter(helpers_id=id)
            post = Helpers.objects.filter(id=id).annotate(post_file=helpers_file.values('image')[:1], member_file=member_files.values('image')[:1], nickname=F('member__member_nickname')).values('id', 'post_title', 'post_content', 'post_file', 'nickname', 'post_view_count', 'created_date', 'member_file')
            posts.append(post)

        posts = posts[offset:limit]  # Remove +1 from the limit

        if len(posts) > size:
            posts.pop(size)

        context = {
            # 'posts': HelpersSerializer(posts, many=True).data,
            'posts': posts
        }

        return Response(context)