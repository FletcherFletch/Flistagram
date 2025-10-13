from django.contrib.auth.models import AbstractUser
from django import forms
from .models import CustomUser, Post

class SignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['picture', 'description', 'title']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
        