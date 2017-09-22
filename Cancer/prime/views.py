# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django_tables2 import RequestConfig
from django.http import HttpResponseRedirect
from prime.models import Doctor,Test
from .tables import DoctorTable,TestTable
from .forms import NameForm,NewForm


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

            print form.cleaned_data['radius_mean']
            print form.cleaned_data['texture_mean']
            print form.cleaned_data['perimeter_mean']
            print form.cleaned_data['area_mean']
            print form.cleaned_data['smoothness_mean']
            print form.cleaned_data['compactness_mean']
            print form.cleaned_data['concavity_mean']
            print form.cleaned_data['concave_points_mean']
            print form.cleaned_data['symmetry_mean']
            print form.cleaned_data['fractal_dimension_mean']

            print form.cleaned_data['radius_se']
            print form.cleaned_data['texture_se']
            print form.cleaned_data['perimeter_se']
            print form.cleaned_data['area_se']
            print form.cleaned_data['smoothness_se']
            print form.cleaned_data['compactness_se']
            print form.cleaned_data['concavity_se']
            print form.cleaned_data['concave_points_se']
            print form.cleaned_data['symmetry_se']
            print form.cleaned_data['fractal_dimension_se']

            print form.cleaned_data['radius_worst']
            print form.cleaned_data['texture_worst']
            print form.cleaned_data['perimeter_worst']
            print form.cleaned_data['area_worst']
            print form.cleaned_data['smoothness_worst']
            print form.cleaned_data['compactness_worst']
            print form.cleaned_data['concavity_worst']
            print form.cleaned_data['concave_points_worst']
            print form.cleaned_data['symmetry_worst']
            print form.cleaned_data['fractal_dimension_worst']

            # print "hello"
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

def login(request):
    return render(request,'prime/login.html')

def signup(request):
    #if this is a POST request, we need to process the form data.
    if request.method == 'POST':
        #create a form instance and populate it with data from the request.
        form = NewForm(request.POST)
        #check whether it is valid.
        if form.is_valid():
            #process the data in form.cleaned_data as required
            return HttpResponseRedirect('users/signup/')
    #if a GET (or any other method) we'l create a blank form.
    else:

        form = NewForm()

    return render(request,'prime/signup.html',{'form':form})

def about(request):
    return render(request,'prime/about.html')
