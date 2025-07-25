"""fakenewsdetect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls import url
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^home', views.home, name='home'),
	url(r'^nvb', views.nvb, name='nvb'),
	url(r'^pac', views.pac, name='pac'),
	url(r'^svm', views.svm, name='svm'),
	url(r'^dec', views.dec, name='dec'),
	url(r'^randomf', views.randomf, name='randomf'),
	url(r'^mnb', views.mnb, name='mnb'),
	url(r'^graph', views.graph, name='graph'),
	url(r'^accuracy', views.accuracy, name='accuracy'),
	url(r'^$', views.accuracy1, name='accuracy1'),
	url(r'^loginCheck', views.loginCheck, name='loginCheck'),
	url(r'^reg', views.reg, name='reg'),
	url(r'^login', views.login, name='login'),
	url(r'^save', views.save, name='save'),
	url(r'^logout', views.logout, name='logout'),
]
