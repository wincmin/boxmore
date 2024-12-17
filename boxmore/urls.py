"""
URL configuration for boxmore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp.views.home import index
from myapp.views.suporte import suporte
from myapp.views.carrinho import carrinho
from myapp.views.pagamento import pagamento
from myapp.views.sobrenos import sobrenos
from myapp.views.home import busca_produtos
from myapp.views.login import user_login

urlpatterns = [

    path('', index, name='home'),
    path('suporte', suporte, name='suporte'),
    path('carrinho', carrinho, name='carrinho'),
    path('pagamento', pagamento, name='pagamento'),
    path('sobrenos', sobrenos, name='sobrenos'),
    path('busca/', busca_produtos, name='busca_produtos'),
    path('login/', user_login, name='login')
    

]
