from tf.models import *
from django.db import IntegrityError

class SaveUsersService:
    def save_users(self, responce):
        for user in responce:
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

