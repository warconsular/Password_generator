from sqlite3 import threadsafety
from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator\home.html')


def password(request):
    
    characters = list('abcdefijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('symbols'):
        characters.extend(list('!@#$%^&*'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))





    length = int(request.GET.get('length', 12))
        
    thepassword = ''

    for _ in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})


def description(request):
    return render(request, 'generator/description.html')