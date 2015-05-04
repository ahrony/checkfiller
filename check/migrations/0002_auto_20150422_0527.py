# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkdetails',
            name='total_ammount',
            field=models.DecimalField(verbose_name=b'TK', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
    ]
