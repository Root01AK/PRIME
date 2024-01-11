from django.shortcuts import render
from django.http import HttpResponse
from operator import index

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def Case(request):
    return render(request,'Case.html')

def contact(request):
    return render(request,'contact.html')

def contract(request):
    return render(request,'contract.html')

def ezhil(request):
    return render(request,'ezhil.html')

def jatin(request):
    return render(request,'jatin.html')

def laudit(request):
    return render(request,'laudit.html')

def Lease(request):
    return render(request,'Lease.html')

def Legal(request):
    return render(request,'Legal.html')

def mission(request):
    return render(request,'mission.html')

def sanjay(request):
    return render(request,'sanjay.html')

def service(request):
    return render(request,'service.html')

def Summary(request):
    return render(request,'Summary.html')

def team(request):
    return render(request,'team.html')

def udhay(request):
    return render(request,'udhay.html')

def uma(request):
    return render(request,'uma.html')

def vision(request):
    return render(request,'vision.html')