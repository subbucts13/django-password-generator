from django.shortcuts import render
from django.http import HttpRequest
import random

# Create your views here.
def home(request):
    return render(request,'Password_generator/home.html')


def about(request):
    return render(request,'Password_generator/about.html')


def results(request):
    length = int(request.GET.get('length'))
    characters = list('abcdefghijklmnopqrstuvwxyz')
    thepassword=''

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers') == 'on':
        print("number true")
        characters.extend('0123456789')

    for x in range(length):
        thepassword += random.choice(characters)

    print("password="+thepassword)
    print("numbers=" + request.GET.get('numbers'))
    return render(request,'Password_generator/results.html',{'newpassword':thepassword})