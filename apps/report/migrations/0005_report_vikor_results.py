# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 10:41
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_report_supplier_compare'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='vikor_results',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
            preserve_default=False,
        ),
    ]