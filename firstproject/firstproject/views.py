from django.shortcuts import redirect
from django.shortcuts import render, HttpResponse

def home(request):
    name = ['niloy', 'nipa', 'puja', 'nirjon']
    context = {
        'name' : name,
    }
    return render(request, 'home.html', context)
