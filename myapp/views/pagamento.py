from django.shortcuts import render, redirect
import requests

def pagamento(request):
    return render(request, 'pagamento.html')