# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 10:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_report_vikor_results'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='vikor_results',
            new_name='vikor_result',
        ),
    ]
