import json
import pymysql
from datetime import datetime

# Função para carregar a lista de SIMCODEs de um arquivo JSON
def load_simcodes_from_json(json_file):
    with open(json_file, 'r') as f:
        simcodes = json.load(f)
    return simcodes

# Função para inserir dados no banco de dados MySQL
def insert_gps_ts_bulk(simcodes, connection):
    try:
        with connection.cursor() as cursor:
            # Query para inserção de dados em lote
            sql = """
                INSERT INTO gps_t_s (SIMCODE, cod_detec, status, created_at, updated_at) 
                VALUES (%s, %s, %s, NOW(), NOW())
            """
            # Preparando dados para inserção em lote
            bulk_data = [(simcode, simcode, 1) for simcode in simcodes]
            cursor.executemany(sql, bulk_data)
        connection.commit()
    except Exception as e:
        print(f"Erro ao inserir no banco de dados: {e}")

# Função principal para carregar os SIMCODEs do JSON e inserir no banco de dados
def main():
    # Carregar o arquivo JSON
    json_file = 'device_ids.json'  # Substitua pelo caminho do arquivo JSON
    simcodes = load_simcodes_from_json(json_file)

    # Conectar ao banco de dados MySQL
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='123456789',
        database='dataHeader',
        port=3306
    )

    try:
        # Inserir os dados no banco de dados
        insert_gps_ts_bulk(simcodes, connection)
        print("Dados inseridos com sucesso.")
    
    finally:
        connection.close()

# Executar o script
if __name__ == "__main__":
    main()
