# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ("records", "0014_user"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]
