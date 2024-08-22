from django.db import models
from authentication.models import *
from customer.models import *

# Create your models here.
class Category(models.Model):
    cname=models.TextField(max_length=100,null=True)
    cimage=models.ImageField(upload_to='category',null=True)

    def __str__(self):
        return self.cname

class Product(models.Model):
    product_name=models.TextField(max_length=100,null=True)
    price=models.FloatField(null=True)
    discription=models.TextField(max_length=400,null=True)
    image=models.ImageField(upload_to='products',null=True)
    restaurant=models.ForeignKey(Seller,on_delete=models.CASCADE,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.product_name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(default=1)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def restaurant_name(self):
        rest_name=self.product.restaurant.hname
        return rest_name
    def __str__(self):
        return f"{self.product.restaurant.hname}"
    
    

    
    
