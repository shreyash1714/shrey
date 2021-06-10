from django.db import models

# Create your models here.


class productmodel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    unit_price=models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return str(self.id)
