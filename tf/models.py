from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=False)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, unique=True)
    address = models.ForeignKey(
        'Address',
        related_name='users',
        on_delete=models.RESTRICT,
        blank=False
    )
    company = models.ForeignKey(
        'Company',
        related_name='users',
        on_delete=models.RESTRICT,
        blank=False
    )
    website = models.CharField(max_length=255, blank=False)


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(
        'User',
        related_name='posts',
        on_delete=models.CASCADE,
        blank=False
    )
    title = models.CharField(max_length=255, blank=False)
    body = models.TextField(blank=False)


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=255, blank=False)
    street = models.CharField(max_length=255, blank=False)
    suite = models.CharField(max_length=255, blank=False)
    zipcode = models.CharField(max_length=255, blank=False)
    geo_lat = models.CharField(max_length=50, blank=False)
    geo_lng = models.CharField(max_length=50, blank=False)

    class Meta:
        unique_together = (('city', 'street', 'suite'),)


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, null=True)
    catchPhrase = models.CharField(max_length=255, blank=False)
    bs = models.CharField(max_length=255, blank=False)
