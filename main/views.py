from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.

def home(response):
	if response.user.is_authenticated:
		return render(response, "main/home.html", {})
	else:
		return redirect("login")