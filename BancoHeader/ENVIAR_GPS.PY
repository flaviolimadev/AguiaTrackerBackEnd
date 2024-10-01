import os
import json
import random
import time
import pymysql
from datetime import datetime

# Função para gerar coordenadas aleatórias (latitude e longitude)
def gerar_coordenadas():
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    return f"{latitude:.6f}/{longitude:.6f}"

# Função para verificar e processar eventos
def verificar_eventos(dados):
    eventos = dados.get("EVENTOS", {})
    alteracoes = []
    
    for evento_id, evento_info in eventos.items():
        for evento_nome, evento_detalhes in evento_info.items():
            if not dados.get(evento_nome):  # Se o evento está como False no JSON principal
                alteracao = f"{evento_nome};R:{evento_detalhes['R']};G:{evento_detalhes['G']};B:{evento_detalhes['B']};VB:{evento_detalhes['VIBRACAO']};BU:{evento_detalhes['BUZZER']}"
                alteracoes.append(alteracao)
    
    return alteracoes

# Função para ler e processar os arquivos JSON
def ler_arquivos_json(pasta, connection):
    arquivos = [f for f in os.listdir(pasta) if f.endswith('.json')]
    
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(pasta, arquivo)
        
        with open(caminho_arquivo, 'r') as f:
            dados = json.load(f)
        
        id_dispositivo = dados.get("ID")
        coordenadas = gerar_coordenadas()
        bateria = dados.get("BATERIA")
        gps = dados.get("GPS", {})
        data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        gps_string = f"{gps.get('G', 0)}/{gps.get('B', 0)}/{gps.get('S', 0)}"
        
        # Verificar eventos e adicionar alterações, se houver
        alteracoes_eventos = verificar_eventos(dados)
        
        if alteracoes_eventos:
            for alteracao in alteracoes_eventos:
                headers_string = f"{id_dispositivo}/{coordenadas}/{bateria}/{gps_string}/{data_atual}&&{alteracao}"
                inserir_no_banco(headers_string, connection)
        else:
            headers_string = f"{id_dispositivo}/{coordenadas}/{bateria}/{gps_string}/{data_atual}"
            inserir_no_banco(headers_string, connection)

# Função para inserir no banco de dados
def inserir_no_banco(headers_string, connection):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO headers (headers, created_at, updated_at) VALUES (%s, NOW(), NOW())"
            cursor.execute(sql, (headers_string,))
        connection.commit()
    except Exception as e:
        print(f"Erro ao inserir no banco de dados: {e}")

# Função principal que executa o simulador
def simulador_gps():
    pasta = './GPS'  # Caminho da pasta onde estão os arquivos JSON
    
    # Conectar ao banco de dados
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='123456789',
        database='dataHeader',
        port=3306
    )
    
    try:
        while True:
            ler_arquivos_json(pasta, connection)
            time.sleep(10)  # Espera de 10 segundos entre cada leitura
    finally:
        connection.close()

# Executa o simulador
if __name__ == "__main__":
    simulador_gps()
