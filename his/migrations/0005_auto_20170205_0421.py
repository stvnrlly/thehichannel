# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 04:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('his', '0004_auto_20170205_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hi',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
