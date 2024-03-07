from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    class SexChoices(models.TextChoices):
        MALE = 'MALE', 'Мужской'
        FEMALE = 'FEMALE', 'Женский'
    phone_number = models.CharField(max_length=30, blank=True, verbose_name='телефон для связи')
    day_of_birth = models.DateField(blank=True, null=True, verbose_name='дата рождения')
    sex = models.CharField(max_length=7, choices=SexChoices.choices, blank=True, verbose_name='пол', default='MALE')

    def get_absolute_url(self):
        return reverse('profile', kwargs={'user_id': self.id})

    def __str__(self):
        return self.username
