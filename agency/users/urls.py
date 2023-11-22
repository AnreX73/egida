from django.urls import path, include

from core.views import index
from users.views import UserLogin, profile

app_name = 'users'
urlpatterns = [
    path('/', include('django.contrib.auth.urls')),
    path('login/', UserLogin.as_view(), name='user_login'),
    path('profile/', profile, name='profile'),

]
