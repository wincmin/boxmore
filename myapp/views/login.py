import requests
from django.shortcuts import render

def login(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        senha = request.POST.get("senha")

        if not nome or not senha:
            return render(request, "login.html", {"error": "Nome e senha são obrigatórios"})

        api_url = "http://127.0.0.1:5000/login"
        payload = {"nome": nome, "senha": senha}

        try:
            # Consumir a API externa
            response = requests.post(api_url, json=payload)
            response_data = response.json()

            if response.status_code == 200:
                # Retorna a mensagem de sucesso ao template
                return render(request, "login.html", {
                    "success": response_data.get("message", "Login bem-sucedido!"),
                    "redirect": True  # Sinaliza para redirecionar
                })
            else:
                return render(request, "login.html", {"error": response_data.get("message", "Erro no login.")})

        except requests.exceptions.RequestException as e:
            return render(request, "login.html", {"error": f"Erro ao conectar à API: {str(e)}"})

    return render(request, "login.html")
