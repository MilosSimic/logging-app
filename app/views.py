# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Comment

# Create your views here.
def home_view(request):
    return HttpResponse("Test view")

def test(request):
    return HttpResponse("test page")

def about(request):
    return HttpResponse("about page")

def list_all(request):
    comments = Comment.objects.all()
    context = {
        'comments': comments,
    }

    return render(request, 'app/template.html', context)

def add(request, comment):
    foo_instance = Comment.objects.create(text=comment)
    foo_instance.save()

    return HttpResponse(comment)
