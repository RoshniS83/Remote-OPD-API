from rest_framework import serializers
from Client.models import Client

class ClientSerializer(serializers.ModelSerializer):
          class Meta:
                    model = Client
                    fields = '__all__'
