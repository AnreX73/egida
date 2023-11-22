from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import render

from users.forms import UserLoginForm


class UserLogin(LoginView):
    template_name = 'users/user_login.html'
    form_class = UserLoginForm


@login_required(login_url='/')
def profile(request):
    user = request.user
    context = {
        'user': user,

    }
    return render(request, 'users/profile.html', context=context)
