from django.db import models

# Create your models here.


class Booking (models.Model):
    name = models.CharField(max_length=100)
    no_of_guests = models.IntegerField()
    bookingDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

    def __str__(self) -> str:
        return self.title
