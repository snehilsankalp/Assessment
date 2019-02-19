from django.contrib import admin
from .models import DoctorsDb
from .models import Appointment

admin.site.register(DoctorsDb)
admin.site.register(Appointment)
# Register your models here.
