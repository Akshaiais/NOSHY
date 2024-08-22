from django.db import models

# Create your models here.

class Customer(models.Model):
    fname=models.TextField(max_length=100,db_column='first name',null=True)
    lname=models.TextField(max_length=100,null=True)
    address=models.TextField(max_length=500,null=True)
    email=models.TextField(max_length=100,null=True)
    mobile=models.BigIntegerField(null=True)
    password=models.TextField(max_length=100,null=True)

    def __str__(self):
        return self.fname

class Seller(models.Model):
    hname=models.TextField(max_length=100,db_column='first name',null=True)
    address=models.TextField(max_length=100,null=True)
    image=models.ImageField(upload_to='restaurant',null=True)
    email=models.TextField(max_length=100,null=True)
    mobile=models.BigIntegerField(null=True)
    password=models.TextField(max_length=100,null=True)

    def __str__(self):
        return self.hname