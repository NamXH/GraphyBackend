from datetime import datetime
import pytz

from django.utils import timezone

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
                        serializer.save()
                        return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    server_serializer = ContactSerializer(server_contact)
                    return Response(server_serializer.data, status=status.HTTP_409_CONFLICT)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_410_GONE)

    def delete(self, request, pk):
        server_contact = self.get_object(pk)

        if server_contact is not None:
            if_unmodified_since_datetime = datetime.strptime(request.META['HTTP_IF_UNMODIFIED_SINCE'], '%a, %d %b %Y %H:%M:%S %Z')
            client_last_modified = if_unmodified_since_datetime.replace(tzinfo=pytz.UTC)

            if client_last_modified > server_contact.LastModified:
                if server_contact.IsDeleted:
                    return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    server_contact.IsDeleted = True
                    server_contact.save()
                    return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                server_serializer = ContactSerializer(server_contact)
                return Response(server_serializer.data, status=status.HTTP_409_CONFLICT)
        else:
            return Response(status=status.HTTP_410_GONE)