from django.shortcuts import render, redirect
from django. views import View




def Contact(request):
    return render(request, 'contact.html')