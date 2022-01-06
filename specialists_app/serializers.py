from rest_framework import serializers
from .models import Vet


class VetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vet
        fields = ['id',
                  'first_name',
                  'last_name',
                  'surname',
                  'speciality',
                  'education',
                  'image',
                  'experience',
                  'contacts'
                  ]
