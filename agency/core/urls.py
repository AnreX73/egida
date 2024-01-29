from django.urls import path

from core.views import index, schedule

urlpatterns = [
    path('', index, name='home'),
    path('/schedule', schedule, name='schedule'),

]
