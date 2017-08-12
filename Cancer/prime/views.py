# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django_tables2 import RequestConfig
from prime.models import Doctor,Test
from .tables import DoctorTable,TestTable

# Create your views here.
def people(request):
    table = DoctorTable(Doctor.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'prime/table.html', {'table': table})

def tests(request):
    table = TestTable(Test.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'prime/table.html', {'table': table})
