# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('method', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='methodinusemodel',
            name='text',
            field=models.CharField(max_length=200, verbose_name='Text'),
        ),
    ]