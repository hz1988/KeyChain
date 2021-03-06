# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-24 03:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=20)),
                ('psw', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=200)),
                ('phone_num', models.CharField(max_length=20)),
                ('remarks', models.CharField(max_length=500)),
                ('regdate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
                ('sex', models.CharField(max_length=2)),
                ('birthday', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='chain',
            name='user_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psw.UserInfo'),
        ),
    ]
