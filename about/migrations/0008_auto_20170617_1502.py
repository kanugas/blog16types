# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_iusecategorymodel_iusemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300, verbose_name='Category name')),
                ('use', models.BooleanField(default=False, verbose_name='In use')),
            ],
            options={
                'verbose_name_plural': 'Я використовую категорії',
                'verbose_name': 'Я використовую категорію',
            },
        ),
        migrations.AlterModelOptions(
            name='aboutmemodel',
            options={'verbose_name': 'Про мене', 'verbose_name_plural': 'Про мене'},
        ),
        migrations.AlterModelOptions(
            name='applicationprojectmodel',
            options={'verbose_name': 'Заявка на "Ознайомча лекція з практичною начинкою"', 'verbose_name_plural': 'Заявки на "Ознайомча лекція з практичною начинкою"'},
        ),
        migrations.AlterModelOptions(
            name='booksmodel',
            options={'verbose_name': 'Моя книга', 'verbose_name_plural': 'Мої книги'},
        ),
        migrations.AlterModelOptions(
            name='iusecategorymodel',
            options={'verbose_name': 'Я використовую категорію', 'verbose_name_plural': 'Я використовую категорії'},
        ),
        migrations.AlterModelOptions(
            name='iusemodel',
            options={'verbose_name': 'Я використовую', 'verbose_name_plural': 'Я використовую'},
        ),
        migrations.AlterField(
            model_name='iusemodel',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
    ]
