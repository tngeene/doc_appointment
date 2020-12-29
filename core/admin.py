from django.contrib import admin

from .models import Appointment, Event, Service

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Event)
admin.site.register(Service)
