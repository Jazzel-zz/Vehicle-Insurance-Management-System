from django.contrib import admin
from . import models
from . import forms
# Register your models here.


class VehicleModelAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Vehicle


admin.site.register(models.Vehicle, VehicleModelAdmin)
