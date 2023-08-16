from django.urls import path
from django.views.generic import TemplateView

from lesson.views import LessonListView, LessonDetailView, LessonWriteView, LessonReviewDetailView, \
    LessonReviewWriteView
from member.views import MemberLoginView
from profilepage.views import ProfileView, HostView

app_name = 'lesson'

urlpatterns = [
    path('list/', LessonListView.as_view(), name='list'),
    path('detail/', LessonDetailView.as_view(), name='detail'),
    path('write/', LessonWriteView.as_view(), name='write'),
    path('review/detail/', LessonReviewDetailView.as_view(), name='review-detail'),
    path('review/write/', LessonReviewWriteView.as_view(), name='review-write'),
]
