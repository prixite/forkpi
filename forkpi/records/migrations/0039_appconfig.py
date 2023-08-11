# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0038_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('global_pin', models.TextField(null=True, default='', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
