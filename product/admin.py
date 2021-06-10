from django.contrib import admin
from .models import productmodel
# Register your models here.

class productmodeladmin(admin.ModelAdmin):
    list_display=['id','name','unit_price']


admin.site.register(productmodel,productmodeladmin)