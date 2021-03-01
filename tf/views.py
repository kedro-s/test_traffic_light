from django.db import IntegrityError
from django.shortcuts import render
from .services.test_data import TestDataService
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

# Create your views here.

class Tf:
    def index(request):
        tds = TestDataService()
        users = tds.get_users()
        for user in users:
            address = Address()
            address.city = user['address']['city']
            address.street = user['address']['street']
            address.suite = user['address']['suite']
            address.zipcode = user['address']['zipcode']
            address.geo_lat = user['address']['geo']['lat']
            address.geo_lng = user['address']['geo']['lng']
            company = Company()
            company.name = user['company']['name']
            company.catchPhrase = user['company']['catchPhrase']
            company.bs = user['company']['bs']
            try:
                address = address.save()
            except IntegrityError:
                pass
            try:
                company.save()
            except IntegrityError:
                pass
            u = User()
            u.name = user['name']
            u.username = user['username']
            u.email = user['email']
            u.phone = user['phone']
            u.website = user['website']
            u.address = address.id
            u.company = company.id
            u.save()


        return render(request, 'index.html')

