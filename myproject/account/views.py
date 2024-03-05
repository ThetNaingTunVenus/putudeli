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
# Create your views here.

class TestView(View):
    def get(self, request):
        return render(request, 'datatable.html')