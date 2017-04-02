# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 11:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camps', '0020_camp_read_only'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0004_team_sub_team_of'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('camp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camps.Camp')),
                ('responsible', models.ManyToManyField(related_name='responsible_team_areas', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='team',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='user',
        ),
        migrations.AddField(
            model_name='team',
            name='membersnew',
            field=models.ManyToManyField(related_name='teams', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='team',
            name='members',
        ),
        migrations.RemoveField(
            model_name='team',
            name='sub_team_of',
        ),
        migrations.AddField(
            model_name='team',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='teams', to='teams.TeamArea'),
        ),
        migrations.AlterUniqueTogether(
            name='team',
            unique_together=set([('name', 'camp'), ('slug', 'camp')]),
        ),
        migrations.DeleteModel(
            name='TeamMember',
        ),
        migrations.AlterUniqueTogether(
            name='teamarea',
            unique_together=set([('name', 'camp')]),
        ),
    ]
