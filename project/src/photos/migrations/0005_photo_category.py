# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20161016_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='category',
            field=models.CharField(blank='True', choices=[('life', 'Life'), ('nature', 'Nature'), ('culture', 'Culture'), ('science', 'Sciense'), ('space', 'Space'), ('news', 'News'), ('humor', 'Humor')], max_length=2),
        ),
    ]