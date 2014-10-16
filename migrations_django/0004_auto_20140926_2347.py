# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140924_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeholder',
            name='slot',
            field=models.CharField(verbose_name='slot', max_length=255, editable=False, db_index=True),
        ),
    ]
