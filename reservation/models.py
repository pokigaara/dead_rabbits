from django.db import models
from datetime import time
from django.db.models.signals import post_save


class Table(models.Model):
    number = models.SmallIntegerField(verbose_name='столы')


class Reserv(models.Model):
    name = models.CharField(max_length=30, verbose_name='имя')
    surname = models.CharField(max_length=30, verbose_name='фамилия')
    phone = models.CharField(max_length=13, verbose_name='телефон')
    email = models.EmailField(verbose_name='почта')
    date = models.DateField(verbose_name='дата')
    time = models.TimeField(verbose_name='время')
    time_hour = models.TimeField(editable=False, null=True, default=None)
    people = models.IntegerField(verbose_name='количество человек')
    table = models.ForeignKey(Table, verbose_name='номер стола', null=True, blank=True, on_delete=models.CASCADE)
    confirmation = models.BooleanField(default=False, null=True, blank=True, verbose_name='подтвержденеи брони')

    class Meta:
        verbose_name_plural = 'брони'
        verbose_name = 'бронь'
        unique_together = ('date', 'time_hour', 'table')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        print(self.time, type(self.time))
        self.time_hour = time(self.time.hour, 0, 0)
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name
