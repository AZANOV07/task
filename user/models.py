from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    AUTH_CHOICES = (
        (1, 'Аутентифицирован'),
        (0, 'Не аутентифицирован'),
    )
    is_verified = models.IntegerField(choices=AUTH_CHOICES, default=0)
    code = models.CharField(max_length=6, null=True, blank=True)