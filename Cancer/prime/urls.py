from django.conf.urls import url

import views

urlpatterns = [
    url(r'^doctors$', views.people, name='people'),
    url(r'^entry$', views.TestCreate.as_view(), name='ent'),
    url(r'^tests$', views.tests, name='tests'),
    url(r'^result$', views.PrimeView.as_view(), name='test-detail'),
]
