from rest_framework import serializers
from rest.models import *

class ContactSerializer(serializers.ModelSerializer):
    Id = serializers.UUIDField()
    class Meta:
        model = Contact
        fields = ('Id', 'FirstName', 'MiddleName', 'LastName', 'Organization', 'ImageName', 'LastModified', 'IsDeleted')

class TagSerializer(serializers.ModelSerializer):
    Id = serializers.UUIDField()
    class Meta:
        model = Tag
        fields = ('Id', 'Name', 'IsDeleted', 'LastModified')
#
# class PhoneNumberSerializer(serializers.ModelSerializer):
#         Id = serializers.UUIDField()
#     class Meta:
#         model = PhoneNumber
#         fields = ('id', 'type', 'number')
#
# class EmailSerializer(serializers.ModelSerializer):
#         Id = serializers.UUIDField()
#     class Meta:
#         model = Email
#         fields = ('id', 'type', 'street_line_1')