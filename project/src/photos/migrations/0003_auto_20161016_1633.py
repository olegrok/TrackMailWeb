# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20161016_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
