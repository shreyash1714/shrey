from typing import OrderedDict
from django.contrib import admin
from .models import ordermodel
# Register your models here.

class ordermodeladmin(admin.ModelAdmin):
    list_display=['id','customer_id','product_id']


admin.site.register(ordermodel,ordermodeladmin)