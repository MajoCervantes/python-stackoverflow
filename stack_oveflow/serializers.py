from dataclasses import fields
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from rest_framework import  serializers
from .models import User, Questions, Answer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'
        depth = 1
    