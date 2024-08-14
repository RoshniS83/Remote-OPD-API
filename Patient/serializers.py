from rest_framework import serializers
from Patient.models import Patientopdform

class PatientSerializer(serializers.ModelSerializer):
          class Meta:
                    model = Patientopdform
                    fields = '__all__'
