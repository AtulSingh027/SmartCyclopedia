from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Topics

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = '__all__'