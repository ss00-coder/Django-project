from django.shortcuts import render
from django.views import View


# Create your views here.
class LessonListView(View):
    def get(self, request):
        return render(request, 'lesson/list.html')


class LessonDetailView(View):
    def get(self, request):
        return render(request, 'lesson/detail.html')


class LessonWriteView(View):
    def get(self, request):
        return render(request, 'lesson/write.html')


class LessonReviewDetailView(View):
    def get(self, request):
        return render(request, 'lesson/review-detail.html')


class LessonReviewWriteView(View):
    def get(self, request):
        return render(request, 'lesson/review-write.html')



