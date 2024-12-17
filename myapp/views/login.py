from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User  # Se você estiver usando um modelo personalizado de usuário

# Função para exibir o login e tratar a autenticação
def view_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        # Tenta autenticar o usuário com o email e senha fornecidos
        user = authenticate(request, username=email, password=senha)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial após login bem-sucedido
        else:
            # Se as credenciais estiverem incorretas, retorne uma mensagem de erro
            return render(request, 'myapp/login.html', {
                'error_message': "Usuário ou senha incorretos!"
            })
    
    # Se o método não for POST (por exemplo, GET), apenas renderize o formulário de login
    return render(request, 'myapp/login.html')


# Função para registrar um novo usuário (se você também quiser ter a parte de registro no mesmo arquivo)
def view_register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        # Cria um novo usuário (essa parte pode mudar conforme seu modelo de usuário)
        user = User.objects.create_user(username=email, password=senha)
        
        if user is not None:
            # Se o registro for bem-sucedido, loga o usuário automaticamente
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial após registro bem-sucedido
        else:
            # Se ocorrer algum erro durante o registro
            return render(request, 'myapp/register.html', {
                'error_message': "Erro ao registrar o usuário!"
            })
    
    # Se o método não for POST (por exemplo, GET), apenas renderize o formulário de registro
    return render(request, 'myapp/register.html')
