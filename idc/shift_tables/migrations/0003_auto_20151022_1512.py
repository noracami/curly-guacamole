# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shift_tables', '0002_auto_20151021_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='confirm',
            field=models.ForeignKey(blank=True, related_name='shifts_confirm', null=True, to='workers.Worker'),
        ),
        migrations.AlterField(
            model_name='shift',
            name='substitute',
            field=models.ForeignKey(blank=True, related_name='shifts_substitute', null=True, to='workers.Worker'),
        ),
        migrations.AlterField(
            model_name='shift',
            name='worker',
            field=models.ForeignKey(blank=True, related_name='shifts_worker', null=True, to='workers.Worker'),
        ),
        migrations.AlterField(
            model_name='table',
            name='supervisor',
            field=models.ForeignKey(blank=True, related_name='table_supervisor', null=True, to='workers.Worker'),
        ),
        migrations.AlterField(
            model_name='table',
            name='worker',
            field=models.ForeignKey(blank=True, related_name='table_worker', null=True, to='workers.Worker'),
        ),
    ]
