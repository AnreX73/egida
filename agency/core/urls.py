from django.urls import path

from core.views import index, schedule, doctor_profile

urlpatterns = [
    path('', index, name='home'),
    path('schedule/', schedule, name='schedule'),
    path('doctor_profile/<slug:slug>', doctor_profile, name='doctor_profile'),

]
