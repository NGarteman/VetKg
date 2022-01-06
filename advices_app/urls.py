from .views import AdviceViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"advices", AdviceViewSet, basename='advices')
urlpatterns = router.urls