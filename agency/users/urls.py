from django.urls import path, include

from core.views import index
from users.views import Register,UserLogin, profile

app_name = 'users'
urlpatterns = [
    path('/', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='user_login'),
    path('profile/', profile, name='profile'),

]
