from django.urls import path
from . import views
from .views import UserCreateView, UserListView, UserDetailView, UserUpdateView, UserDeleteView
from .views import MonitoradoCreateView, MonitoradoListView, MonitoradoDetailView, MonitoradoUpdateView, MonitoradoDeleteView
from .views import DispositivoCreateView, DispositivoListView, DispositivoDetailView, DispositivoUpdateView, DispositivoDeleteView
from .views import FotoCreateView, FotoListView, FotoDetailView, FotoUpdateView, FotoDeleteView
from .views import ArquivoCreateView, ArquivoListView, ArquivoDetailView, ArquivoUpdateView, ArquivoDeleteView
from .views import TelefoneCreateView, TelefoneListView, TelefoneDetailView, TelefoneUpdateView, TelefoneDeleteView
from .views import ProcessoCreateView, ProcessoListView, ProcessoDetailView, ProcessoUpdateView, ProcessoDeleteView
from .views import EstabelecimentoCreateView, EstabelecimentoListView, EstabelecimentoDetailView, EstabelecimentoUpdateView, EstabelecimentoDeleteView
from .views import PerfilCreateView, PerfilListView, PerfilDetailView, PerfilUpdateView, PerfilDeleteView
from .views import RegraCumprimentoPenaCreateView, RegraCumprimentoPenaListView, RegraCumprimentoPenaDetailView, RegraCumprimentoPenaUpdateView, RegraCumprimentoPenaDeleteView
from .views import SituacaoTrabalhistaCreateView, SituacaoTrabalhistaListView, SituacaoTrabalhistaDetailView, SituacaoTrabalhistaUpdateView, SituacaoTrabalhistaDeleteView
from .views import FaccaoCreateView, FaccaoListView, FaccaoDetailView, FaccaoUpdateView, FaccaoDeleteView
from .views import ZonaCreateView, ZonaListView, ZonaDetailView, ZonaUpdateView, ZonaDeleteView
from .views import TrackingDataCreateView, TrackingDataListView, TrackingDataDetailView, TrackingDataUpdateView, TrackingDataDeleteView


urlpatterns = [

    #Rotas de Teste dos Models;
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('monitorados/', views.lista_monitorados, name='lista_monitorados'),
    path('dispositivos/', views.lista_dispositivos, name='lista_dispositivos'),
    path('fotos/', views.lista_fotos, name='lista_fotos'),
    path('arquivos/', views.lista_arquivos, name='lista_arquivos'),
    path('telefones/', views.lista_telefones, name='lista_telefones'),
    path('processos/', views.lista_processos, name='lista_processos'),
    path('estabelecimento/', views.lista_estabelecimento, name='lista_estabelecimento'),
    path('perfil/', views.lista_perfil, name='lista_perfil'),
    path('regras-cumprimento-pena/', views.lista_regra_cumprimento_pena, name='lista_regra_cumprimento_pena'),
    path('faccoes/', views.lista_faccao, name='lista_faccao'),
    path('situacao-trabalhista/', views.lista_situacao_trabalhista, name='lista_situacao_trabalhista'),
    path('zonas/', views.lista_zona, name='lista_zona'),
    path('tracking-data/', views.lista_tracking_data, name='lista_tracking_data'),


    #Rodas Crud User;
    path('usuarios/criar/', UserCreateView.as_view(), name='criar_usuario'),
    path('usuarios/', UserListView.as_view(), name='lista_usuarios'),
    path('usuarios/<int:user_id>/', UserDetailView.as_view(), name='detalhe_usuario'),
    path('usuarios/atualizar/<int:user_id>/', UserUpdateView.as_view(), name='atualizar_usuario'),
    path('usuarios/deletar/<int:user_id>/', UserDeleteView.as_view(), name='deletar_usuario'),

    #Rodas Crud Monitorado;
    path('monitorados/criar/', MonitoradoCreateView.as_view(), name='criar_monitorado'),
    path('monitorados/', MonitoradoListView.as_view(), name='lista_monitorados'),
    path('monitorados/<int:monitorado_id>/', MonitoradoDetailView.as_view(), name='detalhe_monitorado'),
    path('monitorados/atualizar/<int:monitorado_id>/', MonitoradoUpdateView.as_view(), name='atualizar_monitorado'),
    path('monitorados/deletar/<int:monitorado_id>/', MonitoradoDeleteView.as_view(), name='deletar_monitorado'),

    #Rodas Crud Dispositivo;
    path('dispositivos/criar/', DispositivoCreateView.as_view(), name='criar_dispositivo'),
    path('dispositivos/', DispositivoListView.as_view(), name='lista_dispositivos'),
    path('dispositivos/<int:dispositivo_id>/', DispositivoDetailView.as_view(), name='detalhe_dispositivo'),
    path('dispositivos/atualizar/<int:dispositivo_id>/', DispositivoUpdateView.as_view(), name='atualizar_dispositivo'),
    path('dispositivos/deletar/<int:dispositivo_id>/', DispositivoDeleteView.as_view(), name='deletar_dispositivo'),

    #Rodas Crud Foto;
    path('fotos/criar/', FotoCreateView.as_view(), name='criar_foto'),
    path('fotos/', FotoListView.as_view(), name='lista_fotos'),
    path('fotos/<int:foto_id>/', FotoDetailView.as_view(), name='detalhe_foto'),
    path('fotos/atualizar/<int:foto_id>/', FotoUpdateView.as_view(), name='atualizar_foto'),
    path('fotos/deletar/<int:foto_id>/', FotoDeleteView.as_view(), name='deletar_foto'),

    #Rodas Crud Arquivo;
    path('arquivos/criar/', ArquivoCreateView.as_view(), name='criar_arquivo'),
    path('arquivos/', ArquivoListView.as_view(), name='lista_arquivos'),
    path('arquivos/<int:arquivo_id>/', ArquivoDetailView.as_view(), name='detalhe_arquivo'),
    path('arquivos/atualizar/<int:arquivo_id>/', ArquivoUpdateView.as_view(), name='atualizar_arquivo'),
    path('arquivos/deletar/<int:arquivo_id>/', ArquivoDeleteView.as_view(), name='deletar_arquivo'),

    #Rodas Crud Telefone;
    path('telefones/criar/', TelefoneCreateView.as_view(), name='criar_telefone'),
    path('telefones/', TelefoneListView.as_view(), name='lista_telefones'),
    path('telefones/<int:telefone_id>/', TelefoneDetailView.as_view(), name='detalhe_telefone'),
    path('telefones/atualizar/<int:telefone_id>/', TelefoneUpdateView.as_view(), name='atualizar_telefone'),
    path('telefones/deletar/<int:telefone_id>/', TelefoneDeleteView.as_view(), name='deletar_telefone'),

    #Rodas Crud Processo;
    path('processos/criar/', ProcessoCreateView.as_view(), name='criar_processo'),
    path('processos/', ProcessoListView.as_view(), name='lista_processos'),
    path('processos/<int:processo_id>/', ProcessoDetailView.as_view(), name='detalhe_processo'),
    path('processos/atualizar/<int:processo_id>/', ProcessoUpdateView.as_view(), name='atualizar_processo'),
    path('processos/deletar/<int:processo_id>/', ProcessoDeleteView.as_view(), name='deletar_processo'),

    #Rodas Crud Estabelecimento;
    path('estabelecimentos/criar/', EstabelecimentoCreateView.as_view(), name='criar_estabelecimento'),
    path('estabelecimentos/', EstabelecimentoListView.as_view(), name='lista_estabelecimentos'),
    path('estabelecimentos/<int:estabelecimento_id>/', EstabelecimentoDetailView.as_view(), name='detalhe_estabelecimento'),
    path('estabelecimentos/atualizar/<int:estabelecimento_id>/', EstabelecimentoUpdateView.as_view(), name='atualizar_estabelecimento'),
    path('estabelecimentos/deletar/<int:estabelecimento_id>/', EstabelecimentoDeleteView.as_view(), name='deletar_estabelecimento'),

    #Rodas Crud Perfil;
    path('perfis/criar/', PerfilCreateView.as_view(), name='criar_perfil'),
    path('perfis/', PerfilListView.as_view(), name='lista_perfis'),
    path('perfis/<int:perfil_id>/', PerfilDetailView.as_view(), name='detalhe_perfil'),
    path('perfis/atualizar/<int:perfil_id>/', PerfilUpdateView.as_view(), name='atualizar_perfil'),
    path('perfis/deletar/<int:perfil_id>/', PerfilDeleteView.as_view(), name='deletar_perfil'),

    #Rodas Crud regras-cumprimento-pena;
    path('regras-cumprimento-pena/criar/', RegraCumprimentoPenaCreateView.as_view(), name='criar_regra_cumprimento_pena'),
    path('regras-cumprimento-pena/', RegraCumprimentoPenaListView.as_view(), name='lista_regras_cumprimento_pena'),
    path('regras-cumprimento-pena/<int:regra_id>/', RegraCumprimentoPenaDetailView.as_view(), name='detalhe_regra_cumprimento_pena'),
    path('regras-cumprimento-pena/atualizar/<int:regra_id>/', RegraCumprimentoPenaUpdateView.as_view(), name='atualizar_regra_cumprimento_pena'),
    path('regras-cumprimento-pena/deletar/<int:regra_id>/', RegraCumprimentoPenaDeleteView.as_view(), name='deletar_regra_cumprimento_pena'),

    #Rodas Crud Faccao;
    path('faccoes/criar/', FaccaoCreateView.as_view(), name='criar_faccao'),
    path('faccoes/', FaccaoListView.as_view(), name='lista_faccoes'),
    path('faccoes/<int:faccao_id>/', FaccaoDetailView.as_view(), name='detalhe_faccao'),
    path('faccoes/atualizar/<int:faccao_id>/', FaccaoUpdateView.as_view(), name='atualizar_faccao'),
    path('faccoes/deletar/<int:faccao_id>/', FaccaoDeleteView.as_view(), name='deletar_faccao'),

    #Rodas Crud Situacao Trabalhista;
    path('situacoes-trabalhistas/criar/', SituacaoTrabalhistaCreateView.as_view(), name='criar_situacao_trabalhista'),
    path('situacoes-trabalhistas/', SituacaoTrabalhistaListView.as_view(), name='lista_situacoes_trabalhistas'),
    path('situacoes-trabalhistas/<int:situacao_id>/', SituacaoTrabalhistaDetailView.as_view(), name='detalhe_situacao_trabalhista'),
    path('situacoes-trabalhistas/atualizar/<int:situacao_id>/', SituacaoTrabalhistaUpdateView.as_view(), name='atualizar_situacao_trabalhista'),
    path('situacoes-trabalhistas/deletar/<int:situacao_id>/', SituacaoTrabalhistaDeleteView.as_view(), name='deletar_situacao_trabalhista'),

    #Rodas Crud Zonas;
    path('zonas/criar/', ZonaCreateView.as_view(), name='criar_zona'),
    path('zonas/', ZonaListView.as_view(), name='lista_zonas'),
    path('zonas/<int:zona_id>/', ZonaDetailView.as_view(), name='detalhe_zona'),
    path('zonas/atualizar/<int:zona_id>/', ZonaUpdateView.as_view(), name='atualizar_zona'),
    path('zonas/deletar/<int:zona_id>/', ZonaDeleteView.as_view(), name='deletar_zona'),

    #Rodas Crud Traking;
    path('tracking-data/criar/', TrackingDataCreateView.as_view(), name='criar_tracking_data'),
    path('tracking-data/', TrackingDataListView.as_view(), name='lista_tracking_data'),
    path('tracking-data/<int:tracking_id>/', TrackingDataDetailView.as_view(), name='detalhe_tracking_data'),
    path('tracking-data/atualizar/<int:tracking_id>/', TrackingDataUpdateView.as_view(), name='atualizar_tracking_data'),
    path('tracking-data/deletar/<int:tracking_id>/', TrackingDataDeleteView.as_view(), name='deletar_tracking_data'),

]


