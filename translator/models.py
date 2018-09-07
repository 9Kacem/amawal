# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Word(models.Model):
    word_tamazight = models.CharField(max_length=200)
    word_arabic = models.CharField(max_length=200)
    word_french = models.CharField(max_length=200)
    added_at = models.DateTimeField('date added')

    def __str__(self):
        return self.word_tamazight
