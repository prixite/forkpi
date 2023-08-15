# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0040_auto_20230808_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appconfig',
            name='global_pin',
            field=models.TextField(default='', null=True, blank=True),
            preserve_default=True,
        ),
    ]
