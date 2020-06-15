from django.contrib import admin
from .models import Klienci 

class Config(admin.ModelAdmin):
    list_display = ('Numer_klienta', 'Imię', 'Nazwisko', "Numer_telefonu", 'Uwagi') 

admin.site.register(Klienci, Config)