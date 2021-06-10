from django import forms
from .models import ordermodel
from django.utils.translation import ugettext_lazy as _

class addorderform(forms.ModelForm):
    class Meta:
        model = ordermodel
        fields = ('customer_id','product_id','unit_price','qty','total_price')
        