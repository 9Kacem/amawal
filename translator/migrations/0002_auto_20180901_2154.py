# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-01 21:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='meaning_arabic',
            new_name='word_arabic',
        ),
        migrations.RenameField(
            model_name='word',
            old_name='meaning_tamazight',
            new_name='word_tamazight',
        ),
    ]
