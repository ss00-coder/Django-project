from django.urls import path
from django.views.generic import TemplateView

from member.views import MemberLoginView
from profilepage.views import ProfileView, HostView

app_name = 'profile'

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('host/', HostView.as_view(), name='host'),
]
