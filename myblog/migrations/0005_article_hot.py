# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-14 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_auto_20180314_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='hot',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
