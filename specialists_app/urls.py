from .views import VetViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"vets", VetViewSet, basename='vets')
urlpatterns = router.urls