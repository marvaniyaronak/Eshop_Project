from django.shortcuts import render, redirect
from django. views import View




def About(request):
    return render(request, 'about.html')