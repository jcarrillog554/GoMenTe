# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 05:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0003_auto_20170315_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
