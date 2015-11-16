# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_auto_20151116_0603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='First_name',
            new_name='FirstName',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='image_name',
            new_name='ImageName',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='last_name',
            new_name='LastName',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='middle_name',
            new_name='MiddleName',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='organization',
            new_name='Organization',
        ),
    ]
