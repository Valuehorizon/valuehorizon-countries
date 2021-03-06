# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-07 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0006_auto_20160607_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='symbol_alpha3_code',
            field=models.CharField(default='AAA', help_text=b'ISO 3166-1 alpha-3 symbol', max_length=3, unique=True),
            preserve_default=False,
        ),
    ]
