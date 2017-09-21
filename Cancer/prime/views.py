# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django_tables2 import RequestConfig
from django.http import HttpResponseRedirect
from prime.models import Doctor,Test
from .tables import DoctorTable,TestTable
from .forms import NameForm


# Create your views here.
def people(request):
    table = DoctorTable(Doctor.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'prime/table.html', {'table': table})

def tests(request):
    table = TestTable(Test.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'prime/table.html', {'table': table})

def get_name(request):
    #if this is a POST request, we need to process the form data.
    if request.method == 'POST':
        #create a form instance and populate it with data from the request.
        form = NameForm(request.POST)
        #check whether it is valid.
        if form.is_valid():
            #process the data in form.cleaned_data as required
            print form.cleaned_data['your_name']
            print form.cleaned_data['last_name']
            print form.cleaned_data['doc_id']
            print form.cleaned_data['salary']
            # redirect to a new URL.
            return HttpResponseRedirect('users/input/')
    #if a GET (or any other method) we'l create a blank form.
    else:

        form = NameForm()

    return render(request,'prime/name.html',{'form':form})

def SSNWebsite(request):
    return render(request,'prime/SSNwebsite.html')

def blog(request):
    return render(request,'prime/blog.html')
