# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memorization', '0005_remove_chinesesentence_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='chinesesentence',
            name='lesson',
            field=models.IntegerField(default=int(0)),
        ),
    ]
