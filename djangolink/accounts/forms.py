from cProfile import label
from django import forms
from .models import User
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'required': 'true', 'placeholder': '비밀번호', 'class':'form-control', 'id':'pwd1'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'required': 'true', 'placeholder': '비밀번호 확인','class':'form-control','id':'pwd2'}),
    )

    class Meta: 
        model = User
        fields = ['userid','username','email']
        widgets = {
            'userid': forms.TextInput(attrs={'placeholder': 'ID', 'required': 'true', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder':'성명', 'required':'true', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': '이메일 주소', 'required':'true', 'class': 'form-control', 'id':'email'})
        }
        label = {
            'userid': 'userid',
            'username': 'username',
            'email': 'email'
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user