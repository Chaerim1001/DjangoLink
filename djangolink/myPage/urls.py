#mypage/ ...
from django.urls import path

from . import views

urlpatterns = [
    path('', views.mypage, name='mypage'),
    path('new/', views.newCategory, name='new_category'),    
    path('category/<int:category_id>', views.categoryDetail, name='category_detail'),   
    path('category/addlink/<int:category_id>', views.newLink, name='new_link'),   
    path('category/updatelink/<int:category_id>', views.updateLink, name='update_link'),   
    path('category/deletelink/<int:category_id>/<int:link_id>', views.deleteLink, name='delete_link'),   
    path('updatecategory/<int:category_id>', views.updateCategory, name='update_category'),   
    path('deletecategory/<int:category_id>', views.deleteCategory, name='delete_category'),   
]