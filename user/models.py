from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save()

        return user


class User(AbstractUser):
    AUTH_CHOICES = (
        (1, 'Аутентифицирован'),
        (0, 'Не аутентифицирован'),
    )
    is_verified = models.IntegerField(choices=AUTH_CHOICES, default=0)
    code = models.CharField(max_length=6, null=True, blank=True)
    email = models.EmailField('Email', unique=True)
    password = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)