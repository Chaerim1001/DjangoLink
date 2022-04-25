import re
from django.shortcuts import redirect, render

from .forms import UserForm

# Create your views here.
def join(request):
    if request.method == 'GET':
        user_form = UserForm()
        return render(request, 'accounts/join.html', {'form': user_form})
    elif request.method == 'POST':
        user_form = UserForm(request.POST)
        new_user = user_form.save()
        print(new_user)
        return redirect('join')


