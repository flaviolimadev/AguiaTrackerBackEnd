from django.urls import path
from . import views
from .views import AdicionarUsuarioView 

urlpatterns = [
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('monitorados/', views.lista_monitorado, name='lista_monitorado'),
    path('adicionar_usuario/', AdicionarUsuarioView.as_view(), name='adicionar_usuario'),
]


