# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samacore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
