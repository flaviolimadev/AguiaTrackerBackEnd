from django.shortcuts import render
from .models import User
from .models import Monitorado
from .models import Dispositivo
from .models import Foto  # Corrigido o nome para 'Foto'
from .models import Arquivo
from .models import Telefone
from .models import Processo
from .models import Estabelecimento
from .models import Perfil
from .models import Faccao
from .models import Zona
from .models import TrackingData
from .models import SituacaoTrabalhista  # Corrigido o import de 'SituacaoTrabalhista'
from .models import RegraCumprimentoPena
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json


def lista_usuarios(request):
    datas = list(User.objects.values())  # Converte o QuerySet em uma lista de dicionários
    return JsonResponse(datas, safe=False) 

def lista_monitorados(request):
    monitorados = list(Monitorado.objects.values())  # Obtém todos os registros do model Monitorado
    return JsonResponse(monitorados, safe=False) 

def lista_dispositivos(request):
    dispositivo = list(Dispositivo.objects.values())  # Obtém todos os registros do model Monitorado
    return JsonResponse(dispositivo, safe=False) 

def lista_fotos(request):
    data = list(Foto.objects.values())  # Obtém todos os registros do model Monitorado
    return JsonResponse(data, safe=False) 

def lista_arquivos(request):
    data = list(Arquivo.objects.values())  # Obtém todos os registros do model Monitorado
    return JsonResponse(data, safe=False) 

def lista_telefones(request):
    data = list(Telefone.objects.values())  # Obtém todos os registros do model Monitorado
    return JsonResponse(data, safe=False) 

def lista_processos(request):
    data = list(Processo.objects.values())  # Obtém todos os registros do model Monitorado
    return JsonResponse(data, safe=False) 

def lista_estabelecimento(request):
    data = list(Estabelecimento.objects.values())  # Obtém todos os registros do model Monitorado
    return JsonResponse(data, safe=False) 
 
def lista_perfil(request):
    data = list(Perfil.objects.values())  # Obtém todos os registros do model Monitorado
    return JsonResponse(data, safe=False) 

def lista_regra_cumprimento_pena(request):
    data = list(RegraCumprimentoPena.objects.values())  # Obtém todos os registros do model Monitorado
    return JsonResponse(data, safe=False) 

def lista_faccao(request):
    data = list(Faccao.objects.values())  # Obtém todos os registros do model Monitorado
    return JsonResponse(data, safe=False)
 
def lista_situacao_trabalhista(request):
    data = list(SituacaoTrabalhista.objects.values())  # Obtém todos os registros do model Monitorado
    return JsonResponse(data, safe=False)

def lista_zona(request):
    data = list(Zona.objects.values())  # Obtém todos os registros do model Monitorado
    return JsonResponse(data, safe=False)

def lista_tracking_data(request):
    data = list(TrackingData.objects.values())  # Obtém todos os registros do model Monitorado
    return JsonResponse(data, safe=False)



# CRIAR USUÁRIO
@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = User.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                password=data.get('password')
            )
            return JsonResponse({'message': 'Usuário criado com sucesso!', 'user_id': user.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# LISTAR TODOS USUÁRIOS
class UserListView(View):
    def get(self, request):
        users = list(User.objects.values())
        return JsonResponse(users, safe=False)

# CONSULTAR USUÁRIO POR ID
class UserDetailView(View):
    def get(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
            return JsonResponse({
                'id': user.id,
                'name': user.name,
                'email': user.email,
            })
        except User.DoesNotExist:
            return JsonResponse({'error': 'Usuário não encontrado'}, status=404)

# ATUALIZAR USUÁRIO
@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(View):
    def post(self, request, user_id):
        try:
            data = json.loads(request.body)
            user = User.objects.get(pk=user_id)
            user.name = data.get('name', user.name)
            user.email = data.get('email', user.email)
            user.password = data.get('password', user.password)
            user.save()
            return JsonResponse({'message': 'Usuário atualizado com sucesso!'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'Usuário não encontrado'}, status=404)

# DELETAR USUÁRIO
@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(View):
    def post(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
            user.delete()
            return JsonResponse({'message': 'Usuário excluído com sucesso!'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'Usuário não encontrado'}, status=404)

#---------------------------------------------------------------------

# CRIAR MONITORADO
@method_decorator(csrf_exempt, name='dispatch')
class MonitoradoCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            monitorado = Monitorado.objects.create(
                key_monitorado=data.get('key_monitorado'),
                matricula_monitorado=data.get('matricula_monitorado'),
                nome_monitorado=data.get('nome_monitorado'),
                dispositivo=data.get('dispositivo'),
                agencia_id=data.get('agencia_id'),
                estabelecimento_prisional_id=data.get('estabelecimento_prisional_id', 0),
                monitorado_vitima=data.get('monitorado_vitima', 0),
                perfil_id=data.get('perfil_id'),
                nome_completo=data.get('nome_completo'),
                nome_social=data.get('nome_social', ''),
                apelido=data.get('apelido', ''),
                nome_mae=data.get('nome_mae'),
                nome_pai=data.get('nome_pai', ''),
                genero=data.get('genero'),
                cpf=data.get('cpf'),
                rg=data.get('rg', ''),
                data_nascimento=data.get('data_nascimento'),
                protocolo_monitoramento=data.get('protocolo_monitoramento'),
                regime_id=data.get('regime_id', 0),
                controle_prazo=data.get('controle_prazo', '0'),
                inicio_medida=data.get('inicio_medida'),
                dias_medida=data.get('dias_medida'),
                prorrogacao=data.get('prorrogacao', None),
                tipo_monitorado_id=data.get('tipo_monitorado_id', 0),
                periculosidade=data.get('periculosidade', 0),
                faccao_id=data.get('faccao_id', None),
                religiao=data.get('religiao', ''),
                estado_civil=data.get('estado_civil', ''),
                situacao_trabalhista_id=data.get('situacao_trabalhista_id', 0),
                escolaridade_id=data.get('escolaridade_id', 0),
                fotos=data.get('fotos', ''),
                arquivos=data.get('arquivos', ''),
                telefones=data.get('telefones', ''),
                zonas=data.get('zonas', ''),
                processos=data.get('processos', ''),
                agendamento_servicos=data.get('agendamento_servicos', ''),
                comandos_dispositivo=data.get('comandos_dispositivo', ''),
                notificacoes_observacoes=data.get('notificacoes_observacoes', ''),
                historico_posicoes=data.get('historico_posicoes', '')
            )
            return JsonResponse({'message': 'Monitorado criado com sucesso!', 'monitorado_id': monitorado.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# LISTAR TODOS MONITORADOS
class MonitoradoListView(View):
    def get(self, request):
        monitorados = list(Monitorado.objects.values())
        return JsonResponse(monitorados, safe=False)

# CONSULTAR MONITORADO POR ID
class MonitoradoDetailView(View):
    def get(self, request, monitorado_id):
        try:
            monitorado = Monitorado.objects.get(pk=monitorado_id)
            return JsonResponse({
                'id': monitorado.id,
                'nome_monitorado': monitorado.nome_monitorado,
                'cpf': monitorado.cpf,
                'data_nascimento': monitorado.data_nascimento,
                # Adicione outros campos conforme necessário
            })
        except Monitorado.DoesNotExist:
            return JsonResponse({'error': 'Monitorado não encontrado'}, status=404)

# ATUALIZAR MONITORADO
@method_decorator(csrf_exempt, name='dispatch')
class MonitoradoUpdateView(View):
    def post(self, request, monitorado_id):
        try:
            data = json.loads(request.body)
            monitorado = Monitorado.objects.get(pk=monitorado_id)
            monitorado.key_monitorado = data.get('key_monitorado', monitorado.key_monitorado)
            monitorado.matricula_monitorado = data.get('matricula_monitorado', monitorado.matricula_monitorado)
            monitorado.nome_monitorado = data.get('nome_monitorado', monitorado.nome_monitorado)
            monitorado.dispositivo = data.get('dispositivo', monitorado.dispositivo)
            monitorado.agencia_id = data.get('agencia_id', monitorado.agencia_id)
            monitorado.estabelecimento_prisional_id = data.get('estabelecimento_prisional_id', monitorado.estabelecimento_prisional_id)
            monitorado.monitorado_vitima = data.get('monitorado_vitima', monitorado.monitorado_vitima)
            monitorado.perfil_id = data.get('perfil_id', monitorado.perfil_id)
            monitorado.nome_completo = data.get('nome_completo', monitorado.nome_completo)
            monitorado.nome_social = data.get('nome_social', monitorado.nome_social)
            monitorado.apelido = data.get('apelido', monitorado.apelido)
            monitorado.nome_mae = data.get('nome_mae', monitorado.nome_mae)
            monitorado.nome_pai = data.get('nome_pai', monitorado.nome_pai)
            monitorado.genero = data.get('genero', monitorado.genero)
            monitorado.cpf = data.get('cpf', monitorado.cpf)
            monitorado.rg = data.get('rg', monitorado.rg)
            monitorado.data_nascimento = data.get('data_nascimento', monitorado.data_nascimento)
            monitorado.protocolo_monitoramento = data.get('protocolo_monitoramento', monitorado.protocolo_monitoramento)
            monitorado.regime_id = data.get('regime_id', monitorado.regime_id)
            monitorado.controle_prazo = data.get('controle_prazo', monitorado.controle_prazo)
            monitorado.inicio_medida = data.get('inicio_medida', monitorado.inicio_medida)
            monitorado.dias_medida = data.get('dias_medida', monitorado.dias_medida)
            monitorado.prorrogacao = data.get('prorrogacao', monitorado.prorrogacao)
            monitorado.tipo_monitorado_id = data.get('tipo_monitorado_id', monitorado.tipo_monitorado_id)
            monitorado.periculosidade = data.get('periculosidade', monitorado.periculosidade)
            monitorado.faccao_id = data.get('faccao_id', monitorado.faccao_id)
            monitorado.religiao = data.get('religiao', monitorado.religiao)
            monitorado.estado_civil = data.get('estado_civil', monitorado.estado_civil)
            monitorado.situacao_trabalhista_id = data.get('situacao_trabalhista_id', monitorado.situacao_trabalhista_id)
            monitorado.escolaridade_id = data.get('escolaridade_id', monitorado.escolaridade_id)
            monitorado.fotos = data.get('fotos', monitorado.fotos)
            monitorado.arquivos = data.get('arquivos', monitorado.arquivos)
            monitorado.telefones = data.get('telefones', monitorado.telefones)
            monitorado.zonas = data.get('zonas', monitorado.zonas)
            monitorado.processos = data.get('processos', monitorado.processos)
            monitorado.agendamento_servicos = data.get('agendamento_servicos', monitorado.agendamento_servicos)
            monitorado.comandos_dispositivo = data.get('comandos_dispositivo', monitorado.comandos_dispositivo)
            monitorado.notificacoes_observacoes = data.get('notificacoes_observacoes', monitorado.notificacoes_observacoes)
            monitorado.historico_posicoes = data.get('historico_posicoes', monitorado.historico_posicoes)

            monitorado.save()
            return JsonResponse({'message': 'Monitorado atualizado com sucesso!'})
        except Monitorado.DoesNotExist:
            return JsonResponse({'error': 'Monitorado não encontrado'}, status=404)
    def post(self, request, monitorado_id):
        try:
            data = json.loads(request.body)
            monitorado = Monitorado.objects.get(pk=monitorado_id)
            monitorado.nome_monitorado = data.get('nome_monitorado', monitorado.nome_monitorado)
            monitorado.cpf = data.get('cpf', monitorado.cpf)
            monitorado.save()
            return JsonResponse({'message': 'Monitorado atualizado com sucesso!'})
        except Monitorado.DoesNotExist:
            return JsonResponse({'error': 'Monitorado não encontrado'}, status=404)

# DELETAR MONITORADO
@method_decorator(csrf_exempt, name='dispatch')
class MonitoradoDeleteView(View):
    def post(self, request, monitorado_id):
        try:
            monitorado = Monitorado.objects.get(pk=monitorado_id)
            monitorado.delete()
            return JsonResponse({'message': 'Monitorado excluído com sucesso!'})
        except Monitorado.DoesNotExist:
            return JsonResponse({'error': 'Monitorado não encontrado'}, status=404)

#---------------------------------------------------------------------

# CRIAR DISPOSITIVO
@method_decorator(csrf_exempt, name='dispatch')
class DispositivoCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            dispositivo = Dispositivo.objects.create(
                num_serie=data.get('num_serie'),
                versao_firmware=data.get('versao_firmware'),
                status=data.get('status', 0),
                sim_card_01=data.get('sim_card_01'),
                sim_card_02=data.get('sim_card_02')
            )
            return JsonResponse({'message': 'Dispositivo criado com sucesso!', 'dispositivo_id': dispositivo.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# LISTAR TODOS OS DISPOSITIVOS
class DispositivoListView(View):
    def get(self, request):
        dispositivos = list(Dispositivo.objects.values())
        return JsonResponse(dispositivos, safe=False)

# CONSULTAR DISPOSITIVO POR ID
class DispositivoDetailView(View):
    def get(self, request, dispositivo_id):
        try:
            dispositivo = Dispositivo.objects.get(pk=dispositivo_id)
            return JsonResponse({
                'id': dispositivo.id,
                'num_serie': dispositivo.num_serie,
                'versao_firmware': dispositivo.versao_firmware,
                'status': dispositivo.status,
                'sim_card_01': dispositivo.sim_card_01,
                'sim_card_02': dispositivo.sim_card_02,
                'created_at': dispositivo.created_at,
                'updated_at': dispositivo.updated_at
            })
        except Dispositivo.DoesNotExist:
            return JsonResponse({'error': 'Dispositivo não encontrado'}, status=404)

# ATUALIZAR DISPOSITIVO
@method_decorator(csrf_exempt, name='dispatch')
class DispositivoUpdateView(View):
    def post(self, request, dispositivo_id):
        try:
            data = json.loads(request.body)
            dispositivo = Dispositivo.objects.get(pk=dispositivo_id)
            dispositivo.num_serie = data.get('num_serie', dispositivo.num_serie)
            dispositivo.versao_firmware = data.get('versao_firmware', dispositivo.versao_firmware)
            dispositivo.status = data.get('status', dispositivo.status)
            dispositivo.sim_card_01 = data.get('sim_card_01', dispositivo.sim_card_01)
            dispositivo.sim_card_02 = data.get('sim_card_02', dispositivo.sim_card_02)
            dispositivo.save()
            return JsonResponse({'message': 'Dispositivo atualizado com sucesso!'})
        except Dispositivo.DoesNotExist:
            return JsonResponse({'error': 'Dispositivo não encontrado'}, status=404)

# DELETAR DISPOSITIVO
@method_decorator(csrf_exempt, name='dispatch')
class DispositivoDeleteView(View):
    def post(self, request, dispositivo_id):
        try:
            dispositivo = Dispositivo.objects.get(pk=dispositivo_id)
            dispositivo.delete()
            return JsonResponse({'message': 'Dispositivo excluído com sucesso!'})
        except Dispositivo.DoesNotExist:
            return JsonResponse({'error': 'Dispositivo não encontrado'}, status=404)


#---------------------------------------------------------------------

# CRIAR FOTO
@method_decorator(csrf_exempt, name='dispatch')
class FotoCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            foto = Foto.objects.create(
                foto=data.get('foto'),
                principal=data.get('principal', 0),
                operador_registro=data.get('operador_registro', 0)
            )
            return JsonResponse({'message': 'Foto criada com sucesso!', 'foto_id': foto.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# LISTAR TODAS AS FOTOS
class FotoListView(View):
    def get(self, request):
        fotos = list(Foto.objects.values())
        return JsonResponse(fotos, safe=False)

# CONSULTAR FOTO POR ID
class FotoDetailView(View):
    def get(self, request, foto_id):
        try:
            foto = Foto.objects.get(pk=foto_id)
            return JsonResponse({
                'id': foto.id,
                'foto': foto.foto,
                'principal': foto.principal,
                'operador_registro': foto.operador_registro,
                'created_at': foto.created_at,
                'updated_at': foto.updated_at
            })
        except Foto.DoesNotExist:
            return JsonResponse({'error': 'Foto não encontrada'}, status=404)

# ATUALIZAR FOTO
@method_decorator(csrf_exempt, name='dispatch')
class FotoUpdateView(View):
    def post(self, request, foto_id):
        try:
            data = json.loads(request.body)
            foto = Foto.objects.get(pk=foto_id)
            foto.foto = data.get('foto', foto.foto)
            foto.principal = data.get('principal', foto.principal)
            foto.operador_registro = data.get('operador_registro', foto.operador_registro)
            foto.save()
            return JsonResponse({'message': 'Foto atualizada com sucesso!'})
        except Foto.DoesNotExist:
            return JsonResponse({'error': 'Foto não encontrada'}, status=404)

# DELETAR FOTO
@method_decorator(csrf_exempt, name='dispatch')
class FotoDeleteView(View):
    def post(self, request, foto_id):
        try:
            foto = Foto.objects.get(pk=foto_id)
            foto.delete()
            return JsonResponse({'message': 'Foto excluída com sucesso!'})
        except Foto.DoesNotExist:
            return JsonResponse({'error': 'Foto não encontrada'}, status=404)

#---------------------------------------------------------------------

# CRIAR ARQUIVO
@method_decorator(csrf_exempt, name='dispatch')
class ArquivoCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            arquivo = Arquivo.objects.create(
                tipo_arquivo=data.get('tipo_arquivo'),
                formato_arquivo=data.get('formato_arquivo'),
                arquivo=data.get('arquivo'),
                operador_registro=data.get('operador_registro', 0)
            )
            return JsonResponse({'message': 'Arquivo criado com sucesso!', 'arquivo_id': arquivo.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# LISTAR TODOS OS ARQUIVOS
class ArquivoListView(View):
    def get(self, request):
        arquivos = list(Arquivo.objects.values())
        return JsonResponse(arquivos, safe=False)

# CONSULTAR ARQUIVO POR ID
class ArquivoDetailView(View):
    def get(self, request, arquivo_id):
        try:
            arquivo = Arquivo.objects.get(pk=arquivo_id)
            return JsonResponse({
                'id': arquivo.id,
                'tipo_arquivo': arquivo.tipo_arquivo,
                'formato_arquivo': arquivo.formato_arquivo,
                'arquivo': arquivo.arquivo,
                'operador_registro': arquivo.operador_registro,
                'created_at': arquivo.created_at,
                'updated_at': arquivo.updated_at
            })
        except Arquivo.DoesNotExist:
            return JsonResponse({'error': 'Arquivo não encontrado'}, status=404)

# ATUALIZAR ARQUIVO
@method_decorator(csrf_exempt, name='dispatch')
class ArquivoUpdateView(View):
    def post(self, request, arquivo_id):
        try:
            data = json.loads(request.body)
            arquivo = Arquivo.objects.get(pk=arquivo_id)
            arquivo.tipo_arquivo = data.get('tipo_arquivo', arquivo.tipo_arquivo)
            arquivo.formato_arquivo = data.get('formato_arquivo', arquivo.formato_arquivo)
            arquivo.arquivo = data.get('arquivo', arquivo.arquivo)
            arquivo.operador_registro = data.get('operador_registro', arquivo.operador_registro)
            arquivo.save()
            return JsonResponse({'message': 'Arquivo atualizado com sucesso!'})
        except Arquivo.DoesNotExist:
            return JsonResponse({'error': 'Arquivo não encontrado'}, status=404)

# DELETAR ARQUIVO
@method_decorator(csrf_exempt, name='dispatch')
class ArquivoDeleteView(View):
    def post(self, request, arquivo_id):
        try:
            arquivo = Arquivo.objects.get(pk=arquivo_id)
            arquivo.delete()
            return JsonResponse({'message': 'Arquivo excluído com sucesso!'})
        except Arquivo.DoesNotExist:
            return JsonResponse({'error': 'Arquivo não encontrado'}, status=404)


#---------------------------------------------------------------------

# CRIAR TELEFONE
@method_decorator(csrf_exempt, name='dispatch')
class TelefoneCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            telefone = Telefone.objects.create(
                numero=data.get('numero'),
                whatsapp=data.get('whatsapp', 0),
                tipo_contato=data.get('tipo_contato'),
                operador_registro=data.get('operador_registro', 0)
            )
            return JsonResponse({'message': 'Telefone criado com sucesso!', 'telefone_id': telefone.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# LISTAR TODOS OS TELEFONES
class TelefoneListView(View):
    def get(self, request):
        telefones = list(Telefone.objects.values())
        return JsonResponse(telefones, safe=False)

# CONSULTAR TELEFONE POR ID
class TelefoneDetailView(View):
    def get(self, request, telefone_id):
        try:
            telefone = Telefone.objects.get(pk=telefone_id)
            return JsonResponse({
                'id': telefone.id,
                'numero': telefone.numero,
                'whatsapp': telefone.whatsapp,
                'tipo_contato': telefone.tipo_contato,
                'operador_registro': telefone.operador_registro,
                'created_at': telefone.created_at,
                'updated_at': telefone.updated_at
            })
        except Telefone.DoesNotExist:
            return JsonResponse({'error': 'Telefone não encontrado'}, status=404)

# ATUALIZAR TELEFONE
@method_decorator(csrf_exempt, name='dispatch')
class TelefoneUpdateView(View):
    def post(self, request, telefone_id):
        try:
            data = json.loads(request.body)
            telefone = Telefone.objects.get(pk=telefone_id)
            telefone.numero = data.get('numero', telefone.numero)
            telefone.whatsapp = data.get('whatsapp', telefone.whatsapp)
            telefone.tipo_contato = data.get('tipo_contato', telefone.tipo_contato)
            telefone.operador_registro = data.get('operador_registro', telefone.operador_registro)
            telefone.save()
            return JsonResponse({'message': 'Telefone atualizado com sucesso!'})
        except Telefone.DoesNotExist:
            return JsonResponse({'error': 'Telefone não encontrado'}, status=404)

# DELETAR TELEFONE
@method_decorator(csrf_exempt, name='dispatch')
class TelefoneDeleteView(View):
    def post(self, request, telefone_id):
        try:
            telefone = Telefone.objects.get(pk=telefone_id)
            telefone.delete()
            return JsonResponse({'message': 'Telefone excluído com sucesso!'})
        except Telefone.DoesNotExist:
            return JsonResponse({'error': 'Telefone não encontrado'}, status=404)

#---------------------------------------------------------------------

# CRIAR PROCESSO
@method_decorator(csrf_exempt, name='dispatch')
class ProcessoCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            processo = Processo.objects.create(
                num_processo=data.get('num_processo', 0),
                estado=data.get('estado'),
                municipio=data.get('municipio'),
                vara=data.get('vara'),
                magistrado=data.get('magistrado', ''),
                resumo_sentenca=data.get('resumo_sentenca', ''),
                ativo=data.get('ativo', 0),
                principal=data.get('principal', 0)
            )
            return JsonResponse({'message': 'Processo criado com sucesso!', 'processo_id': processo.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# LISTAR TODOS OS PROCESSOS
class ProcessoListView(View):
    def get(self, request):
        processos = list(Processo.objects.values())
        return JsonResponse(processos, safe=False)

# CONSULTAR PROCESSO POR ID
class ProcessoDetailView(View):
    def get(self, request, processo_id):
        try:
            processo = Processo.objects.get(pk=processo_id)
            return JsonResponse({
                'id': processo.id,
                'num_processo': processo.num_processo,
                'estado': processo.estado,
                'municipio': processo.municipio,
                'vara': processo.vara,
                'magistrado': processo.magistrado,
                'resumo_sentenca': processo.resumo_sentenca,
                'ativo': processo.ativo,
                'principal': processo.principal,
                'created_at': processo.created_at,
                'updated_at': processo.updated_at
            })
        except Processo.DoesNotExist:
            return JsonResponse({'error': 'Processo não encontrado'}, status=404)

# ATUALIZAR PROCESSO
@method_decorator(csrf_exempt, name='dispatch')
class ProcessoUpdateView(View):
    def post(self, request, processo_id):
        try:
            data = json.loads(request.body)
            processo = Processo.objects.get(pk=processo_id)
            processo.num_processo = data.get('num_processo', processo.num_processo)
            processo.estado = data.get('estado', processo.estado)
            processo.municipio = data.get('municipio', processo.municipio)
            processo.vara = data.get('vara', processo.vara)
            processo.magistrado = data.get('magistrado', processo.magistrado)
            processo.resumo_sentenca = data.get('resumo_sentenca', processo.resumo_sentenca)
            processo.ativo = data.get('ativo', processo.ativo)
            processo.principal = data.get('principal', processo.principal)
            processo.save()
            return JsonResponse({'message': 'Processo atualizado com sucesso!'})
        except Processo.DoesNotExist:
            return JsonResponse({'error': 'Processo não encontrado'}, status=404)

# DELETAR PROCESSO
@method_decorator(csrf_exempt, name='dispatch')
class ProcessoDeleteView(View):
    def post(self, request, processo_id):
        try:
            processo = Processo.objects.get(pk=processo_id)
            processo.delete()
            return JsonResponse({'message': 'Processo excluído com sucesso!'})
        except Processo.DoesNotExist:
            return JsonResponse({'error': 'Processo não encontrado'}, status=404)

#---------------------------------------------------------------------

# CRIAR ESTABELECIMENTO
@method_decorator(csrf_exempt, name='dispatch')
class EstabelecimentoCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            estabelecimento = Estabelecimento.objects.create(
                nome_do_estabelecimento=data.get('nome_do_estabelecimento'),
                local_do_estabelecimento_prisional=data.get('local_do_estabelecimento_prisional')
            )
            return JsonResponse({'message': 'Estabelecimento criado com sucesso!', 'estabelecimento_id': estabelecimento.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# LISTAR TODOS OS ESTABELECIMENTOS
class EstabelecimentoListView(View):
    def get(self, request):
        estabelecimentos = list(Estabelecimento.objects.values())
        return JsonResponse(estabelecimentos, safe=False)

# CONSULTAR ESTABELECIMENTO POR ID
class EstabelecimentoDetailView(View):
    def get(self, request, estabelecimento_id):
        try:
            estabelecimento = Estabelecimento.objects.get(pk=estabelecimento_id)
            return JsonResponse({
                'id': estabelecimento.id,
                'nome_do_estabelecimento': estabelecimento.nome_do_estabelecimento,
                'local_do_estabelecimento_prisional': estabelecimento.local_do_estabelecimento_prisional,
                'created_at': estabelecimento.created_at,
                'updated_at': estabelecimento.updated_at
            })
        except Estabelecimento.DoesNotExist:
            return JsonResponse({'error': 'Estabelecimento não encontrado'}, status=404)

# ATUALIZAR ESTABELECIMENTO
@method_decorator(csrf_exempt, name='dispatch')
class EstabelecimentoUpdateView(View):
    def post(self, request, estabelecimento_id):
        try:
            data = json.loads(request.body)
            estabelecimento = Estabelecimento.objects.get(pk=estabelecimento_id)
            estabelecimento.nome_do_estabelecimento = data.get('nome_do_estabelecimento', estabelecimento.nome_do_estabelecimento)
            estabelecimento.local_do_estabelecimento_prisional = data.get('local_do_estabelecimento_prisional', estabelecimento.local_do_estabelecimento_prisional)
            estabelecimento.save()
            return JsonResponse({'message': 'Estabelecimento atualizado com sucesso!'})
        except Estabelecimento.DoesNotExist:
            return JsonResponse({'error': 'Estabelecimento não encontrado'}, status=404)

# DELETAR ESTABELECIMENTO
@method_decorator(csrf_exempt, name='dispatch')
class EstabelecimentoDeleteView(View):
    def post(self, request, estabelecimento_id):
        try:
            estabelecimento = Estabelecimento.objects.get(pk=estabelecimento_id)
            estabelecimento.delete()
            return JsonResponse({'message': 'Estabelecimento excluído com sucesso!'})
        except Estabelecimento.DoesNotExist:
            return JsonResponse({'error': 'Estabelecimento não encontrado'}, status=404)

#---------------------------------------------------------------------

# CRIAR PERFIL
@method_decorator(csrf_exempt, name='dispatch')
class PerfilCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            perfil = Perfil.objects.create(
                tipo_de_perfil=data.get('tipo_de_perfil')
            )
            return JsonResponse({'message': 'Perfil criado com sucesso!', 'perfil_id': perfil.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# LISTAR TODOS OS PERFIS
class PerfilListView(View):
    def get(self, request):
        perfis = list(Perfil.objects.values())
        return JsonResponse(perfis, safe=False)

# CONSULTAR PERFIL POR ID
class PerfilDetailView(View):
    def get(self, request, perfil_id):
        try:
            perfil = Perfil.objects.get(pk=perfil_id)
            return JsonResponse({
                'id': perfil.id,
                'tipo_de_perfil': perfil.tipo_de_perfil,
                'created_at': perfil.created_at,
                'updated_at': perfil.updated_at
            })
        except Perfil.DoesNotExist:
            return JsonResponse({'error': 'Perfil não encontrado'}, status=404)

# ATUALIZAR PERFIL
@method_decorator(csrf_exempt, name='dispatch')
class PerfilUpdateView(View):
    def post(self, request, perfil_id):
        try:
            data = json.loads(request.body)
            perfil = Perfil.objects.get(pk=perfil_id)
            perfil.tipo_de_perfil = data.get('tipo_de_perfil', perfil.tipo_de_perfil)
            perfil.save()
            return JsonResponse({'message': 'Perfil atualizado com sucesso!'})
        except Perfil.DoesNotExist:
            return JsonResponse({'error': 'Perfil não encontrado'}, status=404)

# DELETAR PERFIL
@method_decorator(csrf_exempt, name='dispatch')
class PerfilDeleteView(View):
    def post(self, request, perfil_id):
        try:
            perfil = Perfil.objects.get(pk=perfil_id)
            perfil.delete()
            return JsonResponse({'message': 'Perfil excluído com sucesso!'})
        except Perfil.DoesNotExist:
            return JsonResponse({'error': 'Perfil não encontrado'}, status=404)

#---------------------------------------------------------------------

# CRIAR REGRA DE CUMPRIMENTO DE PENA
@method_decorator(csrf_exempt, name='dispatch')
class RegraCumprimentoPenaCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            regra = RegraCumprimentoPena.objects.create(
                tipo_regime=data.get('tipo_regime')
            )
            return JsonResponse({'message': 'Regra de Cumprimento de Pena criada com sucesso!', 'regra_id': regra.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# LISTAR TODAS AS REGRAS
class RegraCumprimentoPenaListView(View):
    def get(self, request):
        regras = list(RegraCumprimentoPena.objects.values())
        return JsonResponse(regras, safe=False)

# CONSULTAR REGRA POR ID
class RegraCumprimentoPenaDetailView(View):
    def get(self, request, regra_id):
        try:
            regra = RegraCumprimentoPena.objects.get(pk=regra_id)
            return JsonResponse({
                'id': regra.id,
                'tipo_regime': regra.tipo_regime,
                'created_at': regra.created_at,
                'updated_at': regra.updated_at
            })
        except RegraCumprimentoPena.DoesNotExist:
            return JsonResponse({'error': 'Regra de Cumprimento de Pena não encontrada'}, status=404)

# ATUALIZAR REGRA DE CUMPRIMENTO DE PENA
@method_decorator(csrf_exempt, name='dispatch')
class RegraCumprimentoPenaUpdateView(View):
    def post(self, request, regra_id):
        try:
            data = json.loads(request.body)
            regra = RegraCumprimentoPena.objects.get(pk=regra_id)
            regra.tipo_regime = data.get('tipo_regime', regra.tipo_regime)
            regra.save()
            return JsonResponse({'message': 'Regra de Cumprimento de Pena atualizada com sucesso!'})
        except RegraCumprimentoPena.DoesNotExist:
            return JsonResponse({'error': 'Regra de Cumprimento de Pena não encontrada'}, status=404)

# DELETAR REGRA DE CUMPRIMENTO DE PENA
@method_decorator(csrf_exempt, name='dispatch')
class RegraCumprimentoPenaDeleteView(View):
    def post(self, request, regra_id):
        try:
            regra = RegraCumprimentoPena.objects.get(pk=regra_id)
            regra.delete()
            return JsonResponse({'message': 'Regra de Cumprimento de Pena excluída com sucesso!'})
        except RegraCumprimentoPena.DoesNotExist:
            return JsonResponse({'error': 'Regra de Cumprimento de Pena não encontrada'}, status=404)

#---------------------------------------------------------------------

# CRIAR FACÇÃO
@method_decorator(csrf_exempt, name='dispatch')
class FaccaoCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            faccao = Faccao.objects.create(
                nome_faccao=data.get('nome_faccao'),
                local_faccao=data.get('local_faccao')
            )
            return JsonResponse({'message': 'Facção criada com sucesso!', 'faccao_id': faccao.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# LISTAR TODAS AS FACÇÕES
class FaccaoListView(View):
    def get(self, request):
        faccoes = list(Faccao.objects.values())
        return JsonResponse(faccoes, safe=False)

# CONSULTAR FACÇÃO POR ID
class FaccaoDetailView(View):
    def get(self, request, faccao_id):
        try:
            faccao = Faccao.objects.get(pk=faccao_id)
            return JsonResponse({
                'id': faccao.id,
                'nome_faccao': faccao.nome_faccao,
                'local_faccao': faccao.local_faccao,
                'created_at': faccao.created_at,
                'updated_at': faccao.updated_at
            })
        except Faccao.DoesNotExist:
            return JsonResponse({'error': 'Facção não encontrada'}, status=404)

# ATUALIZAR FACÇÃO
@method_decorator(csrf_exempt, name='dispatch')
class FaccaoUpdateView(View):
    def post(self, request, faccao_id):
        try:
            data = json.loads(request.body)
            faccao = Faccao.objects.get(pk=faccao_id)
            faccao.nome_faccao = data.get('nome_faccao', faccao.nome_faccao)
            faccao.local_faccao = data.get('local_faccao', faccao.local_faccao)
            faccao.save()
            return JsonResponse({'message': 'Facção atualizada com sucesso!'})
        except Faccao.DoesNotExist:
            return JsonResponse({'error': 'Facção não encontrada'}, status=404)

# DELETAR FACÇÃO
@method_decorator(csrf_exempt, name='dispatch')
class FaccaoDeleteView(View):
    def post(self, request, faccao_id):
        try:
            faccao = Faccao.objects.get(pk=faccao_id)
            faccao.delete()
            return JsonResponse({'message': 'Facção excluída com sucesso!'})
        except Faccao.DoesNotExist:
            return JsonResponse({'error': 'Facção não encontrada'}, status=404)

#---------------------------------------------------------------------

# CRIAR SITUAÇÃO TRABALHISTA
@method_decorator(csrf_exempt, name='dispatch')
class SituacaoTrabalhistaCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            situacao = SituacaoTrabalhista.objects.create(
                nome_empresa=data.get('nome_empresa'),
                cargo_empresa=data.get('cargo_empresa'),
                inicio_da_jornada_trabalho=data.get('inicio_da_jornada_trabalho'),
                termino_da_jornada_trabalho=data.get('termino_da_jornada_trabalho'),
                inicio_do_contrato_trabalho=data.get('inicio_do_contrato_trabalho'),
                termino_do_contrato_trabalho=data.get('termino_do_contrato_trabalho'),
                contato_empresa=data.get('contato_empresa'),
                responsavel=data.get('responsavel')
            )
            return JsonResponse({'message': 'Situação trabalhista criada com sucesso!', 'situacao_id': situacao.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# LISTAR TODAS AS SITUAÇÕES TRABALHISTAS
class SituacaoTrabalhistaListView(View):
    def get(self, request):
        situacoes = list(SituacaoTrabalhista.objects.values())
        return JsonResponse(situacoes, safe=False)

# CONSULTAR SITUAÇÃO TRABALHISTA POR ID
class SituacaoTrabalhistaDetailView(View):
    def get(self, request, situacao_id):
        try:
            situacao = SituacaoTrabalhista.objects.get(pk=situacao_id)
            return JsonResponse({
                'id': situacao.id,
                'nome_empresa': situacao.nome_empresa,
                'cargo_empresa': situacao.cargo_empresa,
                'inicio_da_jornada_trabalho': situacao.inicio_da_jornada_trabalho,
                'termino_da_jornada_trabalho': situacao.termino_da_jornada_trabalho,
                'inicio_do_contrato_trabalho': situacao.inicio_do_contrato_trabalho,
                'termino_do_contrato_trabalho': situacao.termino_do_contrato_trabalho,
                'contato_empresa': situacao.contato_empresa,
                'responsavel': situacao.responsavel,
                'created_at': situacao.created_at,
                'updated_at': situacao.updated_at
            })
        except SituacaoTrabalhista.DoesNotExist:
            return JsonResponse({'error': 'Situação trabalhista não encontrada'}, status=404)

# ATUALIZAR SITUAÇÃO TRABALHISTA
@method_decorator(csrf_exempt, name='dispatch')
class SituacaoTrabalhistaUpdateView(View):
    def post(self, request, situacao_id):
        try:
            data = json.loads(request.body)
            situacao = SituacaoTrabalhista.objects.get(pk=situacao_id)
            situacao.nome_empresa = data.get('nome_empresa', situacao.nome_empresa)
            situacao.cargo_empresa = data.get('cargo_empresa', situacao.cargo_empresa)
            situacao.inicio_da_jornada_trabalho = data.get('inicio_da_jornada_trabalho', situacao.inicio_da_jornada_trabalho)
            situacao.termino_da_jornada_trabalho = data.get('termino_da_jornada_trabalho', situacao.termino_da_jornada_trabalho)
            situacao.inicio_do_contrato_trabalho = data.get('inicio_do_contrato_trabalho', situacao.inicio_do_contrato_trabalho)
            situacao.termino_do_contrato_trabalho = data.get('termino_do_contrato_trabalho', situacao.termino_do_contrato_trabalho)
            situacao.contato_empresa = data.get('contato_empresa', situacao.contato_empresa)
            situacao.responsavel = data.get('responsavel', situacao.responsavel)
            situacao.save()
            return JsonResponse({'message': 'Situação trabalhista atualizada com sucesso!'})
        except SituacaoTrabalhista.DoesNotExist:
            return JsonResponse({'error': 'Situação trabalhista não encontrada'}, status=404)

# DELETAR SITUAÇÃO TRABALHISTA
@method_decorator(csrf_exempt, name='dispatch')
class SituacaoTrabalhistaDeleteView(View):
    def post(self, request, situacao_id):
        try:
            situacao = SituacaoTrabalhista.objects.get(pk=situacao_id)
            situacao.delete()
            return JsonResponse({'message': 'Situação trabalhista excluída com sucesso!'})
        except SituacaoTrabalhista.DoesNotExist:
            return JsonResponse({'error': 'Situação trabalhista não encontrada'}, status=404)

#---------------------------------------------------------------------

# CRIAR ZONA
@method_decorator(csrf_exempt, name='dispatch')
class ZonaCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            zona = Zona.objects.create(
                tipo_zona=data.get('tipo_zona'),
                regras_zona=data.get('regras_zona'),
                endereco_zona=data.get('endereco_zona'),
                observacoes=data.get('observacoes'),
                vigencia_inicial_da_zona=data.get('vigencia_inicial_da_zona'),
                vigencia_final_da_zona=data.get('vigencia_final_da_zona', None),
                tipo_area=data.get('tipo_area'),
                regras_horario=data.get('regras_horario', ''),
                operador_registro=data.get('operador_registro'),
                operador_edit_registro=data.get('operador_edit_registro', 1),
                ativa=data.get('ativa'),
                horario_zona=data.get('horario_zona')
            )
            return JsonResponse({'message': 'Zona criada com sucesso!', 'zona_id': zona.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# LISTAR TODAS AS ZONAS
class ZonaListView(View):
    def get(self, request):
        zonas = list(Zona.objects.values())
        return JsonResponse(zonas, safe=False)

# CONSULTAR ZONA POR ID
class ZonaDetailView(View):
    def get(self, request, zona_id):
        try:
            zona = Zona.objects.get(pk=zona_id)
            return JsonResponse({
                'id': zona.id,
                'tipo_zona': zona.tipo_zona,
                'regras_zona': zona.regras_zona,
                'endereco_zona': zona.endereco_zona,
                'observacoes': zona.observacoes,
                'vigencia_inicial_da_zona': zona.vigencia_inicial_da_zona,
                'vigencia_final_da_zona': zona.vigencia_final_da_zona,
                'tipo_area': zona.tipo_area,
                'regras_horario': zona.regras_horario,
                'operador_registro': zona.operador_registro,
                'operador_edit_registro': zona.operador_edit_registro,
                'ativa': zona.ativa,
                'horario_zona': zona.horario_zona,
                'created_at': zona.created_at,
                'updated_at': zona.updated_at
            })
        except Zona.DoesNotExist:
            return JsonResponse({'error': 'Zona não encontrada'}, status=404)

# ATUALIZAR ZONA
@method_decorator(csrf_exempt, name='dispatch')
class ZonaUpdateView(View):
    def post(self, request, zona_id):
        try:
            data = json.loads(request.body)
            zona = Zona.objects.get(pk=zona_id)
            zona.tipo_zona = data.get('tipo_zona', zona.tipo_zona)
            zona.regras_zona = data.get('regras_zona', zona.regras_zona)
            zona.endereco_zona = data.get('endereco_zona', zona.endereco_zona)
            zona.observacoes = data.get('observacoes', zona.observacoes)
            zona.vigencia_inicial_da_zona = data.get('vigencia_inicial_da_zona', zona.vigencia_inicial_da_zona)
            zona.vigencia_final_da_zona = data.get('vigencia_final_da_zona', zona.vigencia_final_da_zona)
            zona.tipo_area = data.get('tipo_area', zona.tipo_area)
            zona.regras_horario = data.get('regras_horario', zona.regras_horario)
            zona.operador_registro = data.get('operador_registro', zona.operador_registro)
            zona.operador_edit_registro = data.get('operador_edit_registro', zona.operador_edit_registro)
            zona.ativa = data.get('ativa', zona.ativa)
            zona.horario_zona = data.get('horario_zona', zona.horario_zona)
            zona.save()
            return JsonResponse({'message': 'Zona atualizada com sucesso!'})
        except Zona.DoesNotExist:
            return JsonResponse({'error': 'Zona não encontrada'}, status=404)

# DELETAR ZONA
@method_decorator(csrf_exempt, name='dispatch')
class ZonaDeleteView(View):
    def post(self, request, zona_id):
        try:
            zona = Zona.objects.get(pk=zona_id)
            zona.delete()
            return JsonResponse({'message': 'Zona excluída com sucesso!'})
        except Zona.DoesNotExist:
            return JsonResponse({'error': 'Zona não encontrada'}, status=404)

#---------------------------------------------------------------------

# CRIAR DADOS DE RASTREAMENTO
@method_decorator(csrf_exempt, name='dispatch')
class TrackingDataCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            tracking_data = TrackingData.objects.create(
                coordenadas_geograficas=data.get('coordenadas_geograficas'),
                LBS=data.get('LBS'),
                status_feixe_luz=data.get('status_feixe_luz'),
                deteccao_de_jamming=data.get('deteccao_de_jamming'),
                deteccao_de_violacao_de_caixa=data.get('deteccao_de_violacao_de_caixa'),
                altura=data.get('altura'),
                velocidade=data.get('velocidade'),
                VDOP=data.get('VDOP'),
                HDOP=data.get('HDOP'),
                qualidade_satelite=data.get('qualidade_satelite'),
                nivel_bateria=data.get('nivel_bateria'),
                e_sim_card=data.get('e_sim_card'),
                inercia=data.get('inercia'),
                qualidade_GPRS=data.get('qualidade_GPRS')
            )
            return JsonResponse({'message': 'TrackingData criada com sucesso!', 'tracking_id': tracking_data.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# LISTAR TODOS OS DADOS DE RASTREAMENTO
class TrackingDataListView(View):
    def get(self, request):
        tracking_data_list = list(TrackingData.objects.values())
        return JsonResponse(tracking_data_list, safe=False)

# CONSULTAR DADOS DE RASTREAMENTO POR ID
class TrackingDataDetailView(View):
    def get(self, request, tracking_id):
        try:
            tracking_data = TrackingData.objects.get(pk=tracking_id)
            return JsonResponse({
                'id': tracking_data.id,
                'coordenadas_geograficas': tracking_data.coordenadas_geograficas,
                'LBS': tracking_data.LBS,
                'status_feixe_luz': tracking_data.status_feixe_luz,
                'deteccao_de_jamming': tracking_data.deteccao_de_jamming,
                'deteccao_de_violacao_de_caixa': tracking_data.deteccao_de_violacao_de_caixa,
                'altura': tracking_data.altura,
                'velocidade': tracking_data.velocidade,
                'VDOP': tracking_data.VDOP,
                'HDOP': tracking_data.HDOP,
                'qualidade_satelite': tracking_data.qualidade_satelite,
                'nivel_bateria': tracking_data.nivel_bateria,
                'e_sim_card': tracking_data.e_sim_card,
                'inercia': tracking_data.inercia,
                'qualidade_GPRS': tracking_data.qualidade_GPRS,
                'created_at': tracking_data.created_at,
                'updated_at': tracking_data.updated_at
            })
        except TrackingData.DoesNotExist:
            return JsonResponse({'error': 'TrackingData não encontrada'}, status=404)

# ATUALIZAR DADOS DE RASTREAMENTO
@method_decorator(csrf_exempt, name='dispatch')
class TrackingDataUpdateView(View):
    def post(self, request, tracking_id):
        try:
            data = json.loads(request.body)
            tracking_data = TrackingData.objects.get(pk=tracking_id)
            tracking_data.coordenadas_geograficas = data.get('coordenadas_geograficas', tracking_data.coordenadas_geograficas)
            tracking_data.LBS = data.get('LBS', tracking_data.LBS)
            tracking_data.status_feixe_luz = data.get('status_feixe_luz', tracking_data.status_feixe_luz)
            tracking_data.deteccao_de_jamming = data.get('deteccao_de_jamming', tracking_data.deteccao_de_jamming)
            tracking_data.deteccao_de_violacao_de_caixa = data.get('deteccao_de_violacao_de_caixa', tracking_data.deteccao_de_violacao_de_caixa)
            tracking_data.altura = data.get('altura', tracking_data.altura)
            tracking_data.velocidade = data.get('velocidade', tracking_data.velocidade)
            tracking_data.VDOP = data.get('VDOP', tracking_data.VDOP)
            tracking_data.HDOP = data.get('HDOP', tracking_data.HDOP)
            tracking_data.qualidade_satelite = data.get('qualidade_satelite', tracking_data.qualidade_satelite)
            tracking_data.nivel_bateria = data.get('nivel_bateria', tracking_data.nivel_bateria)
            tracking_data.e_sim_card = data.get('e_sim_card', tracking_data.e_sim_card)
            tracking_data.inercia = data.get('inercia', tracking_data.inercia)
            tracking_data.qualidade_GPRS = data.get('qualidade_GPRS', tracking_data.qualidade_GPRS)
            tracking_data.save()
            return JsonResponse({'message': 'TrackingData atualizada com sucesso!'})
        except TrackingData.DoesNotExist:
            return JsonResponse({'error': 'TrackingData não encontrada'}, status=404)

# DELETAR DADOS DE RASTREAMENTO
@method_decorator(csrf_exempt, name='dispatch')
class TrackingDataDeleteView(View):
    def post(self, request, tracking_id):
        try:
            tracking_data = TrackingData.objects.get(pk=tracking_id)
            tracking_data.delete()
            return JsonResponse({'message': 'TrackingData excluída com sucesso!'})
        except TrackingData.DoesNotExist:
            return JsonResponse({'error': 'TrackingData não encontrada'}, status=404)

#---------------------------------------------------------------------



#---------------------------------------------------------------------


