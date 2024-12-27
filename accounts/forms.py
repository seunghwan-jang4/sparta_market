from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

# 회원가입 폼
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'profile_image', 'password1', 'password2']

# 프로필 수정 폼
class ProflieForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_image']
                