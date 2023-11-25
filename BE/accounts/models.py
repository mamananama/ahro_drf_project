from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=24, unique=True)
    email = models.EmailField('email address', unique=True)
    password = models.CharField("password", max_length=128)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
