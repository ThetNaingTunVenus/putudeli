from django.urls import path
from .views import *
from . import views
app_name = 'account'
urlpatterns = [
    # path('login', UserLoginView.as_view(), name = 'UserLoginView'),
    # path('logout/', UserLogoutView.as_view(), name='UserLogoutView'),
    path('TestView/', TestView.as_view(), name='TestView'),

]