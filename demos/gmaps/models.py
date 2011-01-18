from django.db import models
from django.contrib import admin

from gmapsfield.fields import GoogleMapsField

class GMap(models.Model):
    map_field = GoogleMapsField()

class GMapAdmin(admin.ModelAdmin): pass

try:
    admin.site.register(GMap, GMapAdmin)
except: pass
