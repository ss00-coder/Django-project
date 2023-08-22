import math

from django.contrib.admin import helpers
from django.db.models import F, Q
from django.shortcuts import render, redirect
from django.views import View

from Foreign_us.models import Message
from event.models import Event, EventLike, EventFile
from helpers.models import Helpers, HelpersLike, HelpersFile
from lesson.models import Lesson, LessonLike
from member.models import Member
from message.models import ReceiveMessage, SendMessage, ReceiveMessageFile, SendMessageFile


# Create your views here.
class MyProfileView(View):
    # 프로필 사이드바 닉네임
    def get(self, request):
        print(1)
        member_nickname = Member.objects.get(member_email=request.session['member_email']).member_nickname
        print(member_nickname)#(멤버이메일값)
        # print(Member.objects.annotate(email=F('member_email')).values('member_nickname'))
        # member = Member.objects.get(member_email=email)
        # member = Member.objects.filter(member_nickname='짱구')
        # print(member[0].member_nickname)  // 이건 필터
        # nicknames = {'nickname': member[0].member_nickname}
        # print(nicknames)
        # print(nicknames)
        context = {
            'member_nickname': member_nickname
        }
        return render(request, 'mypage/myprofile.html', context)

    # def post(self, request, *args, **kwargs):
    #     token, member_email, member_nickname, member_birth = request.POST.values()
    #     Member.objects.create(member_email=member_email, member_password=member_password, member_name=member_name,
    #                           member_age=member_age, member_birth=member_birth)
    #     # 이동할 urls 경로를 작성한다.
    #     return redirect('/member/myprofile')


class MyLessonView(View):
    def get(self, request, page=1):
        print(2)
        size = 5
        offset = (page - 1) * size
        limit = page * size
        total = Lesson.objects.all().count()
        print(total)
        pageCount = 5
        endPage = math.ceil(page / pageCount) * pageCount
        startPage = endPage - pageCount + 1
        print(startPage)
        realEnd = math.ceil(total / size)
        endPage = realEnd if endPage > realEnd else endPage
        pageUnit = (page - 1) // 5
        if endPage == 0:
            endPage = 1

        # 좋아요
        lessons = Lesson.objects.all().order_by('-id')
        like_list = []
        for lesson in lessons:
            likes = LessonLike.objects.all().filter(lesson_id=lesson).count()
            like_list.append(likes)

        lessons = list(Lesson.objects.all().order_by('-id'))[offset:limit]
        likes = like_list[offset:limit]
        member_nickname = Member.objects.get(member_email=request.session['member_email']).member_nickname
        combine_like = zip(lessons, likes)

        context = {
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'total': total,
            'combine_like': combine_like,
            'member_nickname': member_nickname
        }
        return render(request, 'mypage/mylesson.html', context)


class MyLessonReviewView(View):
    def get(self, request):
        print(3)
        return render(request, 'mypage/mylesson-review.html')


class MyHelpersView(View):
    def get(self, request, keyword=None, page=1):

        size = 5
        offset = (page - 1) * size
        limit = page * size
        total = Helpers.objects.all().count()
        pageCount = 5
        endPage = math.ceil(page / pageCount) * pageCount
        startPage = endPage - pageCount + 1
        realEnd = math.ceil(total / size)
        endPage = realEnd if endPage > realEnd else endPage
        pageUnit = (page - 1) // 5
        if endPage == 0:
            endPage = 1

        if keyword == "None":
            keyword = None

        if keyword:
            print(keyword)
            helperses = Helpers.objects.filter(Q(post_title__contains=keyword) | Q(post_content__contains=keyword)).order_by('-id').all()
        else:
            helperses = Helpers.objects.order_by('-id').all()

        like_list = []
        image_list = []
        for helpers in helperses:
            likes = HelpersLike.objects.all().filter(helpers_id=helpers).count()
            like_list.append(likes)
            helpers_file = HelpersFile.objects.all().filter(helpers_id=helpers)
            image_list.append(helpers_file)

        likes = like_list[offset:limit]
        helpers_files = image_list[offset:limit]
        member_nickname = Member.objects.get(member_email=request.session['member_email']).member_nickname
        combine_like = zip(helperses, likes, helpers_files)
        # print(event_file)

        context = {
            'events': list(helperses)[offset:limit],
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'total': total,
            'combine_like': combine_like,
            'keyword': keyword,
            'member_nickname': member_nickname
        }

        return render(request, 'mypage/myhelpers.html', context)


class MyHelpersDeleteView(View):
    print(6)
    def get(self, request, helpers_id):
        print("helpers_id")
        Helpers.objects.get(id=helpers_id).delete()
        return redirect('mypage:myhelpers_init')


class MyEventView(View):
    def get(self, request, keyword=None, page=1, status='Y'):

        print(5)
        size = 5
        offset = (page - 1) * size
        limit = page * size
        total = Event.objects.all().count()
        pageCount = 5
        endPage = math.ceil(page / pageCount) * pageCount
        startPage = endPage - pageCount + 1
        realEnd = math.ceil(total / size)
        endPage = realEnd if endPage > realEnd else endPage
        pageUnit = (page - 1) // 5
        if endPage == 0:
            endPage = 1

        if keyword == "None":
            keyword = None

        if keyword:
            events = Event.objects.filter(post_status=status).filter(Q(post_title__contains=keyword) | Q(post_content__contains=keyword)).order_by('-id').all()
        else:
            events = Event.objects.filter(post_status=status).order_by('-id').all()
        print(events)

        like_list = []
        image_list = []
        for event in events:
            likes = EventLike.objects.all().filter(event_id=event).count()
            like_list.append(likes)
            event_files = EventFile.objects.all().filter(event_id=event)
            image_list.append(event_files)

        likes = like_list[offset:limit]
        event_files = image_list[offset:limit]
        member_nickname = Member.objects.get(member_email=request.session['member_email']).member_nickname
        combine_like = zip(events, likes, event_files)
        # print(event_file)
        print(status)
        context = {
            'events': list(events)[offset:limit],
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'total': total,
            'combine_like': combine_like,
            'keyword': keyword,
            'member_nickname': member_nickname,
            'status': status
        }

        return render(request, 'mypage/myevent.html', context)


class MyEventDeleteView(View):
    def get(self, request, event_id):
        Event.objects.get(id=event_id).delete()
        return redirect('mypage:myevent_init')


class MyMessageListView(View):
    def get(self, request, keyword=None, page=1):
        if keyword == "None":
            keyword = None

        if keyword:
            receive_messages = ReceiveMessage.objects.filter(
                Q(message_title__contains=keyword) | Q(message_content__contains=keyword)).order_by('-id').all()
        else:
            receive_messages = ReceiveMessage.objects.order_by('-id').all()

        size = 5
        offset = (page - 1) * size
        limit = page * size
        current_total = len(receive_messages)
        real_total = ReceiveMessage.objects.count()
        pageCount = 5
        endPage = math.ceil(page / pageCount) * pageCount
        startPage = endPage - pageCount + 1
        realEnd = math.ceil(current_total / size)
        endPage = realEnd if endPage > realEnd else endPage
        pageUnit = (page - 1 // 5) + 1
        if endPage == 0:
            endPage = 1

        context = {
            'receive_messages': list(receive_messages)[offset:limit],
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'current_total': current_total,
            'real_total': real_total,
            'keyword': keyword,
        }
        return render(request, 'message/list.html', context)


class MyMessageDetailView(View):
    print(8)
    def get(self, request):
        return render(request, 'message/detail.html')


class MyMessageWriteView(View):
    def get(self, request):
        return render(request, 'message/write.html')

    def post(self, request):
        datas = request.POST
        files = request.FILES
        member_id = Member.objects.get(member_email=request.session['member_email']).id
        send_member_id = Member.objects.get(member_email=datas['receive_email']).id

        receive_datas = {
            'message_title': datas['message_title'],
            'message_content': datas['message_content'],
            'message_status': 'N',
            'send_member_id': Member.objects.get(member_email=datas['receive_email']).id,
            'member_id': Member.objects.get(member_email=request.session['member_email']).id,
        }

        Send_datas = {
            'message_title': datas['message_title'],
            'message_content': datas['message_content'],
            'message_status': 'N',
            'member_id': Member.objects.get(member_email=datas['receive_email']).id,
            'receive_member_id': Member.objects.get(member_email=request.session['member_email']).id,
        }

        ReceiveMessage.objects.create(**receive_datas)
        SendMessage.objects.create(**Send_datas)

        if files:
            for file in files.getlist('message_file'):
                # print(member_id)
                # print(send_member_id)
                ReceiveMessageFile.objects.create(image=file, receive_message_id=member_id)
                SendMessageFile.objects.create(image=file, send_message_id=send_member_id)

        return redirect('mypage:message-list')


class MyPayView(View):
    def get(self, request):
        return render(request, 'mypage/mypay.html')
