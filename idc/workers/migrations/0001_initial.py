# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=40, verbose_name='姓名')),
                ('password', models.CharField(max_length=40, blank=True, verbose_name='密碼')),
                ('email', models.EmailField(max_length=254, blank=True, verbose_name='Email')),
                ('account', models.CharField(max_length=40, blank=True, verbose_name='帳號')),
            ],
            options={
                'verbose_name': '人員',
            },
        ),
    ]
