from rest_framework import serializers
from .models import Camps

class CampsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camps
        fields = '__all__'