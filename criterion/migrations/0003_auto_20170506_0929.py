# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criterion', '0002_auto_20170506_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criterion',
            name='priority',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
