# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 18:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20161018_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaies', to='photos.Photo'),
        ),
    ]
