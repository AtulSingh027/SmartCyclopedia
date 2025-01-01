from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Chapters
from .serializers import ChapterSerializer
# Create your views here.
@api_view(['GET'])
def Chapterspage(request, cpk=None):
    if cpk:
        data = Chapters.objects.filter(sid=cpk).all()
    else:
        data = Chapters.objects.all()  # Return all chapters if no cpk
    serializers = ChapterSerializer(data, many=True)
    return Response(serializers.data)


@api_view(['POST'])    
def Chaptersget(request):
    # data = request.data
    serializers = ChapterSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return Response(serializers.errors)

# Create your views here.
