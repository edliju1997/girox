# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-08 01:52
from __future__ import unicode_literals

from django.db import migrations
import girox.gallery.models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_auto_20170507_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='file_height',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='file_width',
        ),
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=versatileimagefield.fields.VersatileImageField(upload_to=girox.gallery.models.album_directory_path, verbose_name='arquivo'),
        ),
    ]
