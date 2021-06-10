from django.urls import path
from .views import pindex
urlpatterns = [
    path('pindex/',pindex,name='pindex'),
]
