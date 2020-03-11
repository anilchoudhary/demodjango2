from apptwo import views
from django.urls import path

urlpatterns = [
    path('index/', views.index),
    path('users/', views.users, name = 'users'),
]
