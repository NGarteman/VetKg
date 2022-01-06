from rest_framework import viewsets
from .models import Advice
from .serializers import AdviceSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class AdviceViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer