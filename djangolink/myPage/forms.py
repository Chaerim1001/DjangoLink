from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta: 
        model = Category
        fields = ['category_name','description','share']
        widgets = {
            'category_name': forms.TextInput(attrs={'required': 'true', 'class': 'form-control', 'name':'category_name'}),
            'description': forms.TextInput(attrs={'required':'true', 'class': 'form-control','name': 'description'}),
        }
        label = {
            'category_name': 'category_name',
            'description': 'description',
        }
