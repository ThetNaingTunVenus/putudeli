from django.contrib import admin
from .models import *
# Register your models here.

class PickupRequestAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'shopname')
admin.site.register(PickupRequest,PickupRequestAdmin)


class PickupItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'phone')
admin.site.register(PickupItems,PickupItemsAdmin)
