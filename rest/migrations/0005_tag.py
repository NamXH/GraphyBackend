# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0004_auto_20151116_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('Name', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
    ]
