# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 11:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Surname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AddedDate', models.DateField(default=datetime.datetime(2017, 1, 6, 11, 25, 33, 185223, tzinfo=utc))),
                ('Genre', models.CharField(max_length=100)),
                ('Label', models.CharField(max_length=100)),
                ('NPrints', models.PositiveSmallIntegerField()),
                ('Publisher', models.CharField(max_length=150)),
                ('TimesBorrowed', models.PositiveIntegerField()),
                ('Title', models.CharField(max_length=200)),
                ('Status', models.CharField(max_length=10)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GfLib.Author')),
            ],
        ),
    ]
