import pytz
from datetime import datetime
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest.models import SpecialDate
from rest.serializers import SpecialDateSerializer

class SpecialDateList(generics.ListCreateAPIView):
    queryset = SpecialDate.objects.all()
    serializer_class = SpecialDateSerializer

class SpecialDateDetail(APIView):
    def get_object(self, pk):
        try:
            return SpecialDate.objects.get(pk=pk)
        except SpecialDate.DoesNotExist:
            return None

    def get(self, request, pk):
        special_date = self.get_object(pk)
        if special_date is not None:
            serializer = SpecialDateSerializer(special_date)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        if 'Id' in request.data and request.data['Id'] != pk:
            return Response("Id is not the same as primary key in url!", status=status.HTTP_400_BAD_REQUEST) # Check this since serializer.save() always save the record using pk as identifier.

        server_special_date = self.get_object(pk)

        if server_special_date is not None:
            serializer = SpecialDateSerializer(server_special_date, data=request.data)

            if serializer.is_valid():
                client_special_date = SpecialDate(**serializer.validated_data)

                if client_special_date.LastModified is not None and client_special_date.LastModified > server_special_date.LastModified:
                    if server_special_date.IsDeleted:
                        return Response(status=status.HTTP_410_GONE)
                    else:
                        serializer.save()
                        return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    server_serializer = SpecialDateSerializer(server_special_date)
                    return Response(server_serializer.data, status=status.HTTP_409_CONFLICT)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_410_GONE)

    def delete(self, request, pk):
        if 'HTTP_IF_UNMODIFIED_SINCE' not in request.META:
            return Response("Delete request requires If-Unmodified-since header!", status=status.HTTP_400_BAD_REQUEST)

        server_special_date = self.get_object(pk)

        if server_special_date is not None:
            if_unmodified_since_datetime = datetime.strptime(request.META['HTTP_IF_UNMODIFIED_SINCE'], '%a, %d %b %Y %H:%M:%S %Z')
            client_last_modified = if_unmodified_since_datetime.replace(tzinfo=pytz.UTC)

            if client_last_modified > server_special_date.LastModified:
                if server_special_date.IsDeleted:
                    return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    server_special_date.IsDeleted = True
                    server_special_date.save()
                    return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                server_serializer = SpecialDateSerializer(server_special_date)
                return Response(server_serializer.data, status=status.HTTP_409_CONFLICT)
        else:
            return Response(status=status.HTTP_410_GONE)