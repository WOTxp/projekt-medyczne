from django.shortcuts import render
from django.http import HttpResponse
from .models import Apteka, Kategoria, Obrazy


# Create your views here.

def index(request):
    # wszystkie = Apteka.objects.all()
    # jeden = Apteka.objects.get(pk=2)
    kat = Apteka.objects.filter(kategoria=1)
    null = Apteka.objects.filter(kategoria__isnull=False)
    kategorie = Kategoria.objects.all()
    obrazek = Obrazy.objects.get(id=1)
    dane = {'kategorie': kategorie,
            'obraz': obrazek}
    return render(request, 'szablon.html', dane)


def kategoria(request, id):
    obrazek = Obrazy.objects.get(id=1)
    kategoria_user = Kategoria.objects.get(pk=id)
    kategoria_apteka = Apteka.objects.filter(kategoria=kategoria_user)
    kategorie = Kategoria.objects.all()
    dane = {'kategoria_user': kategoria_user,
            'kategoria_produkt': kategoria_apteka,
            'kategoria': kategorie,
            'obraz': obrazek}
    return render(request, 'kategorie_apteka.html', dane)


def apteka(request, id):
    obrazek = Obrazy.objects.get(id=1)
    apteka_user = Apteka.objects.get(pk=id)
    kategorie = Kategoria.objects.all()
    dane = {'apteka_user': apteka_user, 'kategorie': kategorie,
            'obraz': obrazek}
    return render(request, 'apteka.html', dane)

"""
def obraz(request, x):
    apteka_user = Apteka.objects.get(pk=x)
    dane = {'apteka_user': apteka_user}
    return render(request, 'apteka.html', dane)
"""