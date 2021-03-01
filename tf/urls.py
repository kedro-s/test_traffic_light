from django.conf.urls import url
from django.urls import path
from .views import Tf

urlpatterns = [
    url(r'^$', Tf.index, name='index'),
    url(r'^get_data/', Tf.get_data, name='get_data'),
    url(r'^drop_data/', Tf.drop_data, name='drop_data'),
]