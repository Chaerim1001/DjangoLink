from django.shortcuts import render

def mypage(request):
    return render(request, 'mypage/mypage.html' )


