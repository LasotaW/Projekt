from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Klienci(models.Model):
    Numer_klienta = models.AutoField(primary_key = True)
    Imię = models.CharField(max_length = 255)
    Nazwisko = models.CharField(max_length = 255)
    Numer_telefonu = PhoneNumberField(null=True)
    Uwagi = models.TextField(null = True)
    
    def __str__(self):
        return self.Imię + ' ' + self.Nazwisko

    class Meta:                        #Niweluje dodawanie "s" na końcu wyrazu/Removes extra "s"
        verbose_name_plural = "Klienci"