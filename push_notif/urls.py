from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('notif_form/', views.notif_form, name='notif_form'),
    path('email_form/', views.email_form, name='email_form'),
]