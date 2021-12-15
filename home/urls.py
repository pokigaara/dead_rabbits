from rest_framework.routers import SimpleRouter
from home.views import *

app_name = 'home'

router = SimpleRouter()


router.register('home', HomeView)
router.register('photo', PhotoView)


urlpatterns = router.urls