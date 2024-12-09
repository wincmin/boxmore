from django.shortcuts import render, redirect
import requests

def sobrenos(request):
    return render(request, 'sobrenos.html')