# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0039_appconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='appconfig',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 8, 8, 1, 59, 54, 374539)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appconfig',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2023, 8, 8, 2, 0, 0, 297024)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appconfig',
            name='global_pin',
            field=models.TextField(null=True, db_index=True, default='', blank=True),
            preserve_default=True,
        ),
    ]
