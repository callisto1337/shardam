from django.db import models

from landing.models import Address


class Reservation(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    guests = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'бронирование'
        verbose_name_plural = 'Бронирования'

    def __str__(self):
        return self.name +  ': ' + self.phone
