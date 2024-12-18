from django.shortcuts import render, redirect
import requests

def confirmacao(request):
    return render(request, 'confirma_compra.html')