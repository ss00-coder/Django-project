from django.shortcuts import render
from django.views import View


# Create your views here.
class MainView(View):
    def get(self, request):
        context = {
            'session_key': request.session.session_key,
        }
        return render(request, 'main/main.html', context)


class AboutUsView(View):
    def get(self, request):
        return render(request, 'about_us/about_us.html')

