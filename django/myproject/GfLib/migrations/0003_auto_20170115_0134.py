# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-15 00:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GfLib', '0002_auto_20170112_0009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='NPrints',
        ),
        migrations.RemoveField(
            model_name='book',
            name='TimesBorrowed',
        ),
    ]
