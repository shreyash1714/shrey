from django.contrib import admin
from .models import customermodel
# Register your models here.


class customermodeladmin(admin.ModelAdmin):
    list_display=['id','firstname','lastname']



admin.site.register(customermodel,customermodeladmin)