# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-07 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0004_auto_20150528_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='is_independent',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='numeric_code',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='remark_1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='country',
            name='remark_2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='country',
            name='remark_3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='country',
            name='territory_name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(help_text=b'Official Country name (ISO Full name)', max_length=255, unique=True),
        ),
    ]
