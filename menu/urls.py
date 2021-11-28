from django.urls import path, include
from menu.views import *
from rest_framework.routers import SimpleRouter


app_name = 'menu'

router = SimpleRouter()

router.register('dish', MenuView)
router.register('Cate', CetegorView)

urlpatterns = router.urls

# MenuViewurlpatterns = [
#     path('view', MenuView.as_view()),
#     # path('create/', MenuCreate.as_view()),
#     # path('all/', MenuListView.as_view()),
#     # path('delet/<int:pk>/', MenuDetailView.as_view()),
#     # path('update/<int:pk>/', MenuUpdateView.as_view()),
# ]
