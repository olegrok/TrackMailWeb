# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 10:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0011_auto_20161101_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='categ',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='categories.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
    ]
