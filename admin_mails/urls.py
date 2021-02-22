# Django
from django.contrib import admin
from django.urls import path, include

# Views
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('mails/', include('mails.urls'))
]
