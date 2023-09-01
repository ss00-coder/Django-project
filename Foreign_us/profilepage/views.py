from django.db.models import F
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from event.models import Event, EventFile
from helpers.models import Helpers, HelpersFile
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
            'member_profile': member.memberfile_set.get(file_type='P') if member.memberfile_set.filter(file_type='P') else "",
            'member_background': member.memberfile_set.get(file_type='B') if member.memberfile_set.filter(file_type='B') else "",
            'login_member': "None",
            'instagram': member.membersns_set.get(sns_type='insta') if member.membersns_set.filter(sns_type='insta') else "",
            'twitter': member.membersns_set.get(sns_type='twitter') if member.membersns_set.filter(sns_type='twitter') else "",
            'youtube': member.membersns_set.get(sns_type='youtube') if member.membersns_set.filter(sns_type='youtube') else "",
            'facebook': member.membersns_set.get(sns_type='facebook') if member.membersns_set.filter(sns_type='facebook') else "",
        }

        # if member.memberfile_set.filter(file_type='P'):
        #     context['member_profile'] = member.memberfile_set.get(file_type='P')
        #
        # if member.memberfile_set.filter(file_type='B'):
        #     context['member_background'] = member.memberfile_set.get(file_type='B')

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
        all_helpers = list(Helpers.objects.filter(member=member_id, post_status='Y').order_by('-id').all())
        all_events = list(Event.objects.filter(member=member_id, post_status='Y').order_by('-id').all())
        posts = []

        for i in range(len(all_helpers)):
            id = all_helpers[i].id
            post_file = HelpersFile.objects.filter(helpers_id=id)
            member_file = all_helpers[i].member.memberfile_set.filter(file_type='P')
            post = Helpers.objects.filter(id=id) \
                .annotate(member_nickname=F('member__member_nickname'), post_file=post_file.values('image')[:1],
                          member_file=member_file.values('image')[:1]) \
                .values('id', 'member_id', 'member_nickname', 'post_title', 'post_content', 'post_file', 'member_file',
                        'created_date', 'post_view_count')
            # print(post[0])
            posts.append(post[0])

        for i in range(len(all_events)):
            id = all_events[i].id
            post_file = EventFile.objects.filter(event_id=id)
            member_file = all_events[i].member.memberfile_set.filter(file_type='P')
            post = Event.objects.filter(id=id) \
                .annotate(member_nickname=F('member__member_nickname'), post_file=post_file.values('image')[:1],
                          member_file=member_file.values('image')[:1]) \
                .values('id', 'member_id', 'member_nickname', 'post_title', 'post_content', 'post_file',
                        'member_file',
                        'created_date', 'post_view_count', 'event_location')
            # print(post[0])
            posts.append(post[0])

        # sorted_data = dict(sorted(dataList.items(), key=lambda item: item[1]['date'], reverse=True))
        # print(posts)
        # print(sorted(posts, key=lambda x: x['created_date'], reverse=True))
        sorted_posts = sorted(posts, key=lambda x: x['created_date'], reverse=True)

        posts = sorted_posts[offset:limit + 1]
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
            'member_profile': member.memberfile_set.get(file_type='P') if member.memberfile_set.filter(file_type='P') else "",
            'member_background': member.memberfile_set.get(file_type='B') if member.memberfile_set.filter(file_type='B') else "",
            'login_member': "None",
        }

        # if member.memberfile_set.filter(file_type='P'):
        #     context['member_profile'] = member.memberfile_set.get(file_type='P')
        #
        # if member.memberfile_set.filter(file_type='B'):
        #     context['member_background'] = member.memberfile_set.get(file_type='B')

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

        # return redirect(f'/profile/{teacher_id}')
        return redirect('mypage:mypay')

