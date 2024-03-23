#from django.shortcuts import render
from django.http import HttpResponse


def home(request): #pedindo para fazer uma request
    return HttpResponse("Hello World")

def sobre(request): #pedindo para fazer uma request
    return HttpResponse("Sobre")

def contato(request): #pedindo para fazer uma request
    return HttpResponse("Contato")