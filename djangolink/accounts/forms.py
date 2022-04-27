from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'required': 'true', 'placeholder': '비밀번호', 'class':'form-control', 'id':'pwd1', 'check': 'false'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'required': 'true', 'placeholder': '비밀번호 확인','class':'form-control','id':'pwd2'}),
    )

    class Meta: 
        model = User
        fields = ['username','name','email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'ID', 'required': 'true', 'class': 'form-control', 'id':'username', 'check':'false'}),
            'name': forms.TextInput(attrs={'placeholder':'성명', 'required':'true', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': '이메일 주소', 'required':'true', 'class': 'form-control', 'id':'email'})
        }
        label = {
            'username': 'username',
            'name': 'name',
            'email': 'email'
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class LoginForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ['username','password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'ID', 'required': 'true', 'class': 'form-control','name': 'username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password', 'required': 'true','class': 'form-control', 'name': 'password'})
           }
        label = {
            'username': 'username',
            'password': 'password'
            }
