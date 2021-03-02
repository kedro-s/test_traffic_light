from django.db import IntegrityError
from django.shortcuts import render, redirect
from .services.test_data import TestDataService
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *


# Create your views here.


def index(request):
    res = Post.objects.select_related().values('user__name', 'title', 'body')
    return render(request, 'index.html', {'posts': res})


def get_data(request):
    tds = TestDataService()
    tds.load_data()
    return redirect('/')


def drop_data(request):
    tds = TestDataService()
    tds.drop_data()
    return redirect('/')
