from django.db import models
from django.contrib.auth.models import AbstractUser, User
# from django.utils.html import escape, mark_safe
# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_emp = models.BooleanField(default=False)
    is_cus = models.BooleanField(default=False)

class ShopProfile(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE)
    shopname = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.shopname