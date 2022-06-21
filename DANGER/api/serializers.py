from rest_framework.serializers import ModelSerializer
from .models import Danger

class DangerSerializer(ModelSerializer):
    class Meta:
        model = Danger
        fields = '__all__'