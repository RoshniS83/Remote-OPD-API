from rest_framework import serializers
from Patient.models import Patientopdform

class PatientSerializer(serializers.ModelSerializer):
          class Meta:
                    model = Patientopdform
                    fields = '__all__'

class PatientHistorySerializer(serializers.ModelSerializer):
          class Meta:
                    model = Patientopdform
                    fields = ['patientName', 'date', 'category', 'diagnosis']