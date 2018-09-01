# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Word

def index(request):
    return render_to_response('translator/index.html')

def translate(request):
    try:
        # COMBAK: inTamazight = request.GET['s']

        inTamazight = request.GET.get('s', None)
        inArabic = Word.objects.get(word_tamazight=inTamazight).word_arabic
        
        data = {
            'inArabic': inArabic
        }

        return JsonResponse(data)

    except Word.DoesNotExist:
        return HttpResponse("Word does not exist")
