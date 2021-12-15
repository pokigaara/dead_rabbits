from django.dispatch import receiver
from .models import *
from django.db.models.signals import post_save
from reservation.views import send_telegram, detailview
from .serializers import *
import json


@receiver(post_save, sender=Reserv)
def post_save_reserv(created, **kwargs):
    instance = kwargs['instance']
    if created:
        temp ="""
        имя: {name}
        номер: {phone}
        дата: {date}
        время: {time}
        количество человек: {people}
        """
        send_telegram(temp.format(**detailview()))
        print(f'бронь стола {instance}', detailview())
    else:
        print(f'бронь подтверждена {instance}')



