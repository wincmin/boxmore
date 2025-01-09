from django.shortcuts import render, redirect
import requests

def register(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        senha = request.POST.get("senha")
        cpf = request.POST.get("cpf")
        email = request.POST.get("email")

        # Verificar se os campos obrigatórios estão preenchidos
        if not nome or not senha or not cpf or not email:
            return render(request, "register.html", {"error": "Todos os campos são obrigatórios."})

        # URL da API de cadastro
        api_url = "http://127.0.0.1:5000/register"
        payload = {
            "nome": nome,
            "senha": senha,
            "cpf": cpf,
            "email": email
        }

        try:
            # Consumir a API externa para cadastro
            response = requests.post(api_url, json=payload)
            response_data = response.json()

            if response.status_code == 201:
                # Caso a API retorne sucesso, redireciona para a página de login
                return render(request, "register.html", {
                    "success": response_data.get("message", "Cadastro bem-sucedido!"),
                    "redirect": True  # Redireciona após o sucesso
                })
            elif response.status_code == 409:
                # Caso o usuário já exista
                return render(request, "register.html", {"error": response_data.get("message", "Usuário já existe.")})
            else:
                return render(request, "register.html", {"error": response_data.get("message", "Erro no cadastro.")})

        except requests.exceptions.RequestException as e:
            return render(request, "register.html", {"error": f"Erro ao conectar à API: {str(e)}"})

    return render(request, "register.html")
