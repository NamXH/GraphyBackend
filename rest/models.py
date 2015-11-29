import uuid
from django.db import models


class Contact(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    FirstName = models.CharField(max_length=255, null=True, blank=True)
    MiddleName = models.CharField(max_length=255, null=True, blank=True)
    LastName = models.CharField(max_length=255, null=True, blank=True)
    Organization = models.CharField(max_length=255, null=True, blank=True)
    ImageName = models.CharField(max_length=255, null=True, blank=True)
    LastModified = models.DateTimeField(null=True, blank=True)
    IsDeleted = models.BooleanField(default=False)
    # Simplify: don't use Birthday, Favorite; every char field can be null.
    # Use camel case to be compatible out of the box for C# client (instead of converting names).


class Tag(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    Name = models.CharField(max_length=255, null=True, blank=True)
    LastModified = models.DateTimeField(null=True, blank=True)
    IsDeleted = models.BooleanField(default=False)


# class RelationshipType(models.Model):
#     Id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     Name = models.CharField(max_length=255, null=True, blank=True)
#     LastModified = models.DateTimeField(null=True, blank=True)
#     IsDeleted = models.BooleanField(default=False)
#
#
# class ContactTagMap(models.Model):
#     Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     Detail = models.CharField(max_length=255, null=True, blank=True)
#     ContactId = models.ForeignKey(Contact, null=True, blank=True)
#     TagId = models.ForeignKey(Tag, null=True, blank=True)
#     LastModified = models.DateTimeField(null=True, blank=True)
#     IsDeleted = models.BooleanField(default=False)
#
#
# class Relationship(models.Model):
#     Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     Detail = models.CharField(max_length=255, null=True, blank=True)
#     FromContactId = models.ForeignKey(Contact, null=True, blank=True)
#     ToContactId = models.ForeignKey(Contact, null=True, blank=True)
#     RelationshipTypeId = models.ForeignKey(RelationshipType, null=True, blank=True)
#     LastModified = models.DateTimeField(null=True, blank=True)
#     IsDeleted = models.BooleanField(default=False)
#
#
# class PhoneNumber(models.Model):
#     Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     Type = models.CharField(max_length=255, null=True, blank=True)
#     Number = models.CharField(max_length=255, null=True, blank=True)
#     ContactId = models.ForeignKey(Contact, null=True, blank=True)
#     LastModified = models.DateTimeField(null=True, blank=True)
#     IsDeleted = models.BooleanField(default=False)
#
#
# class Address(models.Model):
#     Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     Type = models.CharField(max_length=255, null=True, blank=True)
#     StreetLine1 = models.CharField(max_length=255, null=True, blank=True)
#     StreetLine2 = models.CharField(max_length=255, null=True, blank=True)
#     City = models.CharField(max_length=255, null=True, blank=True)
#     Province = models.CharField(max_length=255, null=True, blank=True)
#     PostalCode = models.CharField(max_length=255, null=True, blank=True)
#     Country = models.CharField(max_length=255, null=True, blank=True)
#     ContactId = models.ForeignKey(Contact, null=True, blank=True)
#     LastModified = models.DateTimeField(null=True, blank=True)
#     IsDeleted = models.BooleanField(default=False)
#
#
# class Url(models.Model):
#     Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     Type = models.CharField(max_length=255, null=True, blank=True)
#     Link = models.CharField(max_length=255, null=True, blank=True)
#     LastModified = models.DateTimeField(null=True, blank=True)
#     IsDeleted = models.BooleanField(default=False)
#
#
# class Email(models.Model):
#     Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     Type = models.CharField(max_length=255, null=True, blank=True)
#     Address = models.CharField(max_length=255, null=True, blank=True)
#     ContactId = models.ForeignKey(Contact, null=True, blank=True)
#     LastModified = models.DateTimeField(null=True, blank=True)
#     IsDeleted = models.BooleanField(default=False)
#
#
# class SpecialDate(models.Model):
#     Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     Type = models.CharField(max_length=255, null=True, blank=True)
#     Date = models.DateField(null=True, blank=True)
#     ContactId = models.ForeignKey(Contact, null=True, blank=True)
#     LastModified = models.DateTimeField(null=True, blank=True)
#     IsDeleted = models.BooleanField(default=False)
#
#
# class InstantMessage(models.Model):
#     Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     Type = models.CharField(max_length=255, null=True, blank=True)
#     Nickname = models.CharField(max_length=255, null=True, blank=True)
#     ContactId = models.ForeignKey(Contact, null=True, blank=True)
#     LastModified = models.DateTimeField(null=True, blank=True)
#     IsDeleted = models.BooleanField(default=False)