# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_auto_20150527_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='iso_status',
            field=models.CharField(default=b'UND', max_length=3, choices=[('OFF', 'Officially assigned'), ('INR', 'Indeterminately reserved'), ('EXR', 'Exceptionally reserved'), ('TRR', 'Transitionally reserved'), ('FRU', 'Formerly used'), ('UND', 'Unassigned')]),
        ),
        migrations.AddField(
            model_name='country',
            name='symbol_alpha3_code',
            field=models.CharField(help_text=b'ISO 3166-1 alpha-3 symbol', max_length=3, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='symbol_alpha2_code',
            field=models.CharField(help_text=b'ISO 3166-1 alpha-2 symbol', unique=True, max_length=2),
        ),
    ]
