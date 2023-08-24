#from rest_framework import serializers
from itsdangerous import Serializer
from .models import authentication
 
 
class WomenSerializer(Serializer.ModelSerializer):
    class Meta:
        model = authentication
        fields = ('phone')