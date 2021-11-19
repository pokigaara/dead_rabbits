from django.db import models


class Menu(models.Model):
    Categories = (
        (1, 'Супы'),
        (2, 'Салаты'),
        (3, 'Основные'),
        (4, 'Закуски'),
        (5, 'Десерты'),

    )
    categories = models.IntegerField(verbose_name='категория', choices=Categories)
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
