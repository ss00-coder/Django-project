from django.urls import path

from event.views import EventListView, EventDetailView, EventWriteView
from helpers.views import HelpersListView, HelpersDetailView, HelpersWriteView
from notice.views import NoticeListView, NoticeDetailView, NoticeListAPI, NoticeReplyListAPI, NoticeReplyWriteAPI, \
    NoticeReplyModifyAPI, NoticeReplyDeleteAPI

app_name = 'notice'

urlpatterns = [
    # 공지사항
    path('list/', NoticeListView.as_view(), name='list-init'),
    path('list/<int:page>', NoticeListAPI.as_view(), name='list'),
    path('detail/<int:post_id>', NoticeDetailView.as_view(), name='detail'),
    # 공지사항 댓글
    path('replies/list/<int:post_id>', NoticeReplyListAPI.as_view(), name='list-init'),
    path('replies/list/<int:post_id>/<int:page>', NoticeReplyListAPI.as_view(), name='list'),
    path('replies/write/', NoticeReplyWriteAPI.as_view(), name='write'),
    path('replies/modify/', NoticeReplyModifyAPI.as_view(), name='modify'),
    path('replies/delete/', NoticeReplyDeleteAPI.as_view(), name='delete_post'),
    path('replies/delete/<int:id>/', NoticeReplyDeleteAPI.as_view(), name='delete_get'),
]
