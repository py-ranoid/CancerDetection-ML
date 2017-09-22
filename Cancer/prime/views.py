# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django_tables2 import RequestConfig
from prime.models import Doctor, Test
from .tables import DoctorTable, TestTable
from django.http.response import HttpResponse, JsonResponse
from forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from models import Test
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def people(request):
    table = DoctorTable(Doctor.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'prime/table.html', {'table': table})
    # return HttpResponse("<h1>Hey</h1>")


def entry(request):
    table = DoctorTable(Doctor.objects.all())
    # RequestConfig(request).configure(table)
    # return render(request, 'prime/table.html', {'table': table})
    return HttpResponse("<h1>Hey</h1>")


def tests(request):
    table = TestTable(Test.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'prime/table.html', {'table': table})


class ContactView(FormView):
    template_name = 'prime/contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        return HttpResponse("<h1>Hey</h1>")

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)


class TestCreate(CreateView):
    model = Test
    fields = ['doc', 'test_id', 'Attributes']


class PrimeView(generic.View):
    def get(self, request, *args, **kwargs):
        print self.request.body.decode('utf-8')
        print request.body
        #verify_token = self.request.GET.get('hub.verify_token', '08081997')
        # if verify_token == '08081997':
        #    with open("/home/ubuntu/autobot/nohup.out", 'r') as fl:
        #        logcontents = fl.read()
        # return HttpResponse(self.request.GET.get('hub.challenge', logcontents.replace("\n", "<br/>")))
        # else:
        return HttpResponse('Error, invalid tokeN')

    '''
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)
    '''
    """
    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        req_body = self.request.body.decode('utf-8')
        print "=============================================\n============================================="
        print "Received body :", req_body
        incoming_message = json.loads(req_body)
        mtype = incoming_message["mtype"]
        uid = incoming_message["uid"]
        content = incoming_message["content"]
        # pprint(incoming_message)
        text = content["text"]
    """

    def post(self, request, *args, **kwargs):
        print self.request.body.decode('utf-8')
        print request.body
        #verify_token = self.request.GET.get('hub.verify_token', '08081997')
        # if verify_token == '08081997':
        #    with open("/home/ubuntu/autobot/nohup.out", 'r') as fl:
        #        logcontents = fl.read()
        # return HttpResponse(self.request.GET.get('hub.challenge', logcontents.replace("\n", "<br/>")))
        # else:
        return HttpResponse('Hey')
