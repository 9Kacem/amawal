# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Word

def index(request):
    return render_to_response('translator/index.html')

def translate(request):

    inTamazight = request.GET.get('awal', None); # Returns None if 'awal' not found

    if inTamazight: # Checks if the input field has a value
        try: # Make query for the arabic synonyme
            inArabic = Word.objects.get(word_tamazight=inTamazight).word_arabic
            # TODO: query for french synonyme too

            data = {
                'inArabic': inArabic
                # TODO: 'inFrench' : inFrench
            }

            return JsonResponse(data)
        except Word.DoesNotExist:

            data = {
                'inArabic': "Word does not exist"
            }

            return JsonResponse(data)
            
    else:
        return render_to_response('translator/index.html')
