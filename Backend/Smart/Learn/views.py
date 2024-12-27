from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Subjects
from .serializers import SubjectSerializer

# Create your views here.
@api_view(['GET'])
def Subjectspage(request):
    data = Subjects.objects.all()
    serializers = SubjectSerializer(data, many=True)
    return Response(serializers.data)
    

@api_view(['POST'])
def Subjectsget(request,pk):
    serializers = SubjectSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return Response(serializers.errors)        