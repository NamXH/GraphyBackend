import pytz
from datetime import datetime
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest.models import PhoneNumber
from rest.serializers import PhoneNumberSerializer

class PhoneNumberList(generics.ListCreateAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer

class PhoneNumberDetail(APIView):
    def get_object(self, pk):
        try:
            return PhoneNumber.objects.get(pk=pk)
        except PhoneNumber.DoesNotExist:
            return None

    def get(self, request, pk):
        phone_number = self.get_object(pk)
        if phone_number is not None:
            serializer = PhoneNumberSerializer(phone_number)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        if 'Id' in request.data and request.data['Id'] != pk:
            return Response("Id is not the same as primary key in url!", status=status.HTTP_400_BAD_REQUEST) # Check this since serializer.save() always save the record using pk as identifier.

        server_phone_number = self.get_object(pk)

        if server_phone_number is not None:
            serializer = PhoneNumberSerializer(server_phone_number, data=request.data)

            if serializer.is_valid():
                client_phone_number = PhoneNumber(**serializer.validated_data)

                if client_phone_number.LastModified is not None and client_phone_number.LastModified > server_phone_number.LastModified:
                    if server_phone_number.IsDeleted:
                        return Response(status=status.HTTP_410_GONE)
                    else:
                        serializer.save()
                        return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    server_serializer = PhoneNumberSerializer(server_phone_number)
                    return Response(server_serializer.data, status=status.HTTP_409_CONFLICT)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_410_GONE)

    def delete(self, request, pk):
        if 'HTTP_IF_UNMODIFIED_SINCE' not in request.META:
            return Response("Delete request requires If-Unmodified-since header!", status=status.HTTP_400_BAD_REQUEST)

        server_phone_number = self.get_object(pk)

        if server_phone_number is not None:
            if_unmodified_since_datetime = datetime.strptime(request.META['HTTP_IF_UNMODIFIED_SINCE'], '%a, %d %b %Y %H:%M:%S %Z')
            client_last_modified = if_unmodified_since_datetime.replace(tzinfo=pytz.UTC)

            if client_last_modified > server_phone_number.LastModified:
                if server_phone_number.IsDeleted:
                    return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    server_phone_number.IsDeleted = True
                    server_phone_number.save()
                    return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                server_serializer = PhoneNumberSerializer(server_phone_number)
                return Response(server_serializer.data, status=status.HTTP_409_CONFLICT)
        else:
            return Response(status=status.HTTP_410_GONE)