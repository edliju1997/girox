# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 20:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_auto_20170331_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event', verbose_name='evento'),
        ),
    ]