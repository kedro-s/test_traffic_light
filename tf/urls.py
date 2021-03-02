from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^get_data/', get_data, name='get_data'),
    url(r'^drop_data/', drop_data, name='drop_data'),
]