from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Topics
from .serializers import TopicSerializer

@api_view(['GET'])
def Topicspage(request, tpk):
    try:
        data = Topics.objects.filter(cid=tpk)
        if not data.exists():
            return Response({"error": "No topics found for this chapter."}, status=404)
        serializers = TopicSerializer(data, many=True)
        return Response(serializers.data)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['POST'])
def Topicsget(request):
    serializers = TopicSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=201)
    return Response(serializers.errors, status=400)
