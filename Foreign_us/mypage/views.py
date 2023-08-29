import math
from itertools import chain

from django.contrib.admin import helpers
from django.db.models import F, Q
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse

from Foreign_us.models import Message
from event.models import Event, EventLike, EventFile
from helpers.models import Helpers, HelpersLike, HelpersFile
from lesson.models import Lesson, LessonLike, LessonFile
from member.models import Member, MemberFile, MemberSNS
from message.models import ReceiveMessage, SendMessage, ReceiveMessageFile, SendMessageFile
from payment.models import Payment
from review.models import Review, ReviewFile, ReviewLike

import geopy
from geopy.geocoders import Nominatim


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

        geolocator = Nominatim(user_agent='heesu')
        location = geolocator.geocode(datas['member_address'])

        member_datas = {
            'member_nickname': datas['member_nickname'],
            'member_address': datas['member_address'],
            'member_intro': datas['member_intro'],
            'member_intro_detail': datas['member_intro_detail'],
        }

        if location:
            member_datas['member_latitude'] = location.latitude
            member_datas['member_longitude'] = location.longitude

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
        for lesson in list(lessons)[offset:limit]:
            likes = LessonLike.objects.all().filter(lesson_id=lesson).count()
            like_list.append(likes)
            image_list.append(lesson.lessonfile_set.first())

        likes = like_list[offset:limit]
        combine_all = zip(list(lessons)[offset:limit], likes, image_list)

        member = Member.objects.get(member_email=request.session['member_email'])

        member_profile_img = "member/profile_icon.png"
        if member.memberfile_set.filter(file_type='P'):
            member_profile_img = member.memberfile_set.get(file_type="P").image

        context = {
            # 'events': list(lessons)[offset:limit],
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'combine_all': combine_all,
            'keyword': keyword,
            'member_nickname': member.member_nickname,
            'status': status,
            'saved_event': saved_event,
            'temp_event': temp_event,
            'current_count': current_count,
            'member_profile_img': member_profile_img
        }

        return render(request, 'mypage/mylesson.html', context)


# 과외 목록 삭제
class MyLessonDeleteView(View):
    def get(self, request, lesson_id):
        deleted_lesson = Lesson.objects.get(id=lesson_id)
        status = deleted_lesson.post_status  # 이벤트의 상태 가져오기
        deleted_lesson.delete()

        # 상태에 따라 다른 URL로 이동
        if status == 'Y':
            url = reverse('mypage:mylesson_status', args=['Y'])
        elif status == 'N':
            url = reverse('mypage:mylesson_status', args=['N'])

        return redirect(url)


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
        for review in list(reviews)[offset:limit]:
            likes = ReviewLike.objects.all().filter(review_id=review).count()
            like_list.append(likes)
            image_list.append(review.reviewfile_set.first())

        likes = like_list[offset:limit]
        combine_all = zip(list(reviews)[offset:limit], likes, image_list)

        member = Member.objects.get(member_email=request.session['member_email'])

        member_profile_img = "member/profile_icon.png"
        if member.memberfile_set.filter(file_type='P'):
            member_profile_img = member.memberfile_set.get(file_type="P").image

        context = {
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'combine_all': combine_all,
            'keyword': keyword,
            'member_nickname': member.member_nickname,
            'status': status,
            'saved_event': saved_event,
            'temp_event': temp_event,
            'current_count': current_count,
            'member_profile_img': member_profile_img
        }

        return render(request, 'mypage/mylesson-review.html', context)


# 과외 목록 삭제
class MyLessonReviewDeleteView(View):
    def get(self, request, review_id):
        deleted_review = Review.objects.get(id=review_id)
        status = deleted_review.post_status  # 이벤트의 상태 가져오기
        deleted_review.delete()

        # 상태에 따라 다른 URL로 이동
        if status == 'Y':
            url = reverse('mypage:mylesson-review_status', args=['Y'])
        elif status == 'N':
            url = reverse('mypage:mylesson-review_status', args=['N'])

        return redirect(url)


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
        for helpers in list(helperses)[offset:limit]:
            likes = HelpersLike.objects.all().filter(helpers_id=helpers).count()
            like_list.append(likes)
            image_list.append(helpers.helpersfile_set.first())

        likes = like_list[offset:limit]
        combine_all = zip(list(helperses)[offset:limit], likes, image_list)

        member = Member.objects.get(member_email=request.session['member_email'])

        member_profile_img = "member/profile_icon.png"
        if member.memberfile_set.filter(file_type='P'):
            member_profile_img = member.memberfile_set.get(file_type="P").image

        context = {
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'combine_all': combine_all,
            'keyword': keyword,
            'member_nickname': member.member_nickname,
            'status': status,
            'saved_event': saved_event,
            'temp_event': temp_event,
            'current_count': current_count,
            'member_profile_img': member_profile_img,
        }

        return render(request, 'mypage/myhelpers.html', context)


class MyHelpersDeleteView(View):
    def get(self, request, helpers_id):
        deleted_helpers = Helpers.objects.get(id=helpers_id)
        status = deleted_helpers.post_status  # 이벤트의 상태 가져오기
        deleted_helpers.delete()

        # 상태에 따라 다른 URL로 이동
        if status == 'Y':
            url = reverse('mypage:myhelpers_status', args=['Y'])
        elif status == 'N':
            url = reverse('mypage:myhelpers_status', args=['N'])

        return redirect(url)


class MyEventView(View):
    def get(self, request, keyword=None, page=1, status='Y'):
        member_id = Member.objects.get(member_email=request.session['member_email']).id

        if keyword == "None":
            keyword = None

        if keyword:
            events = Event.objects.filter(member_id=member_id).filter(post_status=status).filter(Q(post_title__contains=keyword) | Q(post_content__contains=keyword)).order_by('-id').all()
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
        for event in list(events)[offset:limit]:
            likes = EventLike.objects.all().filter(event_id=event).count()
            like_list.append(likes)
            image_list.append(event.eventfile_set.first())

        likes = like_list[offset:limit]
        combine_all = zip(list(events)[offset:limit], likes, image_list)

        member = Member.objects.get(member_email=request.session['member_email'])

        member_profile_img = "member/profile_icon.png"
        if member.memberfile_set.filter(file_type='P'):
            member_profile_img = member.memberfile_set.get(file_type="P").image

        context = {
            # 'events': list(events)[offset:limit],
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'combine_all': combine_all,
            'keyword': keyword,
            'member_nickname': member.member_nickname,
            'status': status,
            'saved_event': saved_event,
            'temp_event': temp_event,
            'current_count': current_count,
            'member_profile_img': member_profile_img,
        }
        return render(request, 'mypage/myevent.html', context)


class MyEventDeleteView(View):
    def get(self, request, event_id):
        deleted_event = Event.objects.get(id=event_id)
        status = deleted_event.post_status  # 이벤트의 상태 가져오기
        deleted_event.delete()

        # 상태에 따라 다른 URL로 이동
        if status == 'Y':
            url = reverse('mypage:myevent_status', args=['Y'])
        elif status == 'N':
            url = reverse('mypage:myevent_status', args=['N'])

        return redirect(url)


class MyPayView(View):
    def get(self, request, keyword=None, page=1, status='Y'):
        print(keyword)
        member_id = Member.objects.get(member_email=request.session['member_email']).id
        print(member_id)

        if keyword == "None":
            keyword = None
        print(keyword)
        if status == "N":
            if keyword:
                payments = Payment.objects.filter(Q(teacher_id=member_id) & (Q(member__member_nickname__contains=keyword) | Q(teacher__member_nickname__contains=keyword))).order_by('-id').all()
            else:
                payments = Payment.objects.filter(Q(teacher_id=member_id))
        else:
            if keyword:
                payments = Payment.objects.filter(Q(member_id=member_id) & (Q(member__member_nickname__contains=keyword) | Q(teacher__member_nickname__contains=keyword))).order_by('-id').all()
            else:
                payments = Payment.objects.filter(member_id=member_id).order_by('-id').all()

        size = 5
        offset = (page - 1) * size
        limit = page * size
        current_count = len(payments)
        pay_total = Payment.objects.filter(member_id=member_id).count()
        payed_total = Payment.objects.filter(teacher_id=member_id).count()
        pageCount = 5
        endPage = math.ceil(page / pageCount) * pageCount
        startPage = endPage - pageCount + 1
        realEnd = math.ceil(current_count / size)
        endPage = realEnd if endPage > realEnd else endPage
        pageUnit = (page - 1) // 5
        if endPage == 0:
            endPage = 1

        payments = list(payments)[offset:limit]
        # 결제한 핼퍼스의 닉네임
        member = Member.objects.get(member_email=request.session['member_email'])

        member_profile_img = "member/profile_icon.png"
        if member.memberfile_set.filter(file_type='P'):
            member_profile_img = member.memberfile_set.get(file_type="P").image

        context = {
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'payments': payments,
            'pay_total': pay_total,
            'payed_total': payed_total,
            'member_nickname': member.member_nickname,
            'keyword': keyword,
            'status': status,
            'current_count': current_count,
            'member_profile_img': member_profile_img,
        }

        return render(request, 'mypage/mypay.html', context)


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

        member = Member.objects.get(member_email=request.session['member_email'])

        member_profile_img = "member/profile_icon.png"
        if member.memberfile_set.filter(file_type='P'):
            member_profile_img = member.memberfile_set.get(file_type="P").image

        receive_messages_imgs = []
        for receive_message in list(receive_messages)[offset:limit]:
            receive_messages_imgs.append(receive_message.receivemessagefile_set.first())

        receive_container = zip(list(receive_messages)[offset:limit], receive_messages_imgs)

        context = {
            'receive_container': receive_container,
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'current_total': current_total,
            'send_total': send_total,
            'receive_total': receive_total,
            'keyword': keyword,
            'member_nickname': member.member_nickname,
            'member_file': member_profile_img,
            'member': member,
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

        member = Member.objects.get(member_email=request.session['member_email'])

        member_profile_img = "member/profile_icon.png"
        if member.memberfile_set.filter(file_type='P'):
            member_profile_img = member.memberfile_set.get(file_type="P").image

        send_messages_imgs = []
        for send_message in list(send_messages)[offset:limit]:
            send_messages_imgs.append(send_message.sendmessagefile_set.first())


        send_container = zip(list(send_messages)[offset:limit], send_messages_imgs)
        context = {
            'send_container': send_container,
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'current_total': current_total,
            'send_total': send_total,
            'receive_total': receive_total,
            'keyword': keyword,
            'member_nickname': member.member_nickname,
            'member_file': member_profile_img,
            'member': member,
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

        if ReceiveMessage.objects.get(id=receive_message_id).message_status == 'N':
            receive_message = ReceiveMessage.objects.get(id=receive_message_id)
            receive_message.message_status = 'Y'
            receive_message.save()



        member = Member.objects.get(member_email=request.session['member_email'])

        # 받은 메세지
        receive_message = ReceiveMessage.objects.get(id=receive_message_id)

        # 보낸 유저
        send_member = Member.objects.get(id=ReceiveMessage.objects.get(id=receive_message_id).send_member_id)

        # 보낸 유저 프로필 이미지
        send_member_profile_img = "member/profile_icon.png"
        if send_member.memberfile_set.filter(file_type="P"):
            send_member_profile_img = send_member.memberfile_set.get(file_type="P").image

        member_profile_img = "member/profile_icon.png"
        if member.memberfile_set.filter(file_type='P'):
            member_profile_img = member.memberfile_set.get(file_type="P").image

        # 받은 메세지의 이미지들
        receive_files = list(receive_message.receivemessagefile_set.all())

        context = {
            'type': 'receive',
            'member_nickname': member.member_nickname,
            'send_member_nickname': send_member.member_nickname,
            'receive_message': receive_message,
            'receive_files': receive_files,
            'send_member_profile_img': send_member_profile_img,
            'member_file': member_profile_img,
            'member': member,
        }

        return render(request, 'message/detail.html', context)

class MyMessageSendDetailView(View):


    def get(self, request, send_message_id):

        if SendMessage.objects.get(id=send_message_id).message_status == 'N':
            send_message = SendMessage.objects.get(id=send_message_id)
            send_message.message_status = 'Y'
            send_message.save()

        member = Member.objects.get(member_email=request.session['member_email'])

        # 보낸 메세지
        send_message = SendMessage.objects.get(id=send_message_id)

        # 보낸 유저
        send_member = Member.objects.get(id=SendMessage.objects.get(id=send_message_id).member_id)

        # 보낸 유저 프로필 이미지
        send_member_profile_img = "member/profile_icon.png"
        if send_member.memberfile_set.filter(file_type="P"):
            send_member_profile_img = send_member.memberfile_set.get(file_type="P").image

        member_profile_img = "member/profile_icon.png"
        if member.memberfile_set.filter(file_type='P'):
            member_profile_img = member.memberfile_set.get(file_type="P").image

        # 보낸 메세지의 이미지들
        send_files = list(send_message.sendmessagefile_set.all())

        context = {
            'type': "send",
            'member_nickname': member.member_nickname,
            'send_member_nickname': send_member.member_nickname,
            'send_message': send_message,
            'send_files': send_files,
            'send_member_profile_img': send_member_profile_img,
            'member_file': member_profile_img,
            'member': member,
        }

        return render(request, 'message/detail.html', context)


class MyMessageWriteView(View):
    def get(self, request):
        member = Member.objects.get(member_email=request.session['member_email'])
        member_profile_img = "member/profile_icon.png"
        if member.memberfile_set.filter(file_type='P'):
            member_profile_img = member.memberfile_set.get(file_type="P").image

        context = {
            'member_nickname': member.member_nickname,
            'member_file': member_profile_img,
            'member': member,
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
                ReceiveMessageFile.objects.create(image=file, receive_message=receive_message)
                SendMessageFile.objects.create(image=file, send_message=send_message)

        return redirect('mypage:message-list-init')


