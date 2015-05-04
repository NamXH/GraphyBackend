from rest_framework.views import APIView
from rest.serializers import TagSerializer
from rest_framework.response import Response
from rest.models import Tag

class TagList(APIView):
   def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)