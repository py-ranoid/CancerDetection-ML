from django.conf.urls import url

from . import views

urlpatterns = [
 url(r'^thanks/',views.SSNWebsite,name='SSNWebsite'),
 url(r'^input/',views.get_name,name='get_name'),
 url(r'^doctors/',views.people,name='people'),
  url(r'^tests/',views.tests,name='tests'),
  url(r'^',views.blog,name='blog'),
]
