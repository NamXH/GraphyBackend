import pytz
from datetime import datetime
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest.models import Email
from rest.serializers import EmailSerializer

class EmailList(generics.ListCreateAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

class EmailDetail(APIView):
    def get_object(self, pk):
        try:
            return Email.objects.get(pk=pk)
        except Email.DoesNotExist:
            return None

    def get(self, request, pk):
        email = self.get_object(pk)
        if email is not None:
            serializer = EmailSerializer(email)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        if 'Id' in request.data and request.data['Id'] != pk:
            return Response("Id is not the same as primary key in url!", status=status.HTTP_400_BAD_REQUEST) # Check this since serializer.save() always save the record using pk as identifier.

        server_email = self.get_object(pk)

        if server_email is not None:
            serializer = EmailSerializer(server_email, data=request.data)

            if serializer.is_valid():
                client_email = Email(**serializer.validated_data)

                if client_email.LastModified is not None and client_email.LastModified > server_email.LastModified:
                    if server_email.IsDeleted:
                        return Response(status=status.HTTP_410_GONE)
                    else:
                        serializer.save()
                        return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    server_serializer = EmailSerializer(server_email)
                    return Response(server_serializer.data, status=status.HTTP_409_CONFLICT)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_410_GONE)

    def delete(self, request, pk):
        if 'HTTP_IF_UNMODIFIED_SINCE' not in request.META:
            return Response("Delete request requires If-Unmodified-since header!", status=status.HTTP_400_BAD_REQUEST)

        server_email = self.get_object(pk)

        if server_email is not None:
            if_unmodified_since_datetime = datetime.strptime(request.META['HTTP_IF_UNMODIFIED_SINCE'], '%a, %d %b %Y %H:%M:%S %Z')
            client_last_modified = if_unmodified_since_datetime.replace(tzinfo=pytz.UTC)

            if client_last_modified > server_email.LastModified:
                if server_email.IsDeleted:
                    return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    server_email.IsDeleted = True
                    server_email.save()
                    return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                server_serializer = EmailSerializer(server_email)
                return Response(server_serializer.data, status=status.HTTP_409_CONFLICT)
        else:
            return Response(status=status.HTTP_410_GONE)