# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0036_auto_20150506_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='keypair',
            name='phone_number',
            field=models.CharField(null=True, blank=True, default='', max_length=20),
            preserve_default=True,
        ),
    ]
