# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('memorization', '0003_auto_20171129_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='chinesesentence',
            name='lesson',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]