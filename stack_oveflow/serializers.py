from rest_framework.serializers import ModelSerializer
from rest_framework import  serializers
from .models import User, Questions, Answer

class UserSerializer(ModelSerializer):
    
    