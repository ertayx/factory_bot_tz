import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth. base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, first_name, password, **kwargs):
        if not first_name:
            return ValueError('first_name должен быть обязательно передан')
        user = self.model(first_name=first_name, **kwargs)
        user.generate_telegram_token()
        user.set_password(password)
        user.save()
        return user

    def create_user(self, first_name, password, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(first_name, password, **kwargs)

    def create_superuser(self, first_name, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        if kwargs.get('is_staff') is not True:
            raise ValueError('У суперюзера должно быть поле is_staff=True')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('У суперюзера должно быть поле is_superuser=True')
        return self._create_user(first_name, password, **kwargs)


class CustomUser(AbstractUser):
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, unique=True)
    telegram_token = models.UUIDField()

    objects = UserManager()


    USERNAME_FIELD = 'first_name'
    REQUIRED_FIELDS = []

    def generate_telegram_token(self):
        self.telegram_token = uuid.uuid4().hex