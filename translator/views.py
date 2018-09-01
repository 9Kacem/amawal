# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse

# COMBAK: from .models import Question

def index(request):
    if request.method == 'GET' and 's' in request.GET:
        myString = request.GET['s']
        return render_to_response('translator/index.html')
        # TODO: Render data to AJAX
    else: return render_to_response('translator/index.html')
