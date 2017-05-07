# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-07 23:34
from __future__ import unicode_literals

from django.db import migrations, models
import girox.gallery.models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20170424_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='file_height',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='file_width',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=versatileimagefield.fields.VersatileImageField(height_field='file_height', upload_to=girox.gallery.models.album_directory_path, verbose_name='arquivo', width_field='file_width'),
        ),
    ]