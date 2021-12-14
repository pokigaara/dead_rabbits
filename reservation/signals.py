from django.dispatch import receiver
from .models import *
from django.db.models.signals import post_save
from reservation.views import send_telegram, DetailView


@receiver(post_save, sender=Reserv)
def post_save_reserv(created, **kwargs):
    instance = kwargs['instance']
    if created:
        send_telegram(DetailView())
        print(f'бронь стола {instance}')
    else:
        print(f'бронь подтверждена {instance}')

inf = DetailView()
print(inf)
