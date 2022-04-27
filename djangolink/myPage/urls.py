#mypage/ ...
from django.urls import path

from . import views

urlpatterns = [
    path('', views.mypage, name='mypage'),
    path('new/', views.newCategory, name='new_category'),    
]