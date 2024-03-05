import datetime

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.models import AnonymousUser
from django.db.models import Sum,Count,F
from django.http import HttpResponse
from django.views.generic import TemplateView, View, CreateView, DetailView,FormView

from .forms import *
from .models import *
from shop.views import *
# Create your views here.

class TestView(View):
    def get(self, request):
        return render(request, 'base.html')

# user login
class UserLoginView(FormView):
    template_name = 'login.html'
    form_class = ULoginForm
    success_url = reverse_lazy('account:TestView')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data['password']
        usr = authenticate(username=username, password=password)

        if usr is not None:
            if usr.is_admin:
                login(self.request, usr)
            if usr.is_emp:
                return HttpResponse('this user is Emp')
            if usr.is_cus:
                return redirect('shop:ShopHome')
            
        else:
            return render(self.request, self.template_name, {'form': self.form_class, 'error': 'Invalid user login!'})
        return super().form_valid(form)

class UserLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('account:UserLoginView')