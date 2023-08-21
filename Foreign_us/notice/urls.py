from django.urls import path

from event.views import EventListView, EventDetailView, EventWriteView
from helpers.views import HelpersListView, HelpersDetailView, HelpersWriteView
from notice.views import NoticeListView, NoticeDetailView, NoticeListAPI, NoticeReplyListAPI, NoticeReplyWriteAPI, \
    NoticeReplyModifyAPI, NoticeReplyDeleteAPI, NoticeLikeAddAPI, NoticeLikeDeleteAPI, NoticeLikeCountAPI, \
    NoticeLikeExistAPI

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
    path('replies/delete/<int:id>/', NoticeReplyDeleteAPI.as_view(), name='delete_get'),
    # 공지사항 좋아요
    path('likes/add/', NoticeLikeAddAPI.as_view(), name='add'),
    path('likes/delete/', NoticeLikeDeleteAPI.as_view(), name='delete'),
    path('likes/count/<int:id>/', NoticeLikeCountAPI.as_view(), name='count'),
    path('likes/exist/<int:id>/', NoticeLikeExistAPI.as_view(), name='exist'),
]
