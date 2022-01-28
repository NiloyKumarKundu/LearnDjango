from django.shortcuts import redirect
from django.shortcuts import render, HttpResponse


def home(request):
    name = ['niloy', 'nipa', 'puja', 'nirjon']
    context = {
        'name' : name,
    }
    return render(request, 'home.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        content = request.POST['content']

    return render(request, 'contact.html')