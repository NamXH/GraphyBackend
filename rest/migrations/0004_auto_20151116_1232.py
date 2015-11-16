# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0003_auto_20151116_0609'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='IsDeleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contact',
            name='LastModified',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
