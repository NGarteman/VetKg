from rest_framework import viewsets
from .models import Service
from .serializers import ServiceSerializer, ServiceDetailSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ServiceViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Service.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ServiceSerializer
        return ServiceDetailSerializer



