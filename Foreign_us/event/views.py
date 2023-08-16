from django.shortcuts import render
from django.views import View


# Create your views here.
class EventListView(View):
    def get(self, request):
        return render(request, 'event/list.html')


class EventDetailView(View):
    def get(self, request):
        return render(request, 'event/detail.html')


class EventWriteView(View):
    def get(self, request):
        return render(request, 'event/write.html')

# Create your views here.
