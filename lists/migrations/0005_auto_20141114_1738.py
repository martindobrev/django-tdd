# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20141114_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='list',
            name='list',
        ),
    ]
