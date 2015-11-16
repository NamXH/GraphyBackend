from rest_framework import serializers

from rest.models import *

class ContactSerializer(serializers.ModelSerializer):
    Id = serializers.UUIDField()

    class Meta:
        model = Contact
        fields = ('Id', 'FirstName', 'MiddleName', 'LastName', 'Organization', 'ImageName', 'LastModified', 'IsDeleted')
#
# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = ('id', 'name')
#
# class PhoneNumberSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PhoneNumber
#         fields = ('id', 'type', 'number')
#
# class EmailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Email
#         fields = ('id', 'type', 'street_line_1')