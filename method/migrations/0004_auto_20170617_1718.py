# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 17:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('method', '0003_auto_20170617_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='methodinusemodel',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='method.MethodInUseModel'),
        ),
    ]
