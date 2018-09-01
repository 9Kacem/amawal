# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Word(models.Model):
    meaning_tamazight = models.CharField(max_length=200)
    meaning_arabic = models.CharField(max_length=200)
    added_at = models.DateTimeField('date added')
