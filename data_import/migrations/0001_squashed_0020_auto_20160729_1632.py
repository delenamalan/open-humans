# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 18:43
from __future__ import unicode_literals

import common.fields
import data_import.utils
import datetime
from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
        ('studies', '0001_squashed_0021_auto_20160409_0642'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataRetrievalTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, b'Completed successfully'), (1, b'Submitted'), (2, b'Failed'), (3, b'Queued'), (4, b'Initiated'), (5, b'Postponed')], default=1)),
                ('start_time', models.DateTimeField(default=datetime.datetime.now)),
                ('complete_time', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('app_task_params', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='TestUserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', common.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='test_user_data', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='dataretrievaltask',
            options={'ordering': ['-start_time']},
        ),
        migrations.AlterField(
            model_name='dataretrievaltask',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='DataFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=1024, upload_to=data_import.utils.get_upload_path)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('source', models.CharField(max_length=32)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datafiles', to='data_import.DataRetrievalTask')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datafiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewDataFileAccessLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.GenericIPAddressField()),
                ('data_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_import.DataFile')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='datafile',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='datafiles', to='data_import.DataRetrievalTask'),
        ),
        migrations.AddField(
            model_name='dataretrievaltask',
            name='source',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='datafile',
            name='is_latest',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='datafile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 2, 12, 1, 55, 2, 251836, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newdatafileaccesslog',
            name='data_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='access_logs', to='data_import.DataFile'),
        ),
        migrations.AlterField(
            model_name='newdatafileaccesslog',
            name='ip_address',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
