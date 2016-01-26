# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0007_auto_20151128_0642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('Type', models.CharField(max_length=255, null=True, blank=True)),
                ('StreetLine1', models.CharField(max_length=255, null=True, blank=True)),
                ('StreetLine2', models.CharField(max_length=255, null=True, blank=True)),
                ('City', models.CharField(max_length=255, null=True, blank=True)),
                ('Province', models.CharField(max_length=255, null=True, blank=True)),
                ('PostalCode', models.CharField(max_length=255, null=True, blank=True)),
                ('Country', models.CharField(max_length=255, null=True, blank=True)),
                ('LastModified', models.DateTimeField(null=True, blank=True)),
                ('IsDeleted', models.BooleanField(default=False)),
                ('ContactId', models.ForeignKey(blank=True, to='rest.Contact', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactTagMap',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('Detail', models.CharField(max_length=255, null=True, blank=True)),
                ('LastModified', models.DateTimeField(null=True, blank=True)),
                ('IsDeleted', models.BooleanField(default=False)),
                ('ContactId', models.ForeignKey(blank=True, to='rest.Contact', null=True)),
                ('TagId', models.ForeignKey(blank=True, to='rest.Tag', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('Type', models.CharField(max_length=255, null=True, blank=True)),
                ('Address', models.CharField(max_length=255, null=True, blank=True)),
                ('LastModified', models.DateTimeField(null=True, blank=True)),
                ('IsDeleted', models.BooleanField(default=False)),
                ('ContactId', models.ForeignKey(blank=True, to='rest.Contact', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstantMessage',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('Type', models.CharField(max_length=255, null=True, blank=True)),
                ('Nickname', models.CharField(max_length=255, null=True, blank=True)),
                ('LastModified', models.DateTimeField(null=True, blank=True)),
                ('IsDeleted', models.BooleanField(default=False)),
                ('ContactId', models.ForeignKey(blank=True, to='rest.Contact', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('Type', models.CharField(max_length=255, null=True, blank=True)),
                ('Number', models.CharField(max_length=255, null=True, blank=True)),
                ('LastModified', models.DateTimeField(null=True, blank=True)),
                ('IsDeleted', models.BooleanField(default=False)),
                ('ContactId', models.ForeignKey(blank=True, to='rest.Contact', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('Detail', models.CharField(max_length=255, null=True, blank=True)),
                ('LastModified', models.DateTimeField(null=True, blank=True)),
                ('IsDeleted', models.BooleanField(default=False)),
                ('FromContactId', models.ForeignKey(related_name='from_contact', blank=True, to='rest.Contact', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RelationshipType',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=255, null=True, blank=True)),
                ('LastModified', models.DateTimeField(null=True, blank=True)),
                ('IsDeleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialDate',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('Type', models.CharField(max_length=255, null=True, blank=True)),
                ('Date', models.DateField(null=True, blank=True)),
                ('LastModified', models.DateTimeField(null=True, blank=True)),
                ('IsDeleted', models.BooleanField(default=False)),
                ('ContactId', models.ForeignKey(blank=True, to='rest.Contact', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('Type', models.CharField(max_length=255, null=True, blank=True)),
                ('Link', models.CharField(max_length=255, null=True, blank=True)),
                ('LastModified', models.DateTimeField(null=True, blank=True)),
                ('IsDeleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='relationship',
            name='RelationshipTypeId',
            field=models.ForeignKey(blank=True, to='rest.RelationshipType', null=True),
        ),
        migrations.AddField(
            model_name='relationship',
            name='ToContactId',
            field=models.ForeignKey(related_name='to_contact', blank=True, to='rest.Contact', null=True),
        ),
    ]
