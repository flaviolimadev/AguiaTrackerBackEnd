from django.shortcuts import render
from .models import User  # Importa o modelo de usuários
from .models import Monitorado  # Importa o modelo de usuários
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json


def lista_usuarios(request):
    #usuarios = User.objects.all()  # Obtém todos os usuários
    #eturn JsonResponse(usuarios, safe=False) #render(request, 'usuarios.html', {'usuarios': usuarios})  # Passa os usuários para o template
    
    usuarios = list(User.objects.values())  # Converte o QuerySet em uma lista de dicionários
    return JsonResponse(usuarios, safe=False) 


def lista_monitorado(request):
    data = list(Monitorado.objects.values())  # Converte o QuerySet em uma lista de dicionários
    return JsonResponse(data, safe=False) 

@method_decorator(csrf_exempt, name='dispatch')  # Desativa a verificação CSRF para essa view
class AdicionarUsuarioView(View):

    def post(self, request, *args, **kwargs):
        # Tenta decodificar o JSON recebido
        try:
            dados = json.loads(request.body)
            nome = dados.get('name')
            email = dados.get('email')

            if not nome or not email:
                return JsonResponse({'error': 'Nome e email são obrigatórios.'}, status=400)

            # Cria o novo usuário
            novo_usuario = User.objects.create(name=nome, email=email)

            return JsonResponse({
                'message': 'Usuário criado com sucesso!',
                'user_id': novo_usuario.id,
                'name': novo_usuario.name,
                'email': novo_usuario.email
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Dados inválidos, JSON esperado.'}, status=400)

