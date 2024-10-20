from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='project'),
    path('submit_message/', views.sub_message, name='message_sent'),
    path('message_submitted/<int:message_id>', views.message_sub, name='message_submitted')
]