from rest_framework import serializers
from .models import Megacamp

class MegacampSerializer(serializers.ModelSerializer):
	class Meta:
		model = Megacamp
		fields = '__all__'