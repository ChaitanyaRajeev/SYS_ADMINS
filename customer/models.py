# from django.db import models

# # Create your models here.
from django.db import models

# Creating our model class - Customer_Info

class Customer_Info(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    

    def __str__(self):
        return (self.name + ', ' +  self.address + ', ' +  self.city + ', ' +  self.state + ', ' + self.country)