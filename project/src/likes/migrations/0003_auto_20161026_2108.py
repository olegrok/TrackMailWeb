# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 21:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0002_auto_20161016_1638'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'verbose_name': 'Like', 'verbose_name_plural': 'Likes'},
        ),
    ]