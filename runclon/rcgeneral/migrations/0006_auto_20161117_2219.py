# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-17 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rcgeneral', '0005_auto_20161117_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='registered_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
