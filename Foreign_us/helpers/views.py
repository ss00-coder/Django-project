from django.shortcuts import render
from django.views import View


# Create your views here.
class HelpersListView(View):
    def get(self, request):
        return render(request, 'helpers/list.html')


class HelpersDetailView(View):
    def get(self, request):
        return render(request, 'helpers/detail.html')


class HelpersWriteView(View):
    def get(self, request):
        return render(request, 'helpers/write.html')
