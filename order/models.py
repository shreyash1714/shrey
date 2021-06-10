from django.db import models
from product.models import productmodel
from customer.models import customermodel


# Create your models here.

class ordermodel(models.Model):
    id=models.AutoField(primary_key=True)
    customer_id=models.ForeignKey(customermodel,on_delete=models.CASCADE)
    product_id=models.ForeignKey(productmodel,on_delete=models.CASCADE)
    unit_price=models.DecimalField(max_digits=6,decimal_places=2)
    qty=models.IntegerField()
    total_price=models.DecimalField(max_digits=6,decimal_places=2)
    created_date=models.DateTimeField(auto_now_add=True)
