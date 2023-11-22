from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-input'}), )
    password = forms.CharField(label=_("password"), widget=forms.PasswordInput(attrs={'class': 'form-input'}), )
