from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages

def loginUser(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
         user = form.get_user()
         login(request,user)
         return redirect('auth/')
      else:
         messages.info(request, 'Login lub hasło się nie zgadzają')
   else:
      form = AuthenticationForm()
   return render(request, 'login.html')

def searchBar(request):
    return render(request, 'searchBar.html')