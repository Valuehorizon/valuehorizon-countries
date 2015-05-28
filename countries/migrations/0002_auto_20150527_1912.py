# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='symbol',
            new_name='symbol_alpha2_code',
        ),
        migrations.AlterField(
            model_name='country',
            name='in_name',
            field=models.CharField(help_text=b"The name of the country after the word 'in'. Useful for Autogeneration.", max_length=255),
        ),
    ]
