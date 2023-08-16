from django.shortcuts import render
from django.views import View


# Create your views here.
class ProfileView(View):
    def get(self, request):
        return render(request, 'profile/profile.html')


class HostView(View):
    def get(self, request):
        return render(request, 'profile/host.html')
