# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Comment(models.Model):
    text = models.CharField(max_length=200)
