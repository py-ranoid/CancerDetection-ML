# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Doctor(models.Model):
    doc_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Tests(models.Model):
    log = models.DateTimeField(auto_now=True)
    doc = models.ForeignKey(User, unique=True)
    attribSring = models.CharField  
