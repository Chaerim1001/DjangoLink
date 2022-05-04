from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta: 
        model = Category
        fields = ['category_name','description']
        widgets = {
            'category_name': forms.TextInput(attrs={'required': 'true', 'class': 'form-control', 'name':'category_name', 'placeholder':'Category name'}),
            'description': forms.TextInput(attrs={'required':'true', 'class': 'form-control','name': 'description', 'placeholder':'Category description'}),
        }
        label = {
            'category_name': 'category_name',
            'description': 'description',
        }