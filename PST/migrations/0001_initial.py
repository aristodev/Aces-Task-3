# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-10 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
            ],
        ),
    ]
