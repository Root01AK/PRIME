"""
URL configuration for Rootpc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from pcapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('Case/',views.Case,name='Case'),
    path('contact/',views.contact,name='contact'),
    path('contract/',views.contract,name='contract'),
    path('ezhil/',views.ezhil,name='ezhil'),
    path('jatin/',views.jatin,name='jatin'),
    path('laudit/',views.laudit,name='laudit'),
    path('Lease/',views.Lease,name='Lease'),
    path('Legal/',views.Legal,name='Legal'),
    path('mission/',views.mission,name='mission'),
    path('sanjay/',views.sanjay,name='sanjay'),
    path('service/',views.service,name='service'),
    path('Summary/',views.Summary,name='Summary'),
    path('team/',views.team,name='team'),
    path('udhay/',views.udhay,name='udhay'),
    path('uma/',views.uma,name='uma'),
    path('vision/',views.vision,name='vision')
]
