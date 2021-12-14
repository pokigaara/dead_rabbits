from django.shortcuts import render
from rest_framework import generics, permissions
from reservation.serializers import *
from tg_bot import config
import requests
from .models import Reserv


# Create your views here.
class ReservCreateUser(generics.CreateAPIView):
    serializer_class = ReservCreatUserSerial


class ReservUpdateAdmin(generics.RetrieveUpdateAPIView):
    serializer_class = ReservUptadeAdminSerial
    queryset = Reserv.objects.all()


def DetailView():
    return Reserv.objects.all().order_by("published").last()


def send_telegram(text):
    token = config.TOKEN
    url = "https://api.telegram.org/bot"
    channel_id = '291336121'
    url += token
    method = url + '/sendMessage'

    r = requests.post(method, data={
        'chat_id': channel_id,
        'text': text
    })

    # if r.status_code != 200:
    #     raise Exception('post_text error')


if __name__ == '__main__':
    send_telegram('hello world')
