# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-25 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20180225_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='truck_id',
            field=models.IntegerField(default=1),
        ),
    ]
