from django.urls import path
from django.views.generic import TemplateView

from member.views import MemberLoginView, MemberLogoutView, KakaoView

app_name = 'member'

urlpatterns = [
    # path('login/', MemberLoginView.as_view(), name='login'),
    path('login/', MemberLoginView.as_view(), name='login'),
    path('oauth/redirect/', KakaoView.as_view(), name='redirect'),
    path('logout/', MemberLogoutView.as_view(), name='logout'),
]
