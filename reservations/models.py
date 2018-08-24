from django.db import models

from landing.models import Address


class Reservation(models.Model):
    name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    guests = models.IntegerField(null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'бронирование'
        verbose_name_plural = 'Бронирования'

    def __str__(self):
        return f'{self.name}: {self.phone}'
