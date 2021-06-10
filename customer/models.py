from django.db import models

# Create your models here.

class customermodel(models.Model):
    id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=25)
    lastname=models.CharField(max_length=25)
    contactno=models.CharField(max_length=15)
    pincode=models.IntegerField()

    def __str__(self):
        return str(self.id)