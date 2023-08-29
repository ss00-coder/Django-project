from django.urls import path

from event.views import EventListView, EventDetailView, EventWriteView, EventListAPI, EventReplyListAPI, \
    EventReplyWriteAPI, EventReplyModifyAPI, EventReplyDeleteAPI, EventLikeAddAPI, EventLikeDeleteAPI, \
    EventLikeExistAPI, EventLikeCountAPI
from helpers.views import HelpersListView, HelpersDetailView, HelpersWriteView

app_name = 'event'

urlpatterns = [
    # 이벤트
    path('list/', EventListView.as_view(), name='list-init'),
    path('list/<int:page>/<str:type>/', EventListAPI.as_view(), name='list_type'),
    path('detail/<int:post_id>', EventDetailView.as_view(), name='detail'),
    path('write/', EventWriteView.as_view(), name='write-init'),
    path('write/<int:post_id>', EventWriteView.as_view(), name='write_modify'),
    # 이벤트 댓글
    path('replies/list/<int:post_id>', EventReplyListAPI.as_view(), name='list-init'),
    path('replies/list/<int:post_id>/<int:page>', EventReplyListAPI.as_view(), name='list'),
    path('replies/write/', EventReplyWriteAPI.as_view(), name='write'),
    path('replies/modify/', EventReplyModifyAPI.as_view(), name='modify'),
    path('replies/delete/<int:id>/', EventReplyDeleteAPI.as_view(), name='delete_get'),
    # 이벤트 좋아요
    path('likes/add/', EventLikeAddAPI.as_view(), name='add'),
    path('likes/delete/', EventLikeDeleteAPI.as_view(), name='delete'),
    path('likes/count/<int:id>/', EventLikeCountAPI.as_view(), name='count'),
    path('likes/exist/<int:id>/', EventLikeExistAPI.as_view(), name='exist'),
]