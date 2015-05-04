# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0003_auto_20150422_0539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkdetails',
            name='ammount_in_word',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
