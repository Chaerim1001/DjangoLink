from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    class Meta:
        db_table = "user"
    
    #id 고유 id
    name = models.CharField(max_length=128, unique=False, null=False, blank = False, default='', verbose_name='이름')
    #password 비밀번호
    #username 사용자 아이디
    #email 이메일
    #date_joined 
    
    

    