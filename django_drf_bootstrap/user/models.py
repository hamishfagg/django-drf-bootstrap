from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    id = models.BigAutoField(auto_created=True, primary_key=True, verbose_name='ID')
    username = models.CharField(max_length=64, unique=True, null=False)
    email = models.EmailField(unique=True, null=False)
