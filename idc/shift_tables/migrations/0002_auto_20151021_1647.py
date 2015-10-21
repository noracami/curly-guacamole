# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
        ('shift_tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateField(verbose_name='日期')),
                ('supervisor', models.ForeignKey(related_name='table_supervisor', to='workers.Worker')),
                ('worker', models.ForeignKey(related_name='table_worker', to='workers.Worker')),
            ],
            options={
                'verbose_name': '每月輪值表',
            },
        ),
        migrations.AlterModelOptions(
            name='shift',
            options={'verbose_name': '班'},
        ),
    ]
