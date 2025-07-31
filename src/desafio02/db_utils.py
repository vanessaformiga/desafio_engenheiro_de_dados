from dotenv import load_dotenv
import os
import mysql.connector
import logging

load_dotenv()

DB_CONFIG = {
    'user': os.getenv("MYSQL_USER"),
    'password': os.getenv("MYSQL_PASSWORD"),
    'host': os.getenv("MYSQL_HOST"),
    'port': int(os.getenv("MYSQL_PORT")),
    'database': os.getenv("MYSQL_DB"),
    'raise_on_warnings': True,
}

def connect_db():
    """Cria e retorna uma conexão com o banco de dados MySQL."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        logging.info("Conexão com o banco de dados estabelecida.")
        return conn
    except mysql.connector.Error as err:
        logging.error(f"Erro ao conectar ao banco: {err}")
        raise

def clear_tables(conn):
    """Limpa os dados das tabelas usadas nos testes."""
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM guest_check;")
        cursor.execute("DELETE FROM guest_check_versioned;")
        conn.commit()
        logging.info("Tabelas guest_check e guest_check_versioned limpas com sucesso.")
    except mysql.connector.Error as err:
        logging.error(f"Erro ao limpar tabelas: {err}")
        raise
    finally:
        cursor.close()

def insert_guest_checks(conn, data):
    """Insere múltiplos registros na tabela guest_check.

    Args:
        conn: conexão MySQL ativa.
        data: lista de tuplas (id_guest_check, store_id, guest_count).
    """
    cursor = conn.cursor()
    query = "INSERT INTO guest_check (id_guest_check, store_id, guest_count) VALUES (%s, %s, %s)"
    try:
        cursor.executemany(query, data)
        conn.commit()
        logging.info(f"{cursor.rowcount} registros inseridos em guest_check.")
    except mysql.connector.Error as err:
        logging.error(f"Erro ao inserir dados em guest_check: {err}")
        raise
    finally:
        cursor.close()

def insert_version(conn, id_gc, version, store_id, guest_count, valid_from, valid_to=None):
    """Insere uma versão na tabela guest_check_versioned."""
    cursor = conn.cursor()
    query = """
        INSERT INTO guest_check_versioned
        (id_guest_check, version_number, store_id, guest_count, valid_from, valid_to)
        VALUES (%s, %s, %s, %s, %s, %s);
    """
    try:
        cursor.execute(query, (id_gc, version, store_id, guest_count, valid_from, valid_to))
        conn.commit()
        logging.info("Versão inserida na tabela guest_check_versioned.")
    except mysql.connector.Error as err:
        logging.error(f"Erro ao inserir versão: {err}")
        raise
    finally:
        cursor.close()

def query_current_version(conn, id_gc):
    """Consulta a versão atual de um guest_check."""
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM guest_check_versioned WHERE id_guest_check = %s AND valid_to IS NULL;"
    try:
        cursor.execute(query, (id_gc,))
        result = cursor.fetchone()
        logging.info(f"Versão atual consultada para guest_check {id_gc}.")
        return result
    except mysql.connector.Error as err:
        logging.error(f"Erro ao consultar versão atual: {err}")
        raise
    finally:
        cursor.close()