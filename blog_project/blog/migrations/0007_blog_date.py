# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 17:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170416_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
