import pymysql
import re
import os
import json
import time

# Conexão com o banco de dados
def conectar_banco():
    return pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='123456789',
        database='dataHeader',
        port=3306
    )

# Função para ler os registros onde SIMCODE é NULL
def buscar_registros_simcode_null(connection):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id, headers FROM headers WHERE SIMCODE IS NULL"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
    except Exception as e:
        print(f"Erro ao buscar registros: {e}")
        return []

# Função para extrair o ID de dentro do campo 'headers'
def extrair_id(headers_string):
    try:
        id_match = re.match(r"(\d+)", headers_string)
        if id_match:
            return id_match.group(1)
        else:
            return None
    except Exception as e:
        print(f"Erro ao extrair o ID: {e}")
        return None

# Função para verificar se há um evento na string 'headers'
def verificar_evento(headers_string):
    if "&&" in headers_string:
        partes = headers_string.split("&&")
        evento = partes[1]  # O evento está após o "&&"
        return evento
    return None

# Função para registrar o evento na tabela log_eventos
def registrar_evento(connection, event_id, gps_id, data):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO log_eventos (event_id, gps_id, main, data, created_at, updated_at) VALUES (%s, %s, 'D', %s, NOW(), NOW())"
            cursor.execute(sql, (event_id, gps_id, data))
        connection.commit()
        print(f"Evento {event_id} registrado com sucesso para o GPS ID {gps_id}")
    except Exception as e:
        print(f"Erro ao registrar evento: {e}")

# Função para atualizar o SIMCODE com o valor do ID
def atualizar_simcode(connection, id_registro, simcode):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE headers SET SIMCODE = %s WHERE id = %s"
            cursor.execute(sql, (simcode, id_registro))
        connection.commit()
    except Exception as e:
        print(f"Erro ao atualizar SIMCODE: {e}")

# Função para buscar os registros na tabela log_eventos onde main = "A"
def buscar_registros_main_a(connection):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT gps_id, event_id, data FROM log_eventos WHERE main = 'A'"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
    except Exception as e:
        print(f"Erro ao buscar registros com main='A': {e}")
        return []

# Função para ajustar o arquivo JSON com base nos valores de log_eventos
def ajustar_arquivo_json(gps_id, event_id, data, status):
    arquivo_json = f'./gps/{gps_id}.json'
    
    if not os.path.exists(arquivo_json):
        print(f"Arquivo JSON {arquivo_json} não encontrado")
        return

    with open(arquivo_json, 'r+') as f:
        dados_json = json.load(f)

        # Ajustar o valor do event_id dentro da seção EVENTOS
        dados_json[event_id] = True if status == 1 else False

        # Ajustar as variáveis de acordo com a string de 'data'
        data_vars = data.split(";")
        for var in data_vars:
            nome_var, valor = var.split(":")
            valor_bool = valor.lower() == "true"
            
            # Ajustar os campos principais ou os eventos
            if nome_var == "R":
                dados_json["R"] = valor_bool
            elif nome_var == "G":
                dados_json["G"] = valor_bool
            elif nome_var == "B":
                dados_json["B"] = valor_bool
            elif nome_var == "VB":
                dados_json["VIBRACAO"] = valor_bool
            elif nome_var == "BU":
                dados_json["BUZZER"] = valor_bool

        # Voltar ao início do arquivo e escrever as mudanças
        f.seek(0)
        json.dump(dados_json, f, indent=4)
        f.truncate()
        print(f"Arquivo JSON {arquivo_json} ajustado com sucesso")

# Função para atualizar o status na tabela log_eventos para 3
def atualizar_status_log_eventos(connection, gps_id, event_id):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE log_eventos SET status = '3' WHERE gps_id = %s AND event_id = %s"
            cursor.execute(sql, (gps_id, event_id))
        connection.commit()
        print(f"Status de log_eventos atualizado para 3 para GPS ID {gps_id} e Evento {event_id}")
    except Exception as e:
        print(f"Erro ao atualizar status de log_eventos: {e}")

# Função principal para processar o SIMCODE e ajustar o arquivo JSON conforme necessário
def processar_simcode():
    connection = conectar_banco()
    try:
        registros = buscar_registros_simcode_null(connection)
        for registro in registros:
            id_registro = registro[0]
            headers_string = registro[1]
            simcode = extrair_id(headers_string)
            
            if simcode:
                # Verificar se há um evento e imprimir na tela
                evento = verificar_evento(headers_string)
                if evento:
                    print(f"Evento detectado no ID {id_registro}: {evento}")
                    
                    # Separar o event_id e o restante da string "data"
                    partes_evento = evento.split(";")
                    event_id = partes_evento[0]  # O nome do evento
                    data_evento = ";".join(partes_evento[1:])  # O restante da string

                    # Registrar o evento na tabela log_eventos
                    registrar_evento(connection, event_id, simcode, data_evento)
                
                # Atualizar o SIMCODE no banco
                atualizar_simcode(connection, id_registro, simcode)
                print(f"SIMCODE atualizado para o ID {id_registro} com valor {simcode}")

        # Após processar os SIMCODEs, buscar registros na tabela log_eventos com main = 'A'
        registros_main_a = buscar_registros_main_a(connection)
        for registro in registros_main_a:
            gps_id = registro[0]
            event_id = registro[1]
            data = registro[2]

            # Simulando que o status é obtido do banco ou outra lógica (aqui estamos definindo para 1 como exemplo)
            status = 1

            # Ajustar o arquivo JSON conforme as mudanças
            ajustar_arquivo_json(gps_id, event_id, data, status)

            # Atualizar o status na tabela log_eventos para 3
            atualizar_status_log_eventos(connection, gps_id, event_id)
    finally:
        connection.close()

# Função para executar o processo a cada minuto
def executar_cada_minuto():
    while True:
        processar_simcode()
        time.sleep(10)  # Espera de 60 segundos entre cada execução

# Executa a função principal
if __name__ == "__main__":
    executar_cada_minuto()
