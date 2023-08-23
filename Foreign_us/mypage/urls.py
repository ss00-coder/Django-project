from django.urls import path

from mypage import views
from mypage.views import MyProfileView, MyLessonView, MyLessonReviewView, MyHelpersView, MyEventView, MyMessageListView, \
    MyMessageDetailView, MyMessageWriteView, MyPayView, MyEventDeleteView, MyHelpersDeleteView, MyMessageSendListView, \
    MyMessageDeleteView, MyMessageSendDeleteView, MyLessonDeleteView, MyLessonReviewDeleteView

app_name = 'mypage'

urlpatterns = [
    # 프로필
    path('profile/', MyProfileView.as_view(), name='myprofile'),
    # 과외 매칭
    path('lesson/', MyLessonView.as_view(), name='mylesson_init'),
    path('lesson/<int:page>/', MyLessonView.as_view(), name='mylesson_page'),
    path('lesson/<str:keyword>/', MyLessonView.as_view(), name='mylesson_find'),
    path('lesson/tab/<str:status>/', MyLessonView.as_view(), name='mylesson_status'),
    path('lesson/tab/<str:status>/<str:keyword>/', MyLessonView.as_view(), name='mylesson_status-search'),
    path('lesson/<str:status>/<str:keyword>/<int:page>/', MyLessonView.as_view(), name='mylesson_status_save'),
    path('lesson/delete/<int:lesson_id>/', MyLessonDeleteView.as_view(), name='mylesson_delete'),
    path('lesson/<str:keyword>/<int:page>/', MyLessonView.as_view(), name='mylesson_list'),
    # 과외 리뷰
    path('lesson-review/', MyLessonReviewView.as_view(), name='mylesson-review_init'),
    path('lesson-review/<int:page>/', MyLessonReviewView.as_view(), name='mylesson-review_page'),
    path('lesson-review/<str:keyword>/', MyLessonReviewView.as_view(), name='mylesson-review_find'),
    path('lesson-review/tab/<str:status>/', MyLessonReviewView.as_view(), name='mylesson-review_status'),
    path('lesson-review/tab/<str:status>/<str:keyword>/', MyLessonReviewView.as_view(), name='mylesson-review_status-search'),
    path('lesson-review/<str:status>/<str:keyword>/<int:page>/', MyLessonReviewView.as_view(), name='mylesson-review_status_save'),
    path('lesson-review/delete/<int:lesson_id>/', MyLessonReviewDeleteView.as_view(), name='mylesson-review_delete'),
    path('lesson-review/<str:keyword>/<int:page>/', MyLessonReviewView.as_view(), name='mylesson-review_list'),
    # 헬퍼스
    path('helpers/', MyHelpersView.as_view(), name='myhelpers_init'),
    path('helpers/<int:page>/', MyHelpersView.as_view(), name='myhelpers_page'),
    path('helpers/<str:keyword>/', MyHelpersView.as_view(), name='myhelpers_find'),
    path('helpers/tab/<str:status>/', MyHelpersView.as_view(), name='myhelpers_status'),
    path('helpers/tab/<str:status>/<str:keyword>/', MyHelpersView.as_view(), name='myhelpers_status-search'),
    path('helpers/<str:status>/<str:keyword>/<int:page>/', MyHelpersView.as_view(), name='myhelpers_status_save'),
    path('helpers/delete/<int:helpers_id>/', MyHelpersDeleteView.as_view(), name='myhelpers_delete'),
    path('helpers/<str:keyword>/<int:page>/', MyHelpersView.as_view(), name='myhelpers_list'),
    # 이벤트
    path('event/', MyEventView.as_view(), name='myevent_init'),
    path('event/<int:page>/', MyEventView.as_view(), name='myevent_page'),
    path('event/<str:keyword>/', MyEventView.as_view(), name='myevent_find'),
    path('event/tab/<str:status>/', MyEventView.as_view(), name='myevent_status'),
    path('event/tab/<str:status>/<str:keyword>/', MyEventView.as_view(), name='myevent_status-search'),
    path('event/<str:status>/<str:keyword>/<int:page>/', MyEventView.as_view(), name='myevent_status_save'),
    path('event/delete/<int:event_id>/', MyEventDeleteView.as_view(), name='myevent_delete'),
    path('event/<str:keyword>/<int:page>/', MyEventView.as_view(), name='myevent_list'),
    # 쪽지
    path('message-list/', MyMessageListView.as_view(), name='message-list-init'),
    path('message-list/<str:keyword>/', MyMessageListView.as_view(), name='message-list'),
    path('message-list/<str:keyword>/<int:page>', MyMessageListView.as_view(), name='message-list-page'),
    path('message-send-list/', MyMessageSendListView.as_view(), name='message-send-list-init'),
    path('message-send-list/<str:keyword>/', MyMessageSendListView.as_view(), name='message-send-list'),
    path('message-send-list/<str:keyword>/<int:page>', MyMessageSendListView.as_view(), name='message-send-list-page'),
    path('message/delete/<int:id>', MyMessageDeleteView.as_view(), name='message-delete'),
    path('message/send/delete/<int:id>', MyMessageSendDeleteView.as_view(), name='message-send-delete'),
    path('message-detail/<int:receive_message_id>', MyMessageDetailView.as_view(), name='message-detail'),
    path('message-write/', MyMessageWriteView.as_view(), name='message-write'),
    # 결제
    path('pay/', MyPayView.as_view(), name='mypay'),
]
