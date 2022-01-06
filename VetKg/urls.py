from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('specialists_app.urls')),
    path('', include('contacts_app.urls')),
    path('', include('news_app.urls')),
    path('', include('about_app.urls')),
    path('', include('services_app.urls')),
    path('', include('advices_app.urls')),
    # path('', include('auth_app.urls')),
]
