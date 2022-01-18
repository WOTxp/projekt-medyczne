from django.shortcuts import render
from django.http import HttpResponse
from .models import Apteka, Kategoria

# Create your views here.

def index (request):
    #wszystkie = Apteka.objects.all()
    #jeden = Apteka.objects.get(pk=2)
    kat = Apteka.objects.filter(kategoria=1)
    null = Apteka.objects.filter(kategoria__isnull=False)
    kategorie = Kategoria.objects.all()
    dane = {'kategorie' : kategorie}
    return render(request, 'szablon.html', dane)

def kategoria (request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    kategoria_apteka = Apteka.objects.filter(kategoria = kategoria_user)
    kategorie = Kategoria.objects.all()
    dane = {'kategoria_user' : kategoria_user,
            'kategoria_produkt' : kategoria_apteka,
            'kategoria' : kategorie}
    return render(request, 'kategorie_apteka.html', dane)

def apteka (request, id):
    apteka_user = Apteka.objects.get(pk=id)
    kategorie = Kategoria.objects.all()
    dane = {'apteka_user' : apteka_user, 'kategorie' : kategorie}
    return render(request, 'apteka.html', dane)

