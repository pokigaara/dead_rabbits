from django.db import models


class Reserv(models.Model):
    name = models.CharField(max_length=30, verbose_name='имя')
    surname = models.CharField(max_length=50, verbose_name='фамилия')
    phone = models.CharField(max_length=13, verbose_name='телефон')
    email = models.EmailField(verbose_name='почта')
    date = models.DateField(verbose_name='дата')
    time = models.TimeField(verbose_name='время')
    people = models.IntegerField(verbose_name='количество человек')
    table = models.IntegerField(verbose_name='номер стола', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'брони'
        verbose_name = 'бронь'

    def __str__(self):
        return self.name
