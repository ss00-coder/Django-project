from django.urls import path
from django.views.generic import TemplateView

from member.views import MemberLoginView
from profilepage.views import ProfileView, HostView, ProfileReviewListAPI, ProfileLessonListAPI, PayView

app_name = 'profile'

urlpatterns = [
    path('<int:member_id>', ProfileView.as_view(), name='profile'),
    path('review/<int:page>', ProfileReviewListAPI.as_view(), name='review-list'),
    path('lesson/<int:page>', ProfileLessonListAPI.as_view(), name='lesson-list'),
    path('host/<int:member_id>', HostView.as_view(), name='host'),
    path('pay/', PayView.as_view(), name='pay'),
]
