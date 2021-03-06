# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 09:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_auto_20161018_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to=settings.AUTH_USER_MODEL, verbose_name='\u0410\u0432\u0442\u043e\u0440'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.CharField(blank='True', choices=[('Life', 'life'), ('Nature', 'nature'), ('Culture', 'culture'), ('Sciense', 'science'), ('Space', 'space'), ('News', 'news'), ('Humor', 'humor'), ('Information Technology', 'IT')], max_length=1024, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, max_length=1024, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='photos/', verbose_name='\u0424\u043e\u0442\u043e\u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438'),
        ),
    ]
