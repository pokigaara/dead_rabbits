from django.urls import path, include
from activity.views import *

app_name = 'activity'
urlpatterns = [
    path('create/', ActivityCreate.as_view()),
    path('all/', ActivityListView.as_view()),
    path('delet/<int:pk>/', ActivityDetailView.as_view()),
    path('update/<int:pk>/', ActivityUpdateView.as_view()),
]
