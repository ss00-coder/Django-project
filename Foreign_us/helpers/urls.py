from django.urls import path

from helpers.views import HelpersListView, HelpersDetailView, HelpersWriteView, HelpersListAPI, HelpersReplyListAPI, \
    HelpersReplyWriteAPI, HelpersReplyModifyAPI, HelpersReplyDeleteAPI, HelpersLikeAddAPI, HelpersLikeDeleteAPI, \
    HelpersLikeCountAPI, HelpersLikeExistAPI

app_name = 'helpers'

urlpatterns = [
    path('list/', HelpersListView.as_view(), name='list-init'),
    path('list/<int:page>/<str:type>/', HelpersListAPI.as_view(), name='list_type'),
    path('detail/<int:post_id>', HelpersDetailView.as_view(), name='detail'),
    path('write/', HelpersWriteView.as_view(), name='write-init'),
    path('write/<int:post_id>', HelpersWriteView.as_view(), name='write_modify'),
    # 이벤트 댓글
    path('replies/list/<int:post_id>', HelpersReplyListAPI.as_view(), name='list-init'),
    path('replies/list/<int:post_id>/<int:page>', HelpersReplyListAPI.as_view(), name='list'),
    path('replies/write/', HelpersReplyWriteAPI.as_view(), name='write'),
    path('replies/modify/', HelpersReplyModifyAPI.as_view(), name='modify'),
    path('replies/delete/<int:id>/', HelpersReplyDeleteAPI.as_view(), name='delete_get'),
    # 이벤트 좋아요
    path('likes/add/', HelpersLikeAddAPI.as_view(), name='add'),
    path('likes/delete/', HelpersLikeDeleteAPI.as_view(), name='delete'),
    path('likes/count/<int:id>/', HelpersLikeCountAPI.as_view(), name='count'),
    path('likes/exist/<int:id>/', HelpersLikeExistAPI.as_view(), name='exist'),
]