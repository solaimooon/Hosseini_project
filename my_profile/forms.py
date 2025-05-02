from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import My_user
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15)
    email = forms.EmailField(required=False)

    class Meta:
        model = My_user
        fields = ['phone_number', 'email', 'password1','first_name','last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password2' in self.fields:
            del self.fields['password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="شماره موبایل")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'شماره موبایل'
        self.fields['password'].label = 'رمز عبور'
