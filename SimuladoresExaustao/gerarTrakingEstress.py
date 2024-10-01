import random
import time
import pymysql
from datetime import datetime
import json

# Carregar a lista de IDs de dispositivos a partir de um arquivo JSON
def load_device_ids():
    with open('device_ids.json', 'r') as f:
        device_ids = json.load(f)
    return device_ids

# Função para inserir dados em lote no banco de dados MySQL
def insert_into_db_bulk(data, connection):
    try:
        with connection.cursor() as cursor:
            # Query para inserção de dados em lote
            sql = "INSERT INTO headers (SIMCODE, headers, created_at, updated_at) VALUES (%s, %s, NOW(), NOW())"
            cursor.executemany(sql, data)
        connection.commit()
    except Exception as e:
        print(f"Erro ao inserir no banco de dados: {e}")

# Função para gerar os dados para todos os dispositivos
def generate_data():
    # Carregar os IDs de dispositivos a partir do JSON
    device_ids = load_device_ids()

    # Criar uma conexão persistente com o banco de dados
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='123456789',
        database='dataHeader',
        port=3306
    )

    try:
        while True:
            start_time = time.time()

            # Lista para armazenar os dados de todos os dispositivos
            bulk_data = []

            # Gerar e acumular dados para todos os dispositivos
            for id_dispositivo in device_ids:
                
                # Gerando coordenadas geográficas de exemplo (latitude e longitude)
                altitude = round(random.uniform(-90.0, 90.0), 6)
                longitude = round(random.uniform(-180.0, 180.0), 6)

                # Gerando data e hora atual
                data_envio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Gerando velocidade (S) como um número inteiro entre 0 e 100
                speed = random.randint(0, 100)

                # Gerando bateria (número inteiro entre 0 e 10)
                bateria = random.randint(0, 10)

                # Gerando variáveis V1 a V5 como 0 ou 1
                val01 = random.randint(0, 1)
                val02 = random.randint(0, 1)
                val03 = random.randint(0, 1)
                val04 = random.randint(0, 1)
                val05 = random.randint(0, 1)

                # Gerando P como 0 ou 1
                p = random.randint(0, 1)

                # Montando a string no formato solicitado
                data_string = (f"ID:{id_dispositivo};CORD:{altitude}, {longitude}; DATE:{data_envio}; "
                               f"S:{speed}; {bateria}; V1:{val01}; V2:{val02}; V3:{val03}; V4:{val04}; V5:{val05};P:{p}")

                # SIMCODE sempre igual a 0
                simcode = 0

                # Adicionar os dados à lista para inserção em lote
                bulk_data.append((simcode, data_string))

            # Inserindo os dados de todos os dispositivos no banco de dados em lote
            insert_into_db_bulk(bulk_data, connection)

            # Calcular o tempo de execução em milissegundos e segundos
            time_taken = time.time() - start_time
            time_taken_ms = time_taken * 1000  # Convertendo para milissegundos

            print(f'Envio concluído para {len(device_ids)} dispositivos em {time_taken:.2f} segundos ({time_taken_ms:.0f} ms)')

            # Esperar antes do próximo ciclo
            time.sleep(10)  # Pausa por 60 segundos

    finally:
        connection.close()

# Executando a função
generate_data()
