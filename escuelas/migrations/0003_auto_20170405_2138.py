# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 03:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0002_auto_20170315_0049'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='administrativos',
            options={'verbose_name': 'Administrativo', 'verbose_name_plural': 'Administrativos'},
        ),
        migrations.AlterModelOptions(
            name='estudiantes',
            options={'verbose_name': 'Estudiante', 'verbose_name_plural': 'Estudiantes'},
        ),
    ]