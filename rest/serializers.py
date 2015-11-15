from rest_framework import serializers
from rest.models import Contact #Tag, PhoneNumber, Email

class ContactSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()

    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'organization', 'image_name')
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