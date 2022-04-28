from hashlib import new
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import CategoryForm
from accounts.models import User


def mypage(request):
    user_pk = request.session.get('user')
    if user_pk:
        if request.method == 'GET':
            category_list = Category.objects.filter(id=user_pk)
            user = User.objects.get(id=user_pk)
            content = {
                'category_list':category_list,
                'user': user.name
            }
            return render(request, 'mypage/mypage.html', content )
    else:
        return redirect('login')


def newCategory(request):
    user_pk = request.session.get('user')
    if user_pk:
        if request.method == 'GET':
            new_form = CategoryForm()
            return render(request, 'mypage/new_category.html', {'form': new_form})
        elif request.method == 'POST':
            new_category = Category()
            new_category.id = User.objects.get(id=user_pk)
            new_category.category_name = request.POST.get('category_name')
            new_category.description = request.POST.get('description')

            share = request.POST.get('share')
            if share == 'true':
                new_category.share = True
            else:
                new_category.share = False
            new_category.save()
            return redirect('mypage')
    else:
        return redirect('login')


def categoryDetail(request, category_id):
    user_pk = request.session.get('user')
    if user_pk:
        if request.method == 'GET':
            category = Category.objects.get(category_id=category_id)
            link_list = Link.objects.filter(category_id=category_id)
            content = {
                'category': category,
                'link_list': link_list
            }
            return render(request, 'mypage/category_detail.html', content)


def newLink(request, category_id):
    if request.method == 'POST':
        user_pk = request.session.get('user')
        if user_pk:
            try:
                new_link = Link()
                new_link.link_url = request.POST['link_url']
                new_link.description = request.POST['description']
                new_link.category_id = Category.objects.get(category_id=category_id)
                new_link.save()
            except:
                new_link = None
            result = {
                'result':'success',
                'data' : "add fail" if new_link is None else "add success"
                }
            return JsonResponse(result)



