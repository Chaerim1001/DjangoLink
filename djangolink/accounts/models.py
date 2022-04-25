from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    class Meta:
        db_table = "user"
    
    #id 고유 id
    userid = models.CharField(max_length=128, unique=True, null=False, blank = False, default='', verbose_name='아이디')
    #password 비밀번호
    #username 사용자 이름
    #email 이메일
    #date_joined 
    
    

    