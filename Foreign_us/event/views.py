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
        member = Member.objects.get(member_email=request.session['member_email'])
        member_profile_img = "member/profile_icon.png"
        if member.memberfile_set.filter(file_type='P'):
            member_profile_img = member.memberfile_set.get(file_type="P").image
        if Event.objects.filter(id=post_id):
            post = Event.objects.get(id=post_id)
            context = {
                'member_file': member_profile_img,
                'post_title': post.post_title,
                'post_content': post.post_content,
                'post_status': post.post_status,
                'event_location': post.event_location,
                'member': member,
                'post_id': post_id,
            }
        else:
            context = {
                'member_file': member_profile_img,
                'post_title': "",
                'post_content': "",
                'post_status': "",
                'event_location': "",
                'member': "",
                'post_id': 0,
            }

        return render(request, 'event/write.html', context)

    def post(self, request, post_id):
        member = Member.objects.get(member_email=request.session['member_email'])
        datas = request.POST
        files = request.FILES

        geolocator = Nominatim(user_agent='heesu')
        location = geolocator.geocode(datas['event_location'])

        event_datas = {
            'post_title': datas['post_title'],
            'post_content': datas['post_content'],
            'post_status': datas['post_status'],
            'event_location': datas['event_location'],
            'member': member,
        }

        if location:
            event_datas['event_latitude'] = location.latitude
            event_datas['event_longitude'] = location.longitude
            print(event_datas)

        if Event.objects.filter(id=post_id):
            Event.objects.filter(id=post_id).update(**event_datas)
            event_post = Event.objects.get(id=post_id)

            if files:
                EventFile.objects.filter(event_id=post_id).delete()
                for file in files.getlist('post_file'):
                    EventFile.objects.create(image=file, event=event_post)

        else:
            event_post = Event.objects.create(**event_datas)
            if files:
                for file in files.getlist('post_file'):
                    EventFile.objects.create(image=file, event=event_post)

        return redirect('event:list-init')


# Create your views here.
