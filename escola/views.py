from django.shortcuts import render
from django.http import HttpResponse


def home(request): #pedindo para fazer uma request
    return render(request, 'escola/home.html') #'home.html' meu template #global/home.html

