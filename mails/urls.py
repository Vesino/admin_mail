# Django
from django.urls import path

from .views import MailListView, MailCreateView, MailDeleteView, MailUpdateView, MailDetailView, send

app_name = 'mails'

urlpatterns = [
    path('', MailListView.as_view(), name='list'),
    path('create', MailCreateView.as_view(), name='create'),
    path('update/<int:pk>', MailUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', MailDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', MailDeleteView.as_view(), name='delete'),
    path('send/<int:pk>', send, name='send'),
]
