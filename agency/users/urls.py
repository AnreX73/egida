from django.urls import path, include, reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from users.views import Register, UserLogin, profile, UpdateUserInfo, check_username

app_name = 'users'
urlpatterns = [
    path('/', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='user_login'),
    path('profile/', profile, name='profile'),
    path('update_user_info/', UpdateUserInfo.as_view(), name='update_user_info'),

    path('password-reset/',
         PasswordResetView.as_view(
            template_name="users/password_reset_form.html",
            email_template_name="users/password_reset_email.html",
            success_url=reverse_lazy("users:password_reset_done"),
         ),
         name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            success_url=reverse_lazy("users:password_reset_complete")
         ),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
         name='password_reset_complete'),
    
]

hmtx_views = [
    path("check-username/",check_username, name='check-username'),
]

urlpatterns += hmtx_views

