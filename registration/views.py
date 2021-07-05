from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .forms import RegistrationForm

# Create your views here.

def registration(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():			
			form.save()				
			return redirect('/')
	else:
		form = RegistrationForm()
	return render(request, 'registration/registration.html', {'form': form})

def logout_view(request):
	logout(request)
	return redirect('/')


