# ObjectDetection/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('start/', views.start_stream, name='start_stream'),
    path('stop/', views.stop_stream, name='stop_stream'),
    path('video_feed/', views.video_feed, name='video_feed'),
]
