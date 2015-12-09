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
        fields = ('Id', 'Name', 'LastModified', 'IsDeleted')

class RelationshipTypeSerializer(serializers.ModelSerializer):
    Id = serializers.UUIDField()
    class Meta:
        model = RelationshipType
        fields = ('Id', 'Name', 'LastModified', 'IsDeleted')

class ContactTagMapSerializer(serializers.ModelSerializer):
    Id = serializers.UUIDField()
    class Meta:
        model = ContactTagMap
        fields = ('Id', 'Detail', 'ContactId', 'TagId', 'LastModified', 'IsDeleted')

class RelationshipSerializer(serializers.ModelSerializer):
    Id = serializers.UUIDField()
    class Meta:
        model = Relationship
        fields = ('Id', 'Detail', 'FromContactId', 'ToContactId', 'RelationshipTypeId', 'LastModified', 'IsDeleted')

class PhoneNumberSerializer(serializers.ModelSerializer):
    Id = serializers.UUIDField()
    class Meta:
        model = PhoneNumber
        fields = ('Id', 'Type', 'Number', 'ContactId', 'LastModified', 'IsDeleted')

class AddressSerializer(serializers.ModelSerializer):
    Id = serializers.UUIDField()
    class Meta:
        model = Address
        fields = ('Id', 'Type', 'StreetLine1', 'StreetLine2', 'City', 'Province', 'PostalCode', 'Country', 'ContactId', 'LastModified', 'IsDeleted')

class UrlSerializer(serializers.ModelSerializer):
    Id = serializers.UUIDField()
    class Meta:
        model = Url
        fields = ('Id', 'Type', 'Link', 'LastModified', 'IsDeleted')

class EmailSerializer(serializers.ModelSerializer):
    Id = serializers.UUIDField()
    class Meta:
        model = Email
        fields = ('Id', 'Type', 'Address', 'ContactId', 'LastModified', 'IsDeleted')

class SpecialDateSerializer(serializers.ModelSerializer):
    Id = serializers.UUIDField()
    class Meta:
        model = SpecialDate
        fields = ('Id', 'Type', 'Date', 'ContactId', 'LastModified', 'IsDeleted')

class InstantMessageSerializer(serializers.ModelSerializer):
    Id = serializers.UUIDField()
    class Meta:
        model = InstantMessage
        fields = ('Id', 'Type', 'Nickname', 'ContactId', 'LastModified', 'IsDeleted')