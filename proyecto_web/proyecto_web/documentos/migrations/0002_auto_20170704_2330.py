# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-04 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documento',
            name='edad',
        ),
        migrations.AddField(
            model_name='documento',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
