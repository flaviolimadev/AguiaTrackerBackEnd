import random
import time
import mysql.connector
from mysql.connector import pooling
from datetime import datetime
import json

# Configuração do pool de conexões MySQL com charset e collation
dbconfig = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "123456789",
    "database": "dataHeader",
    "charset": "utf8mb4",  # Definir charset compatível
    "collation": "utf8mb4_general_ci"  # Definir collation suportada
}

pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=10, **dbconfig)

# Carregar a lista de IDs de dispositivos a partir de um arquivo JSON
def load_device_ids():
    with open('device_ids.json', 'r') as f:
        device_ids = json.load(f)
    return device_ids

# Função para inserir dados em lote no banco de dados MySQL
def insert_into_db_bulk(data):
    connection = pool.get_connection()  # Pegar uma conexão do pool
    try:
        cursor = connection.cursor()
        # Query para inserção de dados em lote
        sql = "INSERT INTO headers (SIMCODE, headers, created_at, updated_at) VALUES (%s, %s, NOW(), NOW())"
        cursor.executemany(sql, data)
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao inserir no banco de dados: {e}")
    finally:
        connection.close()

# Função para gerar os dados para todos os dispositivos
def generate_data():
    # Carregar os IDs de dispositivos a partir do JSON
    device_ids = load_device_ids()

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
            insert_into_db_bulk(bulk_data)

            # Calcular o tempo de execução em milissegundos e segundos
            time_taken = time.time() - start_time
            time_taken_ms = time_taken * 1000  # Convertendo para milissegundos

            print(f'Envio concluído para 40000 dispositivos em {time_taken:.2f} segundos ({time_taken_ms:.0f} ms)')

            # Esperar antes do próximo ciclo
            time.sleep(15)  # Pausa por 60 segundos

    finally:
        print("Concluído.")

# Executando a função
generate_data()
