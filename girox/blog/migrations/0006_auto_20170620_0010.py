# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-20 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posted',
            field=models.DateField(auto_now=True, db_index=True, verbose_name='data'),
        ),
    ]
