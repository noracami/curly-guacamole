# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shift_tables', '0003_auto_20151022_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='date',
            field=models.DateField(verbose_name='日期', default=django.utils.timezone.now),
        ),
    ]
