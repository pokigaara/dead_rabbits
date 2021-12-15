from django.db import models



class Photo(models.Model):
    photo = models.ImageField(verbose_name='фото')

    class Meta:
        verbose_name_plural = 'Фотографии'
        verbose_name = 'Фотография'



class Home(models.Model):
    name = models.CharField(max_length=50, verbose_name='назване')
    phone = models.CharField(max_length=13, verbose_name='телефон')
    descrp = models.TextField(verbose_name='описание')
    mail = models.EmailField(verbose_name='почта')


