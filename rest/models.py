import uuid
from django.db import models

class Contact(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    FirstName = models.CharField(max_length=255, null=True, blank=True)
    MiddleName = models.CharField(max_length=255, null=True, blank=True)
    LastName = models.CharField(max_length=255, null=True, blank=True)
    Organization = models.CharField(max_length=255, null=True, blank=True)
    ImageName = models.CharField(max_length=255, null=True, blank=True)
    LastModified = models.DateTimeField(null=True, blank=True)
    IsDeleted = models.BooleanField(default=False)
    # Simplify: don't use Birthday, Favorite, every char field can be null.
    # Use camel case to be compatible out of the box for C# client (instead of converting names).

# class Tag(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     name = models.CharField(max_length=255, null=True, blank=True)
#
# class ContactTagMap(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     detail = models.CharField(max_length=255, null=True, blank=True)
#     contact_id = models.ForeignKey(Contact, null=True, blank=True)
#     tag_id = models.ForeignKey(Tag, null=True, blank=True)
#
# class PhoneNumber(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     type = models.CharField(max_length=255, null=True, blank=True)
#     number = models.CharField(max_length=255, null=True, blank=True)
#     contact_id = models.ForeignKey(Contact, null=True, blank=True)
#
# class Address(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     type = models.CharField(max_length=255, null=True, blank=True)
#     street_line_1 = models.CharField(max_length=255, null=True, blank=True)
#     street_line_2 = models.CharField(max_length=255, null=True, blank=True)
#     city = models.CharField(max_length=255, null=True, blank=True)
#     province = models.CharField(max_length=255, null=True, blank=True)
#     postal_code = models.CharField(max_length=255, null=True, blank=True)
#     country = models.CharField(max_length=255, null=True, blank=True)
#     contact_id = models.ForeignKey(Contact, null=True, blank=True)
