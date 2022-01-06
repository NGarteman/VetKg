from .views import ContactViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"contacts", ContactViewSet, basename='vets')
urlpatterns = router.urls