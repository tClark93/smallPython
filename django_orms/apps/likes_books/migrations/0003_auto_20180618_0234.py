# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-18 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes_books', '0002_auto_20180616_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='desc',
            field=models.CharField(max_length=25),
        ),
    ]
