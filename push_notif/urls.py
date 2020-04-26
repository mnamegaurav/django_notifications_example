from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('fcm_insert/', views.fcm_insert, name='fcm_insert'),
    path('send_notif/', views.send_notif, name='send_notif'),
    path('send_email/', views.send_email, name='send_email'),
]