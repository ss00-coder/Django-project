from django.urls import path
from django.views.generic import TemplateView

from administrator.views import BoardEventListView, BoardEventDetailView, BoardHelpersListView, BoardHelpersDetailView, \
    BoardLessonListView, BoardLessonDetailView, BoardNoticeListView, BoardNoticeDetailView, BoardNoticeWriteView, \
    BoardNoticeModifyView, BoardInquiryListView, BoardInquiryDetailView, BoardInquiryWriteView, MemberListView, \
    MemberDetailView, BoardNoticeDeleteAPI, \
    BoardLessonMatchListView, BoardLessonMatchDetailView, BoardEventDeleteAPI, BoardHelpersDeleteAPI, \
    BoardLessonDeleteAPI, BoardLessonMatchDeleteAPI, BoardLessonReviewDetailView, BoardLessonReviewExistAPI, \
    MemberDeleteAPI

app_name = 'admin'

urlpatterns = [
    # 이벤트
    path('board/event/list/', BoardEventListView.as_view(), name='board-event-list-init'),
    path('board/event/list/<str:keyword>/', BoardEventListView.as_view(), name='board-event-list'),
    path('board/event/list/<str:keyword>/<int:page>/', BoardEventListView.as_view(), name='board-event-list-page'),
    path('board/event/detail/<int:post_id>/<int:page>/', BoardEventDetailView.as_view(), name='board-event-detail-init'),
    path('board/event/detail/<str:keyword>/<int:post_id>/<int:page>/', BoardEventDetailView.as_view(), name='board-event-detail'),
    path('board/event/delete/', BoardEventDeleteAPI.as_view(), name='board-event-delete'),
    # 헬퍼스
    path('board/helpers/list/', BoardHelpersListView.as_view(), name='board-helpers-list-init'),
    path('board/helpers/list/<str:keyword>/', BoardHelpersListView.as_view(), name='board-helpers-list'),
    path('board/helpers/list/<str:keyword>/<int:page>/', BoardHelpersListView.as_view(), name='board-helpers-list-page'),
    path('board/helpers/detail/<int:post_id>/<int:page>/', BoardHelpersDetailView.as_view(), name='board-helpers-detail-init'),
    path('board/helpers/detail/<str:keyword>/<int:post_id>/<int:page>/', BoardHelpersDetailView.as_view(), name='board-helpers-detail'),
    path('board/helpers/delete/', BoardHelpersDeleteAPI.as_view(), name='board-helpers-delete'),
    # 과외
    path('board/lesson/list/', BoardLessonListView.as_view(), name='board-lesson-list-init'),
    path('board/lesson/list/<str:keyword>/', BoardLessonListView.as_view(), name='board-lesson-list'),
    path('board/lesson/list/<str:keyword>/<int:page>/', BoardLessonListView.as_view(), name='board-lesson-list-page'),
    path('board/lesson/detail/<int:post_id>/<int:page>/', BoardLessonDetailView.as_view(), name='board-lesson-detail-init'),
    path('board/lesson/detail/<str:keyword>/<int:post_id>/<int:page>/', BoardLessonDetailView.as_view(), name='board-lesson-detail'),
    path('board/lesson/delete/', BoardLessonDeleteAPI.as_view(), name='board-lesson-delete'),
    # 과외 매칭
    path('board/lesson-match/list/', BoardLessonMatchListView.as_view(), name='board-lesson-match-list-init'),
    path('board/lesson-match/list/<str:keyword>/', BoardLessonMatchListView.as_view(), name='board-lesson-match-list'),
    path('board/lesson-match/list/<str:keyword>/<int:page>/', BoardLessonMatchListView.as_view(), name='board-lesson-match-list-page'),
    path('board/lesson-match/detail/<int:post_id>/<int:page>/', BoardLessonMatchDetailView.as_view(), name='board-lesson-match-detail-init'),
    path('board/lesson-match/detail/<str:keyword>/<int:post_id>/<int:page>/', BoardLessonMatchDetailView.as_view(), name='board-lesson-match-detail'),
    path('board/lesson-match/delete/', BoardLessonMatchDeleteAPI.as_view(), name='board-lesson-match-delete'),
    # 과외 매칭 후기
    path('board/lesson-review/detail/<int:post_id>/<int:page>/', BoardLessonReviewDetailView.as_view(), name='board-lesson-review-detail-init'),
    path('board/lesson-review/detail/<str:keyword>/<int:post_id>/<int:page>/', BoardLessonReviewDetailView.as_view(), name='board-lesson-review-detail'),
    path('board/lesson-review/exist/<int:member_id>/<int:reviewed_member_id>/', BoardLessonReviewExistAPI.as_view(), name='exist'),
    # 공지사항
    path('board/notice/list/', BoardNoticeListView.as_view(), name='board-notice-list-init'),
    path('board/notice/list/<str:keyword>/', BoardNoticeListView.as_view(), name='board-notice-list'),
    path('board/notice/list/<str:keyword>/<int:page>/', BoardNoticeListView.as_view(), name='board-notice-list-page'),
    path('board/notice/detail/<int:post_id>/<int:page>/', BoardNoticeDetailView.as_view(), name='board-notice-detail-init'),
    path('board/notice/detail/<str:keyword>/<int:post_id>/<int:page>/', BoardNoticeDetailView.as_view(), name='board-notice-detail'),
    path('board/notice/write/<int:page>/', BoardNoticeWriteView.as_view(), name='board-notice-write'),
    path('board/notice/modify/<int:post_id>/<int:page>/', BoardNoticeModifyView.as_view(), name='board-notice-modify'),
    path('board/notice/delete/', BoardNoticeDeleteAPI.as_view(), name='board-notice-delete'),
    # 문의사항
    path('board/inquiry/list/', BoardInquiryListView.as_view(), name='board-inquiry-list-init'),
    path('board/inquiry/list/<str:keyword>/', BoardInquiryListView.as_view(), name='board-inquiry-list'),
    path('board/inquiry/list/<str:keyword>/<int:page>/', BoardInquiryListView.as_view(), name='board-inquiry-list-page'),
    path('board/inquiry/detail/<int:post_id>/<int:page>/', BoardInquiryDetailView.as_view(), name='board-inquiry-detail-init'),
    path('board/inquiry/detail/<str:keyword>/<int:post_id>/<int:page>/', BoardInquiryDetailView.as_view(), name='board-inquiry-detail'),
    path('board/inquiry/write/', BoardInquiryWriteView.as_view(), name='board-inquiry-write'),
    # 회원 관리
    path('member/list/', MemberListView.as_view(), name='member-list-init'),
    path('member/list/<str:keyword>/', MemberListView.as_view(), name='member-list'),
    path('member/list/<str:keyword>/<int:page>/', MemberListView.as_view(), name='member-list-page'),
    path('member/detail/<int:member_id>/<int:page>/', MemberDetailView.as_view(), name='member-detail-init'),
    path('member/detail/<str:keyword>/<int:member_id>/<int:page>/', MemberDetailView.as_view(), name='member-detail'),
    path('member/delete/', MemberDeleteAPI.as_view(), name='member-delete'),
    # path('member/modify/', MemberModifyView.as_view(), name='modify'),
]
