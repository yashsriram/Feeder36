# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-30 15:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('special_admin', '0014_auto_20161029_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_set', models.TextField()),
                ('comment', models.TextField()),
                ('feedback_form', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='special_admin.FeedBackForm')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='special_admin.Student')),
            ],
        ),
    ]