# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 06:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '0001_initial'),
        ('lugares', '0001_initial'),
        ('programas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Participantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idGrupoRef', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='gruposI', to='sesiones.Grupo', verbose_name='Grupo')),
                ('idPersonaRef', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='personasI', to='personas.Persona', verbose_name='Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('fecha', models.DateField(default=datetime.date.today, verbose_name='Fecha')),
                ('inicio', models.TimeField(default=datetime.date.today, verbose_name='Hora de inicio')),
                ('fin', models.TimeField(default=datetime.date.today, verbose_name='Hora de fin')),
                ('lugar', models.CharField(max_length=100, verbose_name='Nombre del lugar')),
                ('direccion', models.TextField(blank=True, null=True, verbose_name='Direccion')),
                ('latitud', models.DecimalField(blank=True, decimal_places=10, editable=False, max_digits=30, null=True, verbose_name='Latitud')),
                ('longitud', models.DecimalField(blank=True, decimal_places=10, editable=False, max_digits=30, null=True, verbose_name='Longitud')),
                ('idDistritoRef', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lugares.Distrito', verbose_name='Distrito')),
                ('idPeriodoRef', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='programas.Periodo', verbose_name='Periodo')),
            ],
        ),
        migrations.CreateModel(
            name='TipoParticipante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
            ],
        ),
        migrations.AddField(
            model_name='participantes',
            name='idTipoParticipanteRef',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sesiones.TipoParticipante', verbose_name='Tipo de participante'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='idSesionRef',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sesiones.Sesion', verbose_name='Grupo'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='participantes',
            field=models.ManyToManyField(related_name='participantes', through='sesiones.Participantes', to='personas.Persona'),
        ),
    ]
