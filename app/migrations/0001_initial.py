# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-12 07:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='Browse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attitude', models.IntegerField()),
            ],
            options={
                'db_table': 'browse',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=80)),
                ('time', models.DateTimeField()),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'note',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=4)),
                ('signature', models.CharField(max_length=80)),
                ('url', models.FileField(upload_to='pubheader')),
                ('url1', models.FileField(upload_to='hero1')),
                ('url2', models.FileField(upload_to='hero2')),
                ('url3', models.FileField(upload_to='hero3')),
            ],
            options={
                'db_table': 'publisher',
            },
        ),
        migrations.AddField(
            model_name='note',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Publisher'),
        ),
        migrations.AddField(
            model_name='browse',
            name='note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Note'),
        ),
        migrations.AddField(
            model_name='browse',
            name='reader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Publisher'),
        ),
    ]
