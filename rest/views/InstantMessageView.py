import pytz
from datetime import datetime
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest.models import InstantMessage
from rest.serializers import InstantMessageSerializer

class InstantMessageList(generics.ListCreateAPIView):
    queryset = InstantMessage.objects.all()
    serializer_class = InstantMessageSerializer

class InstantMessageDetail(APIView):
    def get_object(self, pk):
        try:
            return InstantMessage.objects.get(pk=pk)
        except InstantMessage.DoesNotExist:
            return None

    def get(self, request, pk):
        instant_message = self.get_object(pk)
        if instant_message is not None:
            serializer = InstantMessageSerializer(instant_message)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        if 'Id' in request.data and request.data['Id'] != pk:
            return Response("Id is not the same as primary key in url!", status=status.HTTP_400_BAD_REQUEST) # Check this since serializer.save() always save the record using pk as identifier.

        server_instant_message = self.get_object(pk)

        if server_instant_message is not None:
            serializer = InstantMessageSerializer(server_instant_message, data=request.data)

            if serializer.is_valid():
                client_instant_message = InstantMessage(**serializer.validated_data)

                if client_instant_message.LastModified is not None and client_instant_message.LastModified > server_instant_message.LastModified:
                    if server_instant_message.IsDeleted:
                        return Response(status=status.HTTP_410_GONE)
                    else:
                        serializer.save()
                        return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    server_serializer = InstantMessageSerializer(server_instant_message)
                    return Response(server_serializer.data, status=status.HTTP_409_CONFLICT)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_410_GONE)

    def delete(self, request, pk):
        if 'HTTP_IF_UNMODIFIED_SINCE' not in request.META:
            return Response("Delete request requires If-Unmodified-since header!", status=status.HTTP_400_BAD_REQUEST)

        server_instant_message = self.get_object(pk)

        if server_instant_message is not None:
            if_unmodified_since_datetime = datetime.strptime(request.META['HTTP_IF_UNMODIFIED_SINCE'], '%a, %d %b %Y %H:%M:%S %Z')
            client_last_modified = if_unmodified_since_datetime.replace(tzinfo=pytz.UTC)

            if client_last_modified > server_instant_message.LastModified:
                if server_instant_message.IsDeleted:
                    return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    server_instant_message.IsDeleted = True
                    server_instant_message.save()
                    return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                server_serializer = InstantMessageSerializer(server_instant_message)
                return Response(server_serializer.data, status=status.HTTP_409_CONFLICT)
        else:
            return Response(status=status.HTTP_410_GONE)