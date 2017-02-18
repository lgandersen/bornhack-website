# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camps', '0019_auto_20170131_1849'),
        ('program', '0020_auto_20170205_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlocation',
            name='icon',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='eventlocation',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='eventlocation',
            unique_together=set([('camp', 'slug'), ('camp', 'name')]),
        ),
    ]