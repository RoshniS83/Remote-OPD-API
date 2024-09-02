
from rest_framework import serializers
from .models import Medicines

class MedicineSerializer (serializers.ModelSerializer):
    class Meta:
        model= Medicines
        fields = '__all__'