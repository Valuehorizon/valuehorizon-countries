# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0003_auto_20150527_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='common_name',
            field=models.CharField(help_text=b'Common Country name', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='iso_status',
            field=models.CharField(default=b'UND', max_length=3, choices=[('EXR', 'Exceptionally reserved'), ('FRU', 'Formerly used'), ('INR', 'Indeterminately reserved'), ('OFF', 'Officially assigned'), ('TRR', 'Transitionally reserved'), ('UND', 'Unassigned')]),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(help_text=b'Official Country name', unique=True, max_length=255),
        ),
    ]
