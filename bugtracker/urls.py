# coding: utf-8
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from . import views

urlpatterns = patterns('',
                       url(r'^$', views.project_index, name='project-index'),

                       url(r'^project/(?P<project_id>[0-9]+)/$', views.ticket_index, name='ticket-index'),
                       url(r'^project/(?P<project_id>[0-9]+)/create/$', views.ticket_create, name='ticket-create'),

                       url(r'^ticket/(?P<pk>[0-9]+)/$', views.ticket_update, name='ticket-update'),
                       # url(r'^register/$',  views.user_create, name="user-create"),
                       url(r'^login/$', 'django.contrib.auth.views.login',
                           {"template_name": "login.html"}, name="login"),
                       url(r'^logout/$', 'django.contrib.auth.views.logout',
                           {"next_page": reverse_lazy('login')}, name="logout"),
                       )
