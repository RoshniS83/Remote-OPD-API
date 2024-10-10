from rest_framework import serializers
from .models import ADCamp

class ADCampSerializer(serializers.ModelSerializer):
    class Meta:
        model=ADCamp
        fields= '__all__'