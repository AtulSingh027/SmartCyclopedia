from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Chapters

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapters
        fields = '__all__'