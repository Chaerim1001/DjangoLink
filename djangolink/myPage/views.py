from django.shortcuts import redirect, render
from .models import Category
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
