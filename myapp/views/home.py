import requests
from django.shortcuts import render

def index(request):
    # URL da sua API Flask
    url_api = 'http://127.0.0.1:5000/produtos'
    
    # Fazendo a requisição GET para a API Flask
    response = requests.get(url_api)
    
    if response.status_code == 200:
        # Sucesso na requisição, processa os dados
        produtos = response.json()
    else:
        # Caso haja erro na requisição, podemos definir uma lista vazia ou um erro
        produtos = []
    
    # Retorna o contexto para o template com a lista de produtos
    return render(request, 'index.html', {'produtos': produtos})


def busca_produtos(request):
  # Pegando os parâmetros da busca
    query = request.GET.get('query', '')  # Nome do produto
    categoria = request.GET.get('categoria', '')  # Categoria
    marca = request.GET.get('marca', '')  # Marca
    cor = request.GET.get('cor', '')  # Cor
    preco_min = request.GET.get('preco_min', '')  # Preço mínimo
    preco_max = request.GET.get('preco_max', '')  # Preço máximo

    # URL da sua API Flask
    url_api = 'http://127.0.0.1:5000/produtos'

    # Construir os parâmetros para a requisição
    params = {}
    if query:
        params['nome_produto'] = query
    if categoria:
        params['categoria'] = categoria
    if marca:
        params['marca'] = marca
    if cor:
        params['cor'] = cor
    if preco_min:
        params['preco_min'] = preco_min
    if preco_max:
        params['preco_max'] = preco_max

    # Fazendo a requisição GET para a API Flask
    response = requests.get(url_api, params=params)
    
    if response.status_code == 200:
        # Sucesso na requisição, processa os dados
        produtos = response.json()
    else:
        # Caso haja erro na requisição, podemos definir uma lista vazia ou um erro
        produtos = []

    # Retorna o contexto para o template com a lista de produtos
    return render(request, 'index.html', {'produtos': produtos})