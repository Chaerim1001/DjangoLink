import re
from urllib import request
from django.shortcuts import redirect, render

from .forms import UserForm, LoginForm
from .models import User
from django.contrib import auth

def join(request):
    if request.method == 'GET':
        user_form = UserForm()
        return render(request, 'accounts/join.html', {'form': user_form})
    elif request.method == 'POST':
        user_form = UserForm(request.POST)
        new_user = user_form.save()
        return redirect('login')


def login(request):
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'accounts/login.html', {'form': login_form})
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        try:
            exit_user = User.objects.get(username=username)
        except:
            print('등록되지 않은 사용자입니다.')
            return redirect('login')
        
        user = auth.authenticate(request,
                username=username,
                password=password)
            
        if user is not None:
            request.session['user'] = user.id
            auth.login(request, user)
            print('로그인 성공')
            return redirect('mypage')
        else:
            print('아이디 및 비밀번호를 확인해주세요')
            return redirect('login')
        


