# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#cacheing
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.core.cache import cache

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from django.core.serializers import serialize, deserialize

# Django model
from .models import Comment

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# Create your views here.
def home_view(request):
    return HttpResponse("Test view")

def test(request):
    return HttpResponse("test page")

def about(request):
    return HttpResponse("about page")

# RUN FASTER YOU SON OF A B... :D!
def list_all(request):
    comments = None
    if 'comments' in cache:
        ser = cache.get('comments')
        comments = deserialize("json", ser)

    else:
        comments = Comment.objects.all()
        ser = serialize("json", comments)

        cache.set("comments", ser, CACHE_TTL)

    context = {
        'comments': comments,
    }

    return render(request, 'app/template.html', context)

def add(request, comment):
    foo_instance = Comment.objects.create(text=comment)
    foo_instance.save()

    return HttpResponse(comment)
