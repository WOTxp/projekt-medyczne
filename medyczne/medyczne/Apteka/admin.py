from django.contrib import admin
from .models import Apteka, Producent, Kategoria, Obrazy, Recepty

# Register your models here.

admin.site.register(Apteka)
admin.site.register(Producent)
admin.site.register(Kategoria)
admin.site.register(Obrazy)
