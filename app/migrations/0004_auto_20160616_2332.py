# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160611_0235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promo',
            old_name='html',
            new_name='html_en',
        ),
        migrations.AddField(
            model_name='promo',
            name='html_ru',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
