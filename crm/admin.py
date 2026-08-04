from django.contrib import admin
from .models import OrderStatus, Order, Cms
# Register your models here.
admin.site.register(OrderStatus)
admin.site.register(Order)
admin.site.register(Cms)