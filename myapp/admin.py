from django.contrib import admin
from . models import OrderInfo,OrderItem
# Register your models here.
admin.site.register(OrderInfo)
admin.site.register(OrderItem)
