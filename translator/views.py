# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Word

def index(request):
    return render_to_response('translator/base.html')

def translate(request):

    inTamazight = request.GET.get('mot', None); # Returns None if 'awal' not found

    if inTamazight: # Checks if the input field #mot has a value
        try: # do query for the synonyms
            inArabic = Word.objects.get(word_tamazight=inTamazight).word_arabic
            inFrench = Word.objects.get(word_tamazight=inTamazight).word_french

            data = {
                'inArabic': inArabic,
                'inFrench' : inFrench
            }

            return JsonResponse(data);
        except Word.DoesNotExist:
            return JsonResponse({});

    else:
        return HttpResponse()
