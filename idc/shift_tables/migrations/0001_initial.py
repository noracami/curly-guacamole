# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True, verbose_name='日期')),
                ('is_holiday', models.BooleanField(verbose_name='例假日')),
                ('confirm', models.ForeignKey(to='workers.Worker', related_name='shifts_confirm')),
                ('substitute', models.ForeignKey(to='workers.Worker', related_name='shifts_substitute')),
                ('worker', models.ForeignKey(to='workers.Worker', related_name='shifts_worker')),
            ],
        ),
    ]
