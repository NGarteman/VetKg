from rest_framework import serializers
from .models import Record


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['id', 'name', 'phone_number', 'region', 'accept']

