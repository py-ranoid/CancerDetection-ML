from django.conf.urls import url

from . import views

urlpatterns = [
 url(r'^doctors$',views.people,name='people'),
  url(r'^tests$',views.tests,name='tests'),
]
