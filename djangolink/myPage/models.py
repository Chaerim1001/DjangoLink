from django.db import models
from accounts import models as accounts_models


#카테고리 테이블
class Category(models.Model):
    class Meta:
        db_table= 'category'
    
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=128, null=False, blank = False, default='', verbose_name='카테고리 이름')
    description = models.TextField(verbose_name='카테고리 설명') 
    share = models.BooleanField(verbose_name='공유 여부')
    scrap = models.IntegerField(default=0, verbose_name='스크랩 횟수')
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_modified = models.DateTimeField(auto_now=True)
    id = models.ForeignKey(accounts_models.User, on_delete=models.CASCADE, verbose_name="카테고리 사용자 id")



class Link(models.Model):
    class Meta:
        db_table= 'link'
    
    link_id = models.AutoField(primary_key=True)
    link_url = models.CharField(max_length=128, null=False, blank = False, default='', verbose_name='링크 주소')
    description = models.TextField(default='', verbose_name='링크 설명') 
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="카테고리 id")

