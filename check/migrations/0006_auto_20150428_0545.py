# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0005_auto_20150426_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkdetails',
            name='ammount_in_word',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='checkdetails',
            name='date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='checkdetails',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Pay To', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='checkdetails',
            name='signature',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='checkdetails',
            name='total_ammount',
            field=models.DecimalField(null=True, verbose_name=b'TK', max_digits=10, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
