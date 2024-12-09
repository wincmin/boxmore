from django.shortcuts import render, redirect
import requests

def carrinho(request):
    return render(request, 'carrinho.html')