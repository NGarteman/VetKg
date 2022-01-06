from rest_framework import serializers
from .models import Service, Price


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['id', 'title', 'price_service']


class ServiceDetailSerializer(serializers.ModelSerializer):
    service = PriceSerializer(many=True)

    class Meta:
        model = Service
        fields = ['id', 'title', 'body', 'image', 'service']

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ['id', 'title', 'body', 'image']


