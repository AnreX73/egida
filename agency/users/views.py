from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from users.forms import UserLoginForm, UserCreateForm, ChangeUserlnfoForm
from users.models import *


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

class UpdateUserInfo(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/update_user_info.html'
    form_class = ChangeUserlnfoForm
    success_url = reverse_lazy('users:profile')
    

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

        
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


def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div id='reactive_error' class='htmx__danger'> Этот пользователь уже существует </div>")
    else:
        return HttpResponse("<div id='reactive_error' class='htmx__success'> Имя пользователя свободно </div>")