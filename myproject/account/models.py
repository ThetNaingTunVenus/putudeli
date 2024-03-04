from django.db import models
from django.contrib.auth.models import AbstractUser, User
# from django.utils.html import escape, mark_safe
# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_emp = models.BooleanField(default=False)
    is_cus = models.BooleanField(default=False)