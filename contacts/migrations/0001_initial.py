# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Text')),
                ('email', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Email')),
                ('address', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Address')),
                ('use', models.BooleanField(default=False, verbose_name='In use')),
            ],
            options={
                'verbose_name': 'Мої контакти',
                'verbose_name_plural': 'Мої контакти',
            },
        ),
    ]