# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0004_auto_20150422_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkdetails',
            name='date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='checkdetails',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Pay To'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='checkdetails',
            name='signature',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='checkdetails',
            name='total_ammount',
            field=models.DecimalField(null=True, verbose_name=b'TK', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
    ]
