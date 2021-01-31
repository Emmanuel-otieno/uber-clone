from django.contrib import admin
from .models import Location,Driver,Car  
# Register your models here.
admin.site.register(Car)
admin.site.register(Driver)
admin.site.register(Location)
# admin.site.register(Category)
# admin.site.register(Passenger)