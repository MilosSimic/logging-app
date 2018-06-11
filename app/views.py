# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request):
    return HttpResponse("Test view")

def test(request):
    return HttpResponse("test page")

def about(request):
    return HttpResponse("about page")
