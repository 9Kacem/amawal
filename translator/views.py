# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response

# COMBAK: from .models import Question

def index(request):
    return render_to_response('translator/index.html')
