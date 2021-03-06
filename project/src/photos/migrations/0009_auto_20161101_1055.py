# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 10:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('photos', '0008_auto_20161101_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='categ',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='categories.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.CharField(blank='True', choices=[('Life', 'life'), ('Nature', 'nature'), ('Culture', 'culture'), ('Science', 'science'), ('Space', 'space'), ('News', 'news'), ('Humor', 'humor'), ('Information Technology', 'IT')], max_length=1024, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
    ]
