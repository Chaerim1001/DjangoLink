#accounts/ ...
from django.urls import path
from . import views

urlpatterns = [
    path('join/', views.join, name='join'),    
    path('join/id_check', views.idCheck, name='id_check'),
    path('login/', views.login, name='login'),
]