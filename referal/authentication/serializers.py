#from rest_framework import serializers
from itsdangerous import Serializer
from .models import authentication
 
 
class PhoneSerializer(Serializer.ModelSerializer):
    class Meta:
        model = authentication
        fields = ('phone')