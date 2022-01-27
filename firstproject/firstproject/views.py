

from django.shortcuts import redirect
from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'home.html')