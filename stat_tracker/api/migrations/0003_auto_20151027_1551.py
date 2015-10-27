# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20151027_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='units',
            field=models.CharField(default='units', max_length=15),
        ),
    ]
