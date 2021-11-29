from django.db import models


class Categories(models.Model):
    categories = models.CharField(max_length=50, verbose_name='категория')

    def __str__(self):
        return self.categories



class Menu(models.Model):
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='назване блюда')
    weight = models.CharField(max_length=20, verbose_name='вес блюда')
    description = models.TextField(max_length=1000, verbose_name='описание')
    price = models.CharField(max_length=10, verbose_name='цена')
    photo = models.ImageField(verbose_name='фото', upload_to='menu.static')

    class Meta:
        verbose_name_plural = 'Меню'
        verbose_name = 'Меню'

    def __str__(self):
        return self.name


class PreOrder(models.Model):
    pass

