from django.db import models

class user_details(models.Model):
    username=models.CharField(max_length=8,primary_key=True)
    password=models.CharField(max_length=20,blank=False)
    firstname=models.CharField(max_length=20,blank=False)
    lastname=models.CharField(max_length=20)
    mobile=models.CharField(max_length=10)
    email=models.CharField(max_length=30,blank=False)
    address=models.CharField(max_length=20,blank=False)

class products(models.Model):
    pid=models.CharField(max_length=3,primary_key=True)
    name=models.CharField(max_length=20,blank=False)
    price=models.IntegerField(blank=False)
    category=models.CharField(max_length=20,blank=False)
    image=models.CharField(max_length=50,blank=False)

class orders(models.Model):
    username=models.CharField(max_length=8)
    order_id=models.CharField(max_length=32)
    date=models.DateField(default='2019-04-08')
    delivery_address=models.CharField(max_length=255,blank=False)
    total=models.IntegerField(blank=False)
    class Meta:
        unique_together=(("username","order_id"))

class order_details(models.Model):
    order_id=models.CharField(max_length=32)
    pid=models.CharField(max_length=3)
    name=models.CharField(max_length=20,blank=False)
    quantity=models.IntegerField(blank=False)
    price=models.IntegerField(blank=False)
    image=models.CharField(max_length=50,blank=False)
    class Meta:
        unique_together=(("order_id","pid"))
