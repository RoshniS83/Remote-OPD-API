from rest_framework import serializers
from .models import EyeCamp

class EyeCampSerializer(serializers.ModelSerializer):
    class Meta:
        model=EyeCamp
        fields= '__all__'