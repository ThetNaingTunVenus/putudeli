from django.urls import path
from .views import *
from . import views
app_name = 'shop'
urlpatterns = [
    path('', ShopHome.as_view(), name = 'ShopHome'),
    path('PickupRequestView/', PickupRequestView.as_view(), name='PickupRequestView'),
    # path('TestView/', TestView.as_view(), name='TestView'),
    path('create/', PickupCreate.as_view(), name='create_product'),
    path('update/<int:pk>/', PickupUpdate.as_view(), name='update_product'),
    path('delete-variant/<int:pk>/', delete_variant, name='delete_variant'),

]