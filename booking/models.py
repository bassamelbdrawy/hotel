from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime

class user_information(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    orderNumber = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.user_id} -{self.orderNumber}"


class hotels(models.Model):
    name = models.CharField(max_length=64)
    loc = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    desc = models.TextField()
    pic = models.ImageField(upload_to='upload_images')
    lat = models.CharField(max_length=64 , null = True)
    longtude = models.CharField(max_length=64 , null=True)

    def __str__(self):
        return f"{self.name}"

class units(models.Model):
    name = models.CharField(max_length=64)
    pic = models.ImageField(upload_to='upload_images')
    desc = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    hotel_id = models.ForeignKey(hotels, on_delete=models.CASCADE)
    numUnits = models.IntegerField()
    emptyUnit = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.hotel_id} - {self.price}"

class reviews(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel_id = models.ForeignKey(hotels, on_delete=models.CASCADE)
    comment = models.TextField(null = False)
    rate = models.IntegerField(null = False)

    def __str__(self):
        return f"{self.comment} - {self.rate}"

class books(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    unit_id = models.ForeignKey(units, on_delete=models.CASCADE)
    from_date = models.DateField(default = datetime.datetime.now())
    to_date = models.DateField(default = datetime.datetime.now())
    num_of_days = models.CharField(max_length=64)
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2)
    order_num = models.CharField(max_length=64)
    is_paid = models.BooleanField(default = False) 

    def __str__(self):
        return f"{self.unit_id} - {self.num_of_days} - {self.price_per_unit}"


class orders(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=64)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    is_paid = models.BooleanField(default = True) 

    def __str__(self):
        return f"{self.order_number} - {self.total_price}" 