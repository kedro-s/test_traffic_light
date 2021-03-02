import json

import requests
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from tf.models import *


class TestDataService:
    base_url = 'http://jsonplaceholder.typicode.com/'

    def __send(self, entity):
        return json.loads(requests.get(self.base_url + entity).text)

    def get_users(self):
        return self.__send(entity='users')

    def get_posts(self):
        return self.__send(entity='posts')

    def load_users(self):
        for user in self.get_users():
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
                address = Address.objects.filter(
                    city=user['address']['city'],
                    street=user['address']['street'],
                    suite=user['address']['suite']
                ).first()
            try:
                company.save()
            except IntegrityError:
                company = Company.objects.filter(name=user['company']['name']).first()
            try:
                u = User()
                u.name = user['name']
                u.username = user['username']
                u.email = user['email']
                u.phone = user['phone']
                u.website = user['website']
                u.address = address
                u.company = company
                u.save()
            except IntegrityError:
                pass

    def load_posts(self):
        for post in self.get_posts():
            try:
                user = User.objects.get(pk=post['userId'])
                p = Post()
                p.user = user
                p.id = post['id']
                p.title = post['title']
                p.body = post['body']
                p.save()
            except ObjectDoesNotExist:
                pass

    def drop_data(self):
        Post.objects.all().delete()
        User.objects.all().delete()
        Company.objects.all().delete()
        Company.objects.all().delete()

    def load_data(self):
        self.load_users()
        self.load_posts()
