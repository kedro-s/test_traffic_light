from django.db import IntegrityError
from django.shortcuts import render, redirect
from .services.test_data import TestDataService
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
from .services.save_users_services import SaveUsersService
from .services.save_posts_services import SavePostsService
from .services.drop_data_services import DropDataService

# Create your views here.


class Tf:
    def index(request):
        res = Post.objects.select_related().values('user__name', 'title', 'body')
        return render(request, 'index.html', {'posts': res})

    def get_data(request):
        tds = TestDataService()
        users = tds.get_users()

        sus = SaveUsersService()
        sus.save_users(users)

        posts = tds.get_posts()
        sps = SavePostsService()
        sps.save_posts(posts)

        return redirect('/')

    def drop_data(self):
        dds = DropDataService()
        dds.drop_data()

        return redirect('/')

