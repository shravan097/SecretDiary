# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 22:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170415_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='blog',
        ),
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.UserProfile'),
        ),
    ]
