from django.dispatch import receiver
from .models import *
from django.db.models.signals import post_save
@receiver(post_save, sender=Reserv)
def post_save_reserv(created, **kwargs):
    instance = kwargs['instance']
    if created:
        print(f'бронь стола {instance}')
    else:
        print(f'бронь подтверждена {instance}')

