from django.urls import path
from .views import *
from . import views
app_name = 'shop'
urlpatterns = [
    path('', ShopHome.as_view(), name = 'ShopHome'),
    # path('logout/', UserLogoutView.as_view(), name='UserLogoutView'),
    # path('TestView/', TestView.as_view(), name='TestView'),

]