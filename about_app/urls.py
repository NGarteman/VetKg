from django.urls import path
from .views import RecordsApiView

app_name = "about_app"

urlpatterns = [
    path('about_us/', RecordsApiView.as_view())
]


# from .views import RecordViewSet
# from rest_framework.routers import DefaultRouter
#
#
# router = DefaultRouter()
# router.register(r"records", RecordViewSet, basename='records')
# urlpatterns = router.urls
