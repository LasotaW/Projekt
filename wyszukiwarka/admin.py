from django.contrib import admin
from .models import Klienci 

class Config(admin.ModelAdmin):
    list_display = ('Numer_klienta', 'Imię', 'Nazwisko', "Numer_telefonu", 'Uwagi') 
    search_fields = ['Imię', 'Nazwisko', 'Numer_klienta']

admin.site.register(Klienci, Config)