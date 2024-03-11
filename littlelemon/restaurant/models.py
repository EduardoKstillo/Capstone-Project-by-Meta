from django.db import models

# Create your models here.


class Booking (models.Model):
    name = models.CharField(max_length=100)
    no_of_guests = models.IntegerField(max_length=6)
    bookingDate = models.DateTimeField(auto_now_add=True)


class Menu (models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField()
    inventory = models.IntegerField(max_length=5)
