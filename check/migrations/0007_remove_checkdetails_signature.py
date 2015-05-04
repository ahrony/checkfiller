# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0006_auto_20150428_0545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkdetails',
            name='signature',
        ),
    ]
