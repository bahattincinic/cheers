# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 20:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0004_remove_topic_show_home'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ('id',)},
        ),
    ]