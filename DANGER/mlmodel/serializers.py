from rest_framework.serializers import ModelSerializer
from .models import Mlmodel

class MlmodelSerializer(ModelSerializer):
    class Meta:
        model = Mlmodel
        fields = '__all__'

