from django.urls import path
from .views import oindex,addorder
urlpatterns = [
    path('oindex/',oindex,name='oindex'),
    path('addorder',addorder,name='addorder')
]
