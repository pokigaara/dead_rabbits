from django.urls import path, include
from activity.views import *
from rest_framework.routers import SimpleRouter

app_name = 'activity'

router = SimpleRouter()

router.register('', ActivityView)

urlpatterns = router.urls
# urlpatterns = [
#     path('create', ActivityCreate.as_view()),
#     # path('all', BaseActivityView.as_view()),
#     # path('delet/<int:pk>', BaseActivityView.as_view()),
#     # path('update/<int:pk>', BaseActivityView.as_view()),
#     path('all', ActivityListView.as_view()),
#     path('delet/<int:pk>', ActivityDetailView.as_view()),
#     path('update/<int:pk>', ActivityUpdateView.as_view()),
# ]
