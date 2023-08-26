from django.shortcuts import render, redirect
from django.views import View
from geopy import Nominatim

import event
from event.models import Event, EventFile
from member.models import Member


# Create your views here.
class EventListView(View):
    def get(self, request):
        return render(request, 'event/list.html')


class EventDetailView(View):
    def get(self, request):
        return render(request, 'event/detail.html')


class EventWriteView(View):
    def get(self, request, post_id=None):
        # 멤버 정보
        member = Member.objects.get(member_email=request.session['member_email'])

        # 멤버 프로필 이미지 없으면 기본 이미지로
        member_profile_img = "member/profile_icon.png"

        # 멤버의 프로필 이미지가 있으면 해당 이미지로
        if member.memberfile_set.filter(file_type='P'):
            member_profile_img = member.memberfile_set.get(file_type="P").image

        if Event.objects.filter(id=post_id):
            post = Event.objects.get(id=post_id)
            post_img = post.eventfile_set.first()

            # 수정할 게시글 아이디가 맞다면 해당 게시글 수정
            context = {
                'member_file': member_profile_img,
                'post_title': post.post_title,
                'post_content': post.post_content,
                'post_status': post.post_status,
                'event_location': post.event_location,
                'member': member,
                'member_profile_img': member_profile_img,
                'post_id': post_id,
                'post_img': post_img
            }


        # 거짓이면 새로운 게시글 작성
        else:
            context = {
                'member_file': member_profile_img,
                'post_title': "",
                'post_content': "",
                'post_status': "",
                'event_location': "",
                'member': "",
                'post_id': 0,
                'post_img': ""
            }

        return render(request, 'event/write.html', context)

    def post(self, request, post_id):
        # 멤버 정보
        member = Member.objects.get(member_email=request.session['member_email'])

        # 작성 및 수정페이지에서 받아온 데이터 및 파일,태그
        datas = request.POST
        files = request.FILES

        # 주소 데이터 -> 위도, 경도로 변경
        geolocator = Nominatim(user_agent='heesu')
        location = geolocator.geocode(datas['event_location'])

        # event(게시글) 생성 및 업데이트 할때 넣을 데이터
        event_datas = {
            'post_title': datas['post_title'],
            'post_content': datas['post_content'],
            'post_status': datas['post_status'],
            'event_location': datas['event_location'],
            'member': member,
        }
        print(event_datas)
        # 데이터에 주소가 있으면 위도와 경도를 데이터로
        if location:
            event_datas['event_latitude'] = location.latitude
            event_datas['event_longitude'] = location.longitude

        # 수정할 게시글 아이디가 맞다면 해당 게시글 수정
        if Event.objects.filter(id=post_id):
            Event.objects.filter(id=post_id).update(**event_datas)
            event_post = Event.objects.get(id=post_id)

            # 파일 업로드 시 전에 있던 파일 삭제 후 새로 받은 파일로 생성
            EventFile.objects.filter(event=event_post).delete()
            for file in files.getlist('post_file'):
                EventFile.objects.create(image=file, event=event_post)

        # 수정할 게시글이 없다면 새로운 게시글 생성
        else:
            event_post = Event.objects.create(**event_datas)
            if files:
                for file in files.getlist('post_file'):
                    EventFile.objects.create(image=file, event=event_post)

        return redirect('event:list-init')

    # Create your views here.
