from django.db import models
from authentication.models import *
from seller.models import *

# Create your models here.
class Cart(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantity=models.PositiveIntegerField(default=1)