from django.urls import path
from django.views.generic import TemplateView

from member.views import MemberLoginView

app_name = 'member'

urlpatterns = [
    path('login/', MemberLoginView.as_view(), name='login'),
]
