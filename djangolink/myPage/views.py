from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import CategoryForm
from accounts.models import User


def main(request):
    if request.method == 'GET':
        user_pk = request.session.get('user')
        category_list = Category.objects.filter(share=True).order_by('-scrap', 'dt_created')[:3]
        content = {
                'category_list':category_list,
                'user_pk': user_pk
            }
        return render(request, 'main/home.html', content)


def mypage(request):
    user_pk = request.session.get('user')
    if user_pk:
        if request.method == 'GET':
            category_list = Category.objects.filter(id=user_pk)
            user = User.objects.get(id=user_pk)
            content = {
                'category_list':category_list,
                'user': user.name,
                'user_pk': user_pk
            }
            return render(request, 'mypage/mypage.html', content )
    else:
        return redirect('login')


def search(request):
    user_pk = request.session.get('user')
    content = {
        'user_pk':user_pk
    }

    if request.method == 'GET':
        path = request.get_full_path()
        if path.split('search/')[1] != '':
            search_word = request.GET['search_word']
            if search_word:
                category_list = Category.objects.filter(category_name__icontains = search_word, share = True)
                content['category_list'] = category_list
                content['search_word'] = search_word
        return render(request, 'main/search.html', content)
        

def newCategory(request):
    user_pk = request.session.get('user')
    if user_pk:
        if request.method == 'GET':
            new_form = CategoryForm()
            return render(request, 'mypage/post_category.html', {'form': new_form, 'user_pk': user_pk})
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
    if request.method == 'GET':
        category = Category.objects.get(category_id=category_id)
        link_list = Link.objects.filter(category_id=category_id)
        content = {
            'category': category,
            'link_list': link_list,
            'user_pk': user_pk
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
        else:
            return redirect('login')


def updateLink(request, category_id):
    if request.method == 'POST':
        user_pk = request.session.get('user')
        if user_pk:
            link = Link.objects.get(link_id=request.POST['link_id'])
            if(link.category_id_id==category_id):
                try:
                    link.link_url = request.POST['link_url']
                    link.description = request.POST['description']
                    link.save()
                except: 
                    link = None
                result = {
                    'result':'success',
                    'data' : "update fail" if link is None else "update success"
                    }
                return JsonResponse(result)
        else:
            return redirect('login')


def deleteLink(request, category_id, link_id):
        user_pk = request.session.get('user')
        if user_pk:
            link = Link.objects.get(link_id=link_id)
            if link.category_id_id==category_id:
                link.delete()
                return redirect('category_detail', category_id)
        else:
            return redirect('login')


def updateCategory(request, category_id):
    user_pk = request.session.get('user')
    if user_pk: 
        category = Category.objects.get(category_id=category_id)
        if request.method == 'GET':
            form = CategoryForm(instance=category)
            return render(request, 'mypage/post_category.html', {'form': form, 'user_pk':user_pk})
        elif request.method == 'POST':
            category.category_name = request.POST.get('category_name')
            category.description = request.POST.get('description')
            share = request.POST.get('share')
            if share == 'true':
                category.share = True
            else:
                category.share = False
            category.save()
            return redirect('category_detail', category_id)
    else:
        return redirect('login')


def deleteCategory(request, category_id):
        user_pk = request.session.get('user')
        if user_pk:
            category = Category.objects.get(category_id=category_id)
            category.delete()
            return redirect('mypage')


def scrabCategory(request, category_id):
    user_pk = request.session.get('user')
    if user_pk:
        category = Category.objects.get(category_id=category_id)
        if category.share: #공유 가능
            new_category = Category()
            new_category.id = User.objects.get(id=user_pk)
            new_category.category_name = category.category_name
            new_category.description = category.description
            new_category.share = True
            category.scrap = category.scrap + 1
            new_category.save()
            category.save()

            link_list = Link.objects.filter(category_id_id = category.category_id)
            for link in link_list: 
                new_link = Link()
                new_link.link_url = link.link_url
                new_link.description = link.description
                new_link.category_id = new_category
                new_link.save()
            return redirect('mypage')
    else:
        return redirect('login')
