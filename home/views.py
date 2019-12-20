from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html', {'title': 'Accueil'})


def legal(request):
    return render(request, 'home/legal.html', {'title': 'Mentions Legales'})
