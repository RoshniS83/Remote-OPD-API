from rest_framework import serializers
from .models import HBCamp

class HBCampSerializer(serializers.ModelSerializer):
    class Meta:
        model=HBCamp
        fields= '__all__'