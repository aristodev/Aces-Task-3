# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-10 08:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PST', '0003_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=150)),
                ('idQuestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PST.question')),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PST.user')),
            ],
        ),
    ]
