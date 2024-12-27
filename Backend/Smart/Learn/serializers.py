from rest_framework.serializers import ModelSerializer
from .models import Subjects

class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'