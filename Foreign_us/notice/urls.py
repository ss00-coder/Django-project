from django.urls import path

from event.views import EventListView, EventDetailView, EventWriteView
from helpers.views import HelpersListView, HelpersDetailView, HelpersWriteView
from notice.views import NoticeListView, NoticeDetailView

app_name = 'notice'

urlpatterns = [
    path('list/', NoticeListView.as_view(), name='list'),
    path('detail/', NoticeDetailView.as_view(), name='detail'),
]
