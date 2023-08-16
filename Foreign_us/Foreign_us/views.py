from django.shortcuts import render
from django.views import View


# Create your views here.
class MainView(View):
    def get(self, request):
        return render(request, 'main/main.html')


class AboutUsView(View):
    def get(self, request):
        return render(request, 'about_us/about_us.html')

