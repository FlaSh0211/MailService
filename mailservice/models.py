from django.db import models

# Create your models here.

class Order(models.Model):
    company = models.CharField(max_length=100) 
    product_name = models.CharField(max_length=100)  
    count = models.IntegerField()
    emails = models.CharField(max_length=100)



