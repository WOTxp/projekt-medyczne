from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Apteka, Kategoria, Obrazy, Recepty
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import CreateUserForm


def wylogowywanie(request):
    logout(request)
    return redirect('logowanie')


def logowanie(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Nazwa lub hasło jest niepoprawne.')
            return render(request, 'logowanie.html', {})

        return render(request, 'logowanie.html', {})


def rejestracja(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Konto stworzone dla ' + user)

                return redirect('logowanie')
        dane = {'form': form}
        return render(request, 'rejestracja.html', dane)


@login_required(login_url='logowanie')
def index(request):
    # wszystkie = Apteka.objects.all()
    # jeden = Apteka.objects.get(pk=2)
    kat = Apteka.objects.filter(kategoria=1)
    null = Apteka.objects.filter(kategoria__isnull=False)
    kategorie = Kategoria.objects.all()
    obrazek = Obrazy.objects.get(id=1)  # Logo
    tlo = Obrazy.objects.get(id=2)  # tlo
    dane = {'kategorie': kategorie,
            'obraz': obrazek,
            'tlo': tlo}
    return render(request, 'szablon.html', dane)


@login_required(login_url='logowanie')
def kategoria(request, id):
    obrazek = Obrazy.objects.get(id=1)  # Logo
    tlo = Obrazy.objects.get(id=2)  # tlo
    kategoria_user = Kategoria.objects.get(pk=id)
    kategoria_apteka = Apteka.objects.filter(kategoria=kategoria_user).order_by('nazwa')
    kategorie = Kategoria.objects.all()
    dane = {'kategoria_user': kategoria_user,
            'kategoria_produkt': kategoria_apteka,
            'kategorie': kategorie,
            'obraz': obrazek,
            'tlo': tlo}
    return render(request, 'kategorie_apteka.html', dane)


@login_required(login_url='logowanie')
def apteka(request, id):
    obrazek = Obrazy.objects.get(id=1)  # Logo
    tlo = Obrazy.objects.get(id=2)  # tlo
    apteka_user = Apteka.objects.get(pk=id)
    kategorie = Kategoria.objects.all()
    dane = {'apteka_user': apteka_user,
            'kategorie': kategorie,
            'obraz': obrazek,
            'tlo': tlo}
    return render(request, 'apteka.html', dane)


@login_required(login_url='logowanie')
def szukaj(request):
    obrazek = Obrazy.objects.get(id=1)  # Logo
    tlo = Obrazy.objects.get(id=2)  # tlo
    kategorie = Kategoria.objects.all()
    if request.method == "POST":
        szukana = request.POST['szukane']
        wynik = Apteka.objects.filter(nazwa__contains=szukana).order_by('nazwa')
        dane = {'kategorie': kategorie,
                'obraz': obrazek,
                'szukane': szukana,
                'wynik': wynik,
            'tlo': tlo}
        return render(request, 'search.html', dane)
    else:
        dane = {'kategorie': kategorie,
                'obraz': obrazek,
            'tlo': tlo}
        return render(request, 'search.html', dane)
