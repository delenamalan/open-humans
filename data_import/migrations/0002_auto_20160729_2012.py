# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 20:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_import', '0001_squashed_0020_auto_20160729_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datafile',
            name='task',
        ),
        migrations.RemoveField(
            model_name='dataretrievaltask',
            name='user',
        ),
        migrations.DeleteModel(
            name='DataRetrievalTask',
        ),
    ]
