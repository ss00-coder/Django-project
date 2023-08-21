from django.urls import path

from mypage import views
from mypage.views import MyProfileView, MyLessonView, MyLessonReviewView, MyHelpersView, MyEventView, MyMessageListView, \
    MyMessageDetailView, MyMessageWriteView, MyPayView

app_name = 'mypage'

urlpatterns = [
    # 프로필
    path('profile/', MyProfileView.as_view(), name='myprofile'),
    # 과외 매칭
    path('lesson/', MyLessonView.as_view(), name='mylesson'),
    path('lesson/<int:page>/', MyLessonView.as_view(), name='mylesson'),
    path('lesson-review/', MyLessonReviewView.as_view(), name='mylesson-review'),
    # 헬퍼스
    path('helpers/', MyHelpersView.as_view(), name='myhelpers'),
    path('helpers/<int:page>/', MyHelpersView.as_view(), name='myhelpers'),
    # 이벤트
    path('event/', MyEventView.as_view(), name='myevent'),
    path('event/<int:page>/', MyEventView.as_view(), name='myevent'),
    path('event/<str:keyword>/', MyEventView.as_view(), name='myevent'),
    path('event/<str:keyword>/<int:page>/', MyEventView.as_view(), name='myevent'),
    # 쪽지
    path('message-list/', MyMessageListView.as_view(), name='message-list'),
    path('message-list/<int:page>', MyMessageListView.as_view(), name='message-list'),
    path('message-detail/', MyMessageDetailView.as_view(), name='message-detail'),
    path('message-write/', MyMessageWriteView.as_view(), name='message-write'),
    # 결제
    path('pay/', MyPayView.as_view(), name='mypay'),
]
