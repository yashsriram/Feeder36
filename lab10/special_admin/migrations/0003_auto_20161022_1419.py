# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-22 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('special_admin', '0002_auto_20161022_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='user_name',
            field=models.EmailField(max_length=30),
        ),
    ]