# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 21:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0001_initial'),
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='regno',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='grpid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Game.GroupDetails'),
        ),
    ]
