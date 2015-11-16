from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest.serializers import *

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDetail(APIView):
    def get_object(self, pk):
        try:
            return Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        contact = self.get_object(pk)
        if contact is not None:
            serializer = ContactSerializer(contact)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # def put(self, request, pk, format=None):
