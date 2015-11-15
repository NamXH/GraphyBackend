# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('first_name', models.CharField(max_length=255, null=True, blank=True)),
                ('middle_name', models.CharField(max_length=255, null=True, blank=True)),
                ('last_name', models.CharField(max_length=255, null=True, blank=True)),
                ('organization', models.CharField(max_length=255, null=True, blank=True)),
                ('image_name', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
    ]
