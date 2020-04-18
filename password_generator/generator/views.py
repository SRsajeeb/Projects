from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepassword = ''
    length = int(request.GET.get('length',8))
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('special'):
        characters.extend('!@#$%^&*()_+=-')  

    if request.GET.get('numbers'):
        characters.extend('1234567890') 
    
    for i in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html',{'password':thepassword})
