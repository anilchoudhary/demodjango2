from apptwo import views
from django.urls import path

urlpatterns = [
    path('index/', views.help),
    path('users/', views.users, name = 'users'),
]
