from django.urls import path, include
from reservation.views import *

app_name = 'reservation'
urlpatterns = [
    path('create', ReservCreateUser.as_view()),
    path('update/<int:pk>', ReservUpdateAdmin.as_view())
]
