from django.shortcuts import render
from django.http import HttpResponse
from .models import Apteka, Kategoria

# Create your views here.

def index(request):
    wszystkie = Apteka.objects.all()
    jeden = Apteka.objects.get(pk=2)
    kat = Apteka.objects.filter(kategoria=1)
    null = Apteka.objects.filer(kategoria__isnull=False)
    return HttpResponse(kat)

