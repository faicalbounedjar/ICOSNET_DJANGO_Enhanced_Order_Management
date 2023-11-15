from django.db import models
from django.contrib.auth.models import User
# the status for each order
class Status(models.TextChoices):
    Pending= 'Pending'
    Processing= 'Processing'
    Shipped='Shipped'
    Delivered='Delivered'
# order class
class Order(models.Model):
    # the id is assigned by default and auto incrementing
    # title will be unique
    title = models.CharField(max_length=255,unique=True,blank=False)
    name = models.CharField(max_length=255,blank=False)
    description = models.TextField(max_length=255,blank=False)
    price = models.DecimalField(max_digits=7,decimal_places=2,default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255,choices=Status.choices,default='Pending')
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    timestamp =  models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return f"{self.title}-{self.name}-{self.description}-{self.price}-{self.createdAt}:{self.status}"