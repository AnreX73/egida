from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    phone_number = models.CharField(max_length=30, blank=True, verbose_name='телефон для связи')

    def get_absolute_url(self):
        return reverse('profile', kwargs={'user_id': self.id})

    def __str__(self):
        return self.username
