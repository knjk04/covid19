from django.contrib import admin

from .models import Country, Source, Vaccine

# Register your models here.
admin.site.register(Vaccine)
admin.site.register(Source)
admin.site.register(Country)
