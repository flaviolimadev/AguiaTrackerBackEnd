import mysql.connector.pooling as pooling
import time  # Import necessário para a função sleep

# Configuração do pool de conexões MySQL
dbconfig = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "123456789",
    "database": "dataHeader",
    "charset": "utf8mb4",
    "collation": "utf8mb4_general_ci",  # Usar uma collation compatível
    "pool_name": "mypool",
    "pool_size": 20  # Aumente o pool_size para permitir mais conexões simultâneas
}

# Criar pool de conexões
pool = pooling.MySQLConnectionPool(**dbconfig)

# Função para definir a collation ao conectar-se
def set_collation(connection):
    with connection.cursor() as cursor:
        cursor.execute("SET NAMES 'utf8mb4' COLLATE 'utf8mb4_general_ci'")
        connection.commit()

# Função para obter uma conexão com tentativas de retry
def get_connection_with_retry(pool, retries=5, wait_time=1):
    for i in range(retries):
        try:
            return pool.get_connection()
        except Exception as e:
            print(f"Tentativa {i+1} falhou: {e}")
            time.sleep(wait_time)
    raise Exception("Falha ao obter conexão do pool após várias tentativas")

# Função para inserir múltiplos itens na tabela de ações em uma única query
def insert_actions_bulk(actions, connection):
    if not actions:
        return

    try:
        with connection.cursor() as cursor:
            # Inserindo todos os dados de uma vez (bulk insert)
            sql = """INSERT INTO log_actions (SIMCODE_ID, action_id, status, request, direction, count_resp, created_at, updated_at) 
                     VALUES (%s, %s, 0, '', 0, 0, NOW(), NOW())"""
            cursor.executemany(sql, actions)
    except Exception as e:
        print(f"Erro ao inserir ações: {e}")

# Função para atualizar múltiplos SIMCODEs em uma única query
def update_simcode_bulk(updates, connection):
    if not updates:
        return

    try:
        with connection.cursor() as cursor:
            # Atualizando todos os SIMCODEs de uma vez (bulk update)
            sql = "UPDATE headers SET SIMCODE = %s WHERE id = %s"
            cursor.executemany(sql, updates)
    except Exception as e:
        print(f"Erro ao atualizar SIMCODEs: {e}")

# Função para buscar registros com SIMCODE = 0 e processar as atualizações e inserções de ações
def update_simcode_with_id():
    # Pega uma conexão do pool com tentativas de retry
    connection = get_connection_with_retry(pool)

    try:
        # Iniciar transação manualmente
        connection.start_transaction()
        
        # Define a collation na conexão
        set_collation(connection)

        # Registrar o início do processo
        start_time = time.time()

        with connection.cursor() as cursor:
            # Buscar todos os registros com SIMCODE = 0
            select_sql = "SELECT id, headers FROM headers WHERE SIMCODE = 0 LIMIT 100000"  # Ajuste o limite conforme necessário
            cursor.execute(select_sql)
            results = cursor.fetchall()

            # Listas para armazenar as atualizações e inserções em lote
            updates = []
            actions = []

            # Percorrer cada registro para processar as atualizações e inserções
            for record in results:
                header_id = record[0]  # ID da linha no banco
                header_string = record[1]  # String do header

                # Extraindo o ID do header usando string.split ao invés de regex
                try:
                    id_from_header = int(header_string.split('ID:')[1].split(';')[0])
                except (IndexError, ValueError):
                    continue  # Pula o registro se ocorrer erro ao processar

                # Adicionar à lista de atualizações
                updates.append((id_from_header, header_id))

                # Verificando os valores de v1 a v5 na string diretamente (sem regex)
                if 'V1:1' in header_string:
                    actions.append((id_from_header, 1))  # action_id = 1 para v1
                if 'V2:1' in header_string:
                    actions.append((id_from_header, 2))  # action_id = 2 para v2
                if 'V3:1' in header_string:
                    actions.append((id_from_header, 3))  # action_id = 3 para v3
                if 'V4:1' in header_string:
                    actions.append((id_from_header, 4))  # action_id = 4 para v4
                if 'V5:1' in header_string:
                    actions.append((id_from_header, 5))  # action_id = 5 para v5

            # Realizar as atualizações e inserções em lote
            update_simcode_bulk(updates, connection)
            insert_actions_bulk(actions, connection)

            # Confirmar transação
            connection.commit()

            # Calcular o tempo gasto no ciclo
            time_taken = time.time() - start_time
            time_taken_ms = time_taken * 1000  # Converter para milissegundos

            print(f"Processo concluído em {time_taken:.2f} segundos ({time_taken_ms:.0f} ms)")

    except Exception as e:
        print(f"Erro durante a execução: {e}")
        connection.rollback()  # Reverter em caso de erro
    finally:
        connection.close()

# Loop infinito para executar a função uma vez por minuto
while True:
    update_simcode_with_id()  # Atualiza os SIMCODEs e verifica v1 a v5
    time.sleep(1)  # Pausa de 5 segundos entre execuções
