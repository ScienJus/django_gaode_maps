from django.db.models import Model
from django_gaode_maps.fields import *

class Example(Model):
    address = AddressField(max_length=100)
    location = LocationField(max_length=100)
    city = CityField(max_length=100)
    postal_code = PostalCodeField(max_length=10)
