# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='First_name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='id',
            new_name='Id',
        ),
    ]
