# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20161107_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/default-avatar.jpg', upload_to='avatars', verbose_name='\u0444\u043e\u0442\u043e \u043f\u0440\u043e\u0444\u0438\u043b\u044f'),
        ),
    ]