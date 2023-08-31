from django.urls import path
from django.views.generic import TemplateView

from lesson.views import LessonListView, LessonDetailView, LessonWriteView, LessonReviewDetailView, \
    LessonReviewWriteView, LessonListAPI, LessonReplyListAPI, LessonReplyWriteAPI, LessonReplyModifyAPI, \
    LessonReplyDeleteAPI, LessonLikeAddAPI, LessonLikeDeleteAPI, LessonLikeCountAPI, LessonLikeExistAPI, \
    ReviewReplyListAPI, ReviewReplyWriteAPI, ReviewReplyModifyAPI, ReviewReplyDeleteAPI, ReviewLikeAddAPI, \
    ReviewLikeDeleteAPI, ReviewLikeCountAPI, ReviewLikeExistAPI
from member.views import MemberLoginView
from profilepage.views import ProfileView, HostView

app_name = 'lesson'

urlpatterns = [
    # 과외 홍보
    path('list/', LessonListView.as_view(), name='list-init'),
    path('list/<int:page>', LessonListAPI.as_view(), name='list-post'),
    path('list/<int:page>/<str:type>', LessonListAPI.as_view(), name='list'),
    path('detail/<int:post_id>', LessonDetailView.as_view(), name='detail'),
    path('write/', LessonWriteView.as_view(), name='write-init'),
    path('write/<int:post_id>', LessonWriteView.as_view(), name='write'),

    # 과외 홍보 댓글
    path('replies/list/<int:post_id>', LessonReplyListAPI.as_view(), name='list-init'),
    path('replies/list/<int:post_id>/<int:page>', LessonReplyListAPI.as_view(), name='list'),
    path('replies/write/', LessonReplyWriteAPI.as_view(), name='write'),
    path('replies/modify/', LessonReplyModifyAPI.as_view(), name='modify'),
    path('replies/delete/<int:id>/', LessonReplyDeleteAPI.as_view(), name='delete_get'),
    # 과외 홍보 좋아요
    path('likes/add/', LessonLikeAddAPI.as_view(), name='add'),
    path('likes/delete/', LessonLikeDeleteAPI.as_view(), name='delete'),
    path('likes/count/<int:id>/', LessonLikeCountAPI.as_view(), name='count'),
    path('likes/exist/<int:id>/', LessonLikeExistAPI.as_view(), name='exist'),

    # 과외 후기
    path('review/detail/<int:post_id>', LessonReviewDetailView.as_view(), name='review-detail'),
    path('review/write/', LessonReviewWriteView.as_view(), name='review-write-init'),
    path('review/write/<int:post_id>', LessonReviewWriteView.as_view(), name='review-write'),
    # 과외 후기 댓글
    path('review/replies/list/<int:post_id>', ReviewReplyListAPI.as_view(), name='review-replies-list-init'),
    path('review/replies/list/<int:post_id>/<int:page>', ReviewReplyListAPI.as_view(), name='review-replies-list'),
    path('review/replies/write/', ReviewReplyWriteAPI.as_view(), name='review-replies-write'),
    path('review/replies/modify/', ReviewReplyModifyAPI.as_view(), name='review-replies-modify'),
    path('review/replies/delete/<int:id>/', ReviewReplyDeleteAPI.as_view(), name='review-replies-delete_get'),
    # 과외 홍보 좋아요
    path('review/likes/add/', ReviewLikeAddAPI.as_view(), name='review-replies-add'),
    path('review/likes/delete/', ReviewLikeDeleteAPI.as_view(), name='review-replies-delete'),
    path('review/likes/count/<int:id>/', ReviewLikeCountAPI.as_view(), name='review-replies-count'),
    path('review/likes/exist/<int:id>/', ReviewLikeExistAPI.as_view(), name='review-replies-exist'),
]



