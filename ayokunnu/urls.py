from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='project'),
    path('submit_message/', views.sub_message, name='message_sent'),
    path('message_submitted/<int:message_id>', views.message_sub, name='message_submitted'),
    path('download/', views.download_file, name='download_file'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)