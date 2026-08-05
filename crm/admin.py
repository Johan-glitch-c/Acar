from django.contrib import admin
from .models import Order, Cms, Service
# Register your models here.
admin.site.register(Order)
admin.site.register(Cms)
admin.site.register(Service)