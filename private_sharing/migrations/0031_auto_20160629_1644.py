# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('private_sharing', '0030_datarequestproject_returned_data_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onsitedatarequestproject',
            name='post_sharing_url',
            field=models.URLField(blank=True, help_text='If provided, after authorizing sharing the\nmember will be taken to this URL. If this URL includes "PROJECT_MEMBER_ID"\nwithin it, we will replace that with the member\'s project-specific\nproject_member_id. This allows you to direct them to an external survey you\noperate (e.g. using Google Forms) where a pre-filled project_member_id field\nallows you to connect those responses to corresponding data in Open Humans.', verbose_name='Post-sharing URL'),
        ),
    ]
