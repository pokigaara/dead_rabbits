from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=50, verbose_name='назване мероприятия')
    description = models.TextField(max_length=1000, verbose_name='описание')
    data = models.DateField(verbose_name='дата мероприятия')
    time = models.TimeField(verbose_name='время мероприятия')
    photo = models.ImageField(verbose_name='фото')

    class Meta:
        verbose_name_plural = 'Мероприятия'
        verbose_name = 'Мероприятие'


    def __str__(self):
        return self.name

