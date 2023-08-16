from django.urls import path

from helpers.views import HelpersListView, HelpersDetailView, HelpersWriteView

app_name = 'helpers'

urlpatterns = [
    path('list/', HelpersListView.as_view(), name='list'),
    path('detail/', HelpersDetailView.as_view(), name='detail'),
    path('write/', HelpersWriteView.as_view(), name='write'),
]
