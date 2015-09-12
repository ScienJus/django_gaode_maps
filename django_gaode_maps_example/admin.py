from django.contrib import admin
from .models import Example
from django_gaode_maps.widgets import LocationWidget
from django_gaode_maps.fields import LocationField

@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    fields = ["address", "city", "postal_code", "location"]

    formfield_overrides = {
        LocationField: {'widget': LocationWidget},
    }