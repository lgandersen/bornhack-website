# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-17 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
        ('shop', '0047_auto_20170522_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ticket_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.TicketType'),
        ),
    ]
