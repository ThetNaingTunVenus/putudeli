from django.contrib import admin
from .models import User
from .models import *
# Register your models here.

class ShopProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'usr', 'shopname')
admin.site.register(ShopProfile,ShopProfileAdmin)


admin.site.register(User)