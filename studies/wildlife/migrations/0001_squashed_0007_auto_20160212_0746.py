# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 18:22
from __future__ import unicode_literals

import common.fields
from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data_import', '0001_squashed_0020_auto_20160729_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('user', common.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wildlife', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Wildlife of Our Homes user data',
                'verbose_name_plural': 'Wildlife of Our Homes user data',
            },
        ),
    ]
