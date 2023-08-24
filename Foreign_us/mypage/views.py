import math

from django.contrib.admin import helpers
from django.db.models import F, Q
from django.shortcuts import render, redirect
from django.views import View

from Foreign_us.models import Message
from event.models import Event, EventLike, EventFile
from helpers.models import Helpers, HelpersLike, HelpersFile
from lesson.models import Lesson, LessonLike, LessonFile
from member.models import Member, MemberFile, MemberSNS
from message.models import ReceiveMessage, SendMessage, ReceiveMessageFile, SendMessageFile
from review.models import Review, ReviewFile, ReviewLike


# 내 페이지
# Create your views here.
class MyProfileView(View):
    def get(self, request):
        member = Member.objects.get(member_email=request.session['member_email'])
        member_sns = member.membersns_set
        member_file = member.memberfile_set

        context = {
            'member_profile_img': member_file.get(file_type="P").image if member_file.filter(file_type="p") else '',
            'member_background_img': member_file.get(file_type="B").image if member_file.filter(file_type="B") else '',
            'member_nickname': member.member_nickname,
            'member_address': member.member_address,
            'member_intro': member.member_intro,
            'member_intro_detail': member.member_intro_detail,
            'member_sns_insta': member_sns.get(sns_type="insta").sns_url if member_sns.filter(sns_type="insta") else '',
            'member_sns_twitter': member_sns.get(sns_type="twitter").sns_url if member_sns.filter(sns_type="twitter") else '',
            'member_sns_youtube': member_sns.get(sns_type="youtube").sns_url if member_sns.filter(sns_type="youtube") else '',
            'member_sns_facebook': member_sns.get(sns_type="facebook").sns_url if member_sns.filter(sns_type="facebook") else '',
        }

        # render(request, to, context): 바로 html 화면으로 이동
        return render(request, "mypage/myprofile.html", context)

    def post(self, request):
        datas = request.POST
        files = request.FILES

        member = Member.objects.get(member_email=request.session['member_email'])
        # print(datas)
        member_datas = {
            'member_nickname': datas['member_nickname'],
            'member_address': datas['member_address'],
            'member_intro': datas['member_intro'],
            'member_intro_detail': datas['member_intro_detail'],
        }

        Member.objects.filter(id=member.id).update(**member_datas)

        # if MemberFile.objects.filter(member_id=member.id, file_type='P'):
        #     MemberFile.objects.get(member_id=member.id, file_type='P').update()

        for file in files.getlist('file1'):
            memberPimg = MemberFile.objects.get_or_create(member_id=member.id, file_type='P')[0]
            memberPimg.image = file
            memberPimg.save()

        for file in files.getlist('file2'):
            memberBimg = MemberFile.objects.get_or_create(member_id=member.id, file_type='B')[0]
            memberBimg.image = file
            memberBimg.save()


        memberSNS_insta = MemberSNS.objects.get_or_create(member_id=member.id, sns_type='insta')[0]
        memberSNS_insta.sns_url = datas['insta']
        memberSNS_insta.save()

        memberSNS_twitter = MemberSNS.objects.get_or_create(member_id=member.id, sns_type='twitter')[0]
        memberSNS_twitter.sns_url = datas['twitter']
        memberSNS_twitter.save()

        memberSNS_youtube = MemberSNS.objects.get_or_create(member_id=member.id, sns_type='youtube')[0]
        memberSNS_youtube.sns_url = datas['youtube']
        memberSNS_youtube.save()

        memberSNS_facebook = MemberSNS.objects.get_or_create(member_id=member.id, sns_type='facebook')[0]
        memberSNS_facebook.sns_url = datas['facebook']
        memberSNS_facebook.save()



        return redirect("mypage:myprofile")

# 과외 목록
class MyLessonView(View):
    def get(self, request, keyword=None, page=1, status='Y'):
        member_id = Member.objects.get(member_email=request.session['member_email']).id
        if keyword == "None":
            keyword = None

        if keyword:
            lessons = Lesson.objects.filter(member_id=member_id).filter(post_status=status).filter(Q(post_title__contains=keyword) | Q(post_content__contains=keyword)).order_by('-id').all()
        else:
            lessons = Lesson.objects.filter(member_id=member_id).filter(post_status=status).order_by('-id').all()

        size = 5
        offset = (page - 1) * size
        limit = page * size
        current_count = len(lessons)
        saved_event = Lesson.objects.filter(member_id=member_id).filter(post_status="Y").count()
        temp_event = Lesson.objects.filter(member_id=member_id).filter(post_status='N').count()
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


# 과외 목록 삭제
class MyLessonDeleteView(View):
    def get(self, request, lesson_id):
        Lesson.objects.get(id=lesson_id).delete()
        return redirect('mypage:mylesson_init')


# 과외 후기
class MyLessonReviewView(View):
    def get(self, request, keyword=None, page=1, status='Y'):

        if keyword == "None":
            keyword = None

        if keyword:
            reviews = Review.objects.filter(post_status=status).filter(Q(post_title__contains=keyword) | Q(post_content__contains=keyword)).order_by('-id').all()
        else:
            reviews = Review.objects.filter(post_status=status).order_by('-id').all()

        size = 5
        offset = (page - 1) * size
        limit = page * size
        current_count = len(reviews)
        saved_event = Review.objects.filter(post_status="Y").count()
        temp_event = Review.objects.filter(post_status='N').count()
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
        for review in reviews:
            likes = ReviewLike.objects.all().filter(review_id=review).count()
            like_list.append(likes)
            review_file = ReviewFile.objects.all().filter(review_id=review)
            image_list.append(review_file)

        likes = like_list[offset:limit]
        review_files = image_list[offset:limit]
        member_nickname = Member.objects.get(member_email=request.session['member_email']).member_nickname
        reviews = list(reviews)[offset:limit]
        combine_like = zip(reviews, likes, review_files)

        context = {
            # 'reviews': list(reviews)[offset:limit],
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

        return render(request, 'mypage/mylesson-review.html', context)


# 과외 목록 삭제
class MyLessonReviewDeleteView(View):
    def get(self, request, review_id):
        Review.objects.get(id=review_id).delete()
        return redirect('mypage:mylesson-review_init')


class MyHelpersView(View):
    def get(self, request, keyword=None, page=1, status='Y'):
        member_id = Member.objects.get(member_email=request.session['member_email']).id
        if keyword == "None":
            keyword = None

        if keyword:
            helperses = Helpers.objects.filter(member_id=member_id).filter(post_status=status).filter(
                Q(post_title__contains=keyword) | Q(post_content__contains=keyword)).order_by('-id').all()
        else:
            helperses = Helpers.objects.filter(member_id=member_id).filter(post_status=status).order_by('-id').all()

        size = 5
        offset = (page - 1) * size
        limit = page * size
        current_count = len(helperses)
        saved_event = Helpers.objects.filter(member_id=member_id).filter(post_status="Y").count()
        temp_event = Helpers.objects.filter(member_id=member_id).filter(post_status='N').count()
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
        Helpers.objects.get(id=helpers_id).delete()
        return redirect('mypage:myhelpers_init')


class MyEventView(View):
    def get(self, request, keyword=None, page=1, status='Y'):
        member_id = Member.objects.get(member_email=request.session['member_email']).id

        if keyword == "None":
            keyword = None

        if keyword:
            events = Event.objects.filter(member_id=member_id).filter(post_status=status).filter(
                Q(post_title__contains=keyword) | Q(post_content__contains=keyword)).order_by('-id').all()
        else:
            events = Event.objects.filter(member_id=member_id).filter(post_status=status).order_by('-id').all()

        size = 5
        offset = (page - 1) * size
        limit = page * size
        current_count = len(events)
        saved_event = Event.objects.filter(member_id=member_id).filter(post_status="Y").count()
        temp_event = Event.objects.filter(member_id=member_id).filter(post_status='N').count()
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
            send_messages = SendMessage.objects.filter(member_id=member_id).filter(
                Q(message_title__contains=keyword) | Q(message_content__contains=keyword)).order_by('-id').all()
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
        # 파일 첨부 이미지
        file = ReceiveMessageFile.objects.get(receive_message=receive_message)
        # 이미지
        context = {
            'member_nickname': member_nickname,
            'send_nickname': nickname,
            'receive_message': receive_message,
            'file': file
        }

        return render(request, 'message/detail.html', context)


class MyMessageWriteView(View):
    def get(self, request):
        context = {
            'member_nickname': Member.objects.get(member_email=request.session['member_email']).member_nickname
        }
        return render(request, 'message/write.html', context)

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

        receive_message = ReceiveMessage.objects.create(**receive_datas)
        send_message = SendMessage.objects.create(**Send_datas)

        if files:
            for file in files.getlist('message_file'):
                # print(member_id)
                # print(send_member_id)
                ReceiveMessageFile.objects.create(image=file, receive_message=receive_message)
                SendMessageFile.objects.create(image=file, send_message=send_message)

        return redirect('mypage:message-list-init')


class MyPayView(View):
    def get(self, request):
        return render(request, 'mypage/mypay.html')
