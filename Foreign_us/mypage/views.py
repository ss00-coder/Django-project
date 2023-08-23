import math

from django.contrib.admin import helpers
from django.db.models import F, Q
from django.shortcuts import render, redirect
from django.views import View

from Foreign_us.models import Message
from event.models import Event, EventLike, EventFile
from helpers.models import Helpers, HelpersLike, HelpersFile
from lesson.models import Lesson, LessonLike, LessonFile
from member.models import Member
from message.models import ReceiveMessage, SendMessage, ReceiveMessageFile, SendMessageFile


# Create your views here.
class MyProfileView(View):
    # 프로필 사이드바 닉네임
    def get(self, request):

        member_nickname = Member.objects.get(member_email=request.session['member_email']).member_nickname
        print(member_nickname)  # (멤버이메일값)
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
    def get(self, request, keyword=None, page=1, status='Y'):
        if keyword == "None":
            keyword = None

        if keyword:
            lessons = Lesson.objects.filter(post_status=status).filter(Q(post_title__contains=keyword) | Q(post_content__contains=keyword)).order_by('-id').all()
        else:
            lessons = Lesson.objects.filter(post_status=status).order_by('-id').all()

        size = 5
        offset = (page - 1) * size
        limit = page * size
        current_count = len(lessons)
        saved_event = Lesson.objects.filter(post_status="Y").count()
        temp_event = Lesson.objects.filter(post_status='N').count()
        pageCount = 5
        endPage = math.ceil(page / pageCount) * pageCount
        startPage = endPage - pageCount + 1
        realEnd = math.ceil(current_count / size)
        endPage = realEnd if endPage > realEnd else endPage
        pageUnit = (page - 1) // 5
        if endPage == 0:
            endPage = 1


        like_list = []
        image_list = []
        for lesson in lessons:
            likes = LessonLike.objects.all().filter(lesson_id=lesson).count()
            like_list.append(likes)
            lesson_file = LessonFile.objects.all().filter(lesson_id=lesson)
            image_list.append(lesson_file)

        likes = like_list[offset:limit]
        lesson_files = image_list[offset:limit]
        member_nickname = Member.objects.get(member_email=request.session['member_email']).member_nickname
        lessons = list(lessons)[offset:limit]
        combine_like = zip(lessons, likes, lesson_files)

        context = {
            # 'events': list(lessons)[offset:limit],
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'combine_like': combine_like,
            'keyword': keyword,
            'member_nickname': member_nickname,
            'status': status,
            'saved_event': saved_event,
            'temp_event': temp_event,
            'current_count': current_count
        }

        return render(request, 'mypage/mylesson.html', context)


class MyLessonDeleteView(View):
    def get(self, request, lesson_id):
        print("lesson_id")
        Helpers.objects.get(id=lesson_id).delete()
        return redirect('mypage:mylesson_init')


class MyLessonReviewView(View):
    def get(self, request):
        print(3)
        return render(request, 'mypage/mylesson-review.html')


class MyHelpersView(View):
    def get(self, request, keyword=None, page=1, status='Y'):
        if keyword == "None":
            keyword = None

        if keyword:
            helperses = Helpers.objects.filter(post_status=status).filter(Q(post_title__contains=keyword) | Q(post_content__contains=keyword)).order_by('-id').all()
        else:
            helperses = Helpers.objects.filter(post_status=status).order_by('-id').all()

        size = 5
        offset = (page - 1) * size
        limit = page * size
        current_count = len(helperses)
        saved_event = Helpers.objects.filter(post_status="Y").count()
        temp_event = Helpers.objects.filter(post_status='N').count()
        pageCount = 5
        endPage = math.ceil(page / pageCount) * pageCount
        startPage = endPage - pageCount + 1
        realEnd = math.ceil(current_count / size)
        endPage = realEnd if endPage > realEnd else endPage
        pageUnit = (page - 1) // 5
        if endPage == 0:
            endPage = 1

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
        helperses = list(helperses)[offset:limit]
        combine_like = zip(helperses, likes, helpers_files)

        context = {
            # 'events': list(helperses)[offset:limit],
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'combine_like': combine_like,
            'keyword': keyword,
            'member_nickname': member_nickname,
            'status': status,
            'saved_event': saved_event,
            'temp_event': temp_event,
            'current_count': current_count
        }

        return render(request, 'mypage/myhelpers.html', context)


class MyHelpersDeleteView(View):
    def get(self, request, helpers_id):
        print("helpers_id")
        Helpers.objects.get(id=helpers_id).delete()
        return redirect('mypage:myhelpers_init')


class MyEventView(View):
    def get(self, request, keyword=None, page=1, status='Y'):

        if keyword == "None":
            keyword = None


        if keyword:
            events = Event.objects.filter(post_status=status).filter(Q(post_title__contains=keyword) | Q(post_content__contains=keyword)).order_by('-id').all()
        else:
            events = Event.objects.filter(post_status=status).order_by('-id').all()

        size = 5
        offset = (page - 1) * size
        limit = page * size
        current_count = len(events)
        saved_event = Event.objects.filter(post_status="Y").count()
        temp_event = Event.objects.filter(post_status='N').count()
        pageCount = 5
        endPage = math.ceil(page / pageCount) * pageCount
        startPage = endPage - pageCount + 1
        realEnd = math.ceil(current_count / size)
        endPage = realEnd if endPage > realEnd else endPage
        pageUnit = (page - 1) // 5
        if endPage == 0:
            endPage = 1

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
        events = list(events)[offset:limit]
        combine_like = zip(events, likes, event_files)
        # print(event_file)
        print(status)

        context = {
            # 'events': list(events)[offset:limit],
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'combine_like': combine_like,
            'keyword': keyword,
            'member_nickname': member_nickname,
            'status': status,
            'saved_event': saved_event,
            'temp_event': temp_event,
            'current_count': current_count

        }
        return render(request, 'mypage/myevent.html', context)


class MyEventDeleteView(View):
    def get(self, request, event_id):
        Event.objects.get(id=event_id).delete()
        return redirect('mypage:myevent_init')


class MyMessageListView(View):
    def get(self, request, keyword=None, page=1):
        member_id = Member.objects.get(member_email=request.session['member_email']).id
        if keyword == "None":
            keyword = None

        if keyword:
            receive_messages = ReceiveMessage.objects.filter(member_id=member_id).filter(Q(message_title__contains=keyword) | Q(message_content__contains=keyword)).order_by('-id').all()
        else:
            receive_messages = ReceiveMessage.objects.filter(member_id=member_id).order_by('-id').all()
        type = "receive"
        size = 5
        offset = (page - 1) * size
        limit = page * size
        current_total = len(receive_messages)
        send_total = SendMessage.objects.filter(member_id=member_id).count()
        receive_total = ReceiveMessage.objects.filter(member_id=member_id).count()
        pageCount = 5
        endPage = math.ceil(page / pageCount) * pageCount
        startPage = endPage - pageCount + 1
        realEnd = math.ceil(current_total / size)
        endPage = realEnd if endPage > realEnd else endPage
        pageUnit = (page - 1 // 5) + 1
        if endPage == 0:
            endPage = 1

        member_nickname = Member.objects.get(member_email=request.session['member_email']).member_nickname

        context = {
            'receive_messages': list(receive_messages)[offset:limit],
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'current_total': current_total,
            'send_total': send_total,
            'receive_total': receive_total,
            'keyword': keyword,
            'member_nickname': member_nickname,
            'type': type,
        }
        return render(request, 'message/list.html', context)


class MyMessageSendListView(View):
    def get(self, request, keyword=None, page=1):
        member_id = Member.objects.get(member_email=request.session['member_email']).id
        if keyword == "None":
            keyword = None

        if keyword:
            send_messages = SendMessage.objects.filter(member_id=member_id).filter(Q(message_title__contains=keyword) | Q(message_content__contains=keyword)).order_by('-id').all()
        else:
            send_messages = SendMessage.objects.filter(member_id=member_id).order_by('-id').all()
        type = "send"
        size = 5
        offset = (page - 1) * size
        limit = page * size
        current_total = len(send_messages)
        send_total = SendMessage.objects.filter(member_id=member_id).count()
        receive_total = ReceiveMessage.objects.filter(member_id=member_id).count()
        pageCount = 5
        endPage = math.ceil(page / pageCount) * pageCount
        startPage = endPage - pageCount + 1
        realEnd = math.ceil(current_total / size)
        endPage = realEnd if endPage > realEnd else endPage
        pageUnit = (page - 1 // 5) + 1
        if endPage == 0:
            endPage = 1

        member_nickname = Member.objects.get(member_email=request.session['member_email']).member_nickname

        context = {
            'send_messages': list(send_messages)[offset:limit],
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'current_total': current_total,
            'send_total': send_total,
            'receive_total': receive_total,
            'keyword': keyword,
            'member_nickname': member_nickname,
            'type': type,
        }
        return render(request, 'message/list.html', context)


class MyMessageDeleteView(View):
    def get(self, request, id):
        ReceiveMessage.objects.get(id=id).delete()
        ReceiveMessageFile.objects.filter(receive_message_id=id).delete()
        return redirect('mypage:message-list-init')


class MyMessageSendDeleteView(View):
    def get(self, request, id):
        SendMessage.objects.get(id=id).delete()
        SendMessageFile.objects.filter(send_message_id=id).delete()
        return redirect('mypage:message-send-list-init')


class MyMessageDetailView(View):

    def get(self, request, receive_message_id):
        member_nickname = Member.objects.get(member_email=request.session['member_email']).member_nickname

        # 받은 메세제 id
        receive_message = ReceiveMessage.objects.get(id=receive_message_id)

        # 받은 메세지 유저 id
        send_member_id = ReceiveMessage.objects.get(id=receive_message_id).send_member_id

        # 닉네임
        nickname = Member.objects.get(id=send_member_id).member_nickname
        # 프로필 이미지



        # 이미지
        context = {
            'member_nickname': member_nickname,
            'send_nickname': nickname,
            'receive_message': receive_message,
        }


        return render(request, 'message/detail.html', context)


class MyMessageWriteView(View):
    def get(self, request):
        return render(request, 'message/write.html')

    def post(self, request):
        datas = request.POST
        files = request.FILES
        # 보내는 사람(로그인된 사람)
        send_member_id = Member.objects.get(member_email=request.session['member_email']).id

        # 받는 사람 (이메일 작성해서 넘겨준 사람의 id)
        receive_member_id = Member.objects.get(member_email=datas['receive_email']).id


        receive_datas = {
            'message_title': datas['message_title'],
            'message_content': datas['message_content'],
            'message_status': 'N',
            'send_member_id': send_member_id,
            'member_id': receive_member_id,
        }

        Send_datas = {
            'message_title': datas['message_title'],
            'message_content': datas['message_content'],
            'message_status': 'N',
            'member_id': send_member_id,
            'receive_member_id': receive_member_id,
        }

        ReceiveMessage.objects.create(**receive_datas)
        SendMessage.objects.create(**Send_datas)

        if files:
            for file in files.getlist('message_file'):
                # print(member_id)
                # print(send_member_id)
                ReceiveMessageFile.objects.create(image=file, receive_message_id=receive_member_id)
                SendMessageFile.objects.create(image=file, send_message_id=send_member_id)

        return redirect('mypage:message-list-init')

class MyPayView(View):
    def get(self, request):
        return render(request, 'mypage/mypay.html')
