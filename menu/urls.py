from django.urls import path, include
from menu.views import *

app_name = 'menu'
urlpatterns = [
    path('create/', MenuCreate.as_view()),
    path('all/', MenuListView.as_view()),
]
