from django.urls import path
from django.views.generic import TemplateView

from administrator.views import BoardEventListView, BoardEventDetailView, BoardHelpersListView, BoardHelpersDetailView, \
    BoardLessonListView, BoardLessonDetailView, BoardNoticeListView, BoardNoticeDetailView, BoardNoticeWriteView, \
    BoardNoticeModifyView, BoardInquiryListView, BoardInquiryDetailView, BoardInquiryWriteView, MemberListView, \
    MemberDetailView, MemberModifyView

app_name = 'admin'

urlpatterns = [
    # 이벤트
    path('board/event/list/', BoardEventListView.as_view(), name='board-event-list'),
    path('board/event/detail/', BoardEventDetailView.as_view(), name='board-event-detail'),
    # 헬퍼스
    path('board/helpers/list/', BoardHelpersListView.as_view(), name='board-helpers-list'),
    path('board/helpers/detail/', BoardHelpersDetailView.as_view(), name='board-helpers-detail'),
    # 레슨
    path('board/lesson/list/', BoardLessonListView.as_view(), name='board-helpers-list'),
    path('board/lesson/detail/', BoardLessonDetailView.as_view(), name='board-helpers-detail'),
    # 공지사항
    path('board/notice/list/', BoardNoticeListView.as_view(), name='board-notice-list'),
    path('board/notice/detail/', BoardNoticeDetailView.as_view(), name='board-notice-detail'),
    path('board/notice/write/', BoardNoticeWriteView.as_view(), name='board-notice-write'),
    path('board/notice/modify/', BoardNoticeModifyView.as_view(), name='board-notice-modify'),
    # 문의사항
    path('board/inquiry/list/', BoardInquiryListView.as_view(), name='board-inquiry-list'),
    path('board/inquiry/detail/', BoardInquiryDetailView.as_view(), name='board-inquiry-detail'),
    path('board/inquiry/write/', BoardInquiryWriteView.as_view(), name='board-inquiry-write'),
    # 회원 관리
    path('member/list/', MemberListView.as_view(), name='list'),
    path('member/detail/', MemberDetailView.as_view(), name='detail'),
    path('member/modify/', MemberModifyView.as_view(), name='modify'),
]
