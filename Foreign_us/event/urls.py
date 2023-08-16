from django.urls import path

from event.views import EventListView, EventDetailView, EventWriteView
from helpers.views import HelpersListView, HelpersDetailView, HelpersWriteView

app_name = 'event'

urlpatterns = [
    path('list/', EventListView.as_view(), name='list'),
    path('detail/', EventDetailView.as_view(), name='detail'),
    path('write/', EventWriteView.as_view(), name='write'),
]
