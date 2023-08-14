from django.urls import path
from django.views.generic import TemplateView

app_name = 'member'

urlpatterns = [
    path('login/', TemplateView.as_view(template_name='login/login.html')),
    # path('login/', TemplateView.as_view(template_name='mypage/login.html')),
    # path('join/', MemberJoinView.as_view(), name='join'),
    # path('login/', MemberLoginView.as_view(), name='login'),
    # path('logout/', MemberLogoutView.as_view(), name='logout'),
    # path('success/', TemplateView.as_view(template_name='member/success.html'), name='success'),
    # path('fail/', TemplateView.as_view(template_name='member/fail.html'), name='fail'),
]
