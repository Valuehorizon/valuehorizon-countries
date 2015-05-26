# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0008_auto_20150526_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('symbol', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('in_name', models.CharField(help_text=b"The name of the country after the word 'in'. Usefule for Autogeneration.", max_length=255)),
                ('symbol', models.CharField(help_text=b'ISO 3166-1 alpha-2 symbol', unique=True, max_length=3)),
                ('currency', models.ManyToManyField(help_text=b'Official currencies for this country. More than one currency is possible', to='forex.Currency')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Government',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('country', models.ForeignKey(to='countries.Country')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Government',
                'verbose_name_plural': 'Governments',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('symbol', models.CharField(max_length=4)),
                ('country', models.ManyToManyField(to='countries.Country')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(to='countries.Country'),
        ),
        migrations.AlterUniqueTogether(
            name='government',
            unique_together=set([('name', 'country')]),
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together=set([('name', 'country')]),
        ),
    ]
