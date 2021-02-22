# Django
from django.urls import path

from .views import MailListView, MailCreateView, MailDeleteView

app_name = 'mails'

urlpatterns = [
    path('', MailListView.as_view(), name='list'),
    path('create', MailCreateView.as_view(), name='create'),
    path('delete/<int:pk>', MailDeleteView.as_view(), name='delete'),
]
