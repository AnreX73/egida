from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from users.forms import UserLoginForm, UserCreateForm


class Register(View):
    template_name = 'users/register.html'

    def get(self, request):
        context = {
            'form': UserCreateForm(),
            'title': 'регистрация',
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('users:profile')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

        
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
