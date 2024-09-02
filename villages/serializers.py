from rest_framework import serializers
from .models import Villages

class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Villages
        fields = '__all__'