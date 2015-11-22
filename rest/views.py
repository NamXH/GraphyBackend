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

    def get(self, request, pk):
        contact = self.get_object(pk)
        if contact is not None:
            serializer = ContactSerializer(contact)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        server_contact = self.get_object(pk)

        if server_contact is not None:
            serializer = ContactSerializer(server_contact, data=request.data)

            if serializer.is_valid():
                client_contact = Contact(**serializer.validated_data)

                if client_contact.LastModified > server_contact.LastModified:
                    if server_contact.IsDeleted:
                        return Response(status=status.HTTP_410_GONE)
                    else:
                        # serializer = ContactSerializer(contact, data=request.data)
                        # if serializer.is_valid():
                        #     serializer.save()
                        # else:
                        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        serializer.save()
                        return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    server_serializer = ContactSerializer(server_contact)
                    return Response(server_serializer.data, status=status.HTTP_409_CONFLICT)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_410_GONE)
