# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubiome', '0003_ubiomesample'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ubiomesample',
            name='sample_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]