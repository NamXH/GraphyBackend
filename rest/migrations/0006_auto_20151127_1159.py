# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0005_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='IsDeleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tag',
            name='LastModified',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
