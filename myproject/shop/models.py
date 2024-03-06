from django.db import models
from account.models import *

# Create your models here.




class PickupRequest(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    shopname = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    shop_address = models.TextField()
    status = models.PositiveIntegerField(default=1)
    rider_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.shopname

class PickupItems(models.Model):
    pickup = models.ForeignKey(PickupRequest, on_delete=models.CASCADE)
    shop_usr = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    invoice_amount = models.PositiveBigIntegerField(default=0)
    deli_charge = models.PositiveBigIntegerField(default=0)
    status = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_name

