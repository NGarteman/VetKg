from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import views
from .models import Record
from .serializers import RecordSerializer

class RecordsApiView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = RecordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

