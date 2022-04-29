#mypage/ ...
from django.urls import path

from . import views

urlpatterns = [
    path('', views.mypage, name='mypage'),
    path('new/', views.newCategory, name='new_category'),    
    path('category/<int:category_id>', views.categoryDetail, name='category_detail'),   
    path('category/addlink/<int:category_id>', views.newLink, name='new_link'),   
    path('category/updatelink/<int:category_id>', views.updateLink, name='update_link'),   
]