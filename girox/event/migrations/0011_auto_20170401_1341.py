# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import girox.event.validators


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_auto_20170331_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='cpf',
            field=models.CharField(db_index=True, help_text='(Necessário para o seguro)', max_length=11, validators=[girox.event.validators.validate_cpf], verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='date_of_birth',
            field=models.DateField(help_text='(Necessário para o seguro)', verbose_name='data nascimento'),
        ),
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together=set([('cpf', 'event'), ('rg', 'event')]),
        ),
    ]