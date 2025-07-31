import json
import mysql.connector
from mysql.connector import Error
from pathlib import Path
import logging
from dotenv import load_dotenv
import os

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = int(os.getenv("MYSQL_PORT"))
MYSQL_DB = os.getenv("MYSQL_DB")


DATA_LAKE_RAW = Path("data_lake/raw")

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

ENTITY_TABLE_MAP = {
    "store": "store",
    "guest_check": "guest_check",
    "detail_line": "detail_line",
    "menu_item": "menu_item",
    "tax": "tax"
}


def arquivo_ja_processado(cursor, arquivo_nome):
    """Verifica se o arquivo já foi carregado"""
    cursor.execute("SELECT 1 FROM load_log WHERE file_name = %s", (arquivo_nome,))
    return cursor.fetchone() is not None


def registrar_arquivo_processado(cursor, arquivo_nome):
    """Registra arquivo carregado na tabela de log"""
    cursor.execute("INSERT IGNORE INTO load_log (file_name) VALUES (%s)", (arquivo_nome,))


def carregar_json_para_mysql(arquivo_json: Path, tabela: str, conn):
    """Carrega os dados de um arquivo JSON para a tabela MySQL correspondente"""
    cursor = conn.cursor()

    
    if arquivo_ja_processado(cursor, arquivo_json.name):
        logging.info(f"Pulando {arquivo_json.name} (já processado).")
        return

    with open(arquivo_json, "r", encoding="utf-8") as f:
        registros = json.load(f)

    if not registros:
        logging.warning(f"Arquivo {arquivo_json} está vazio. Ignorando...")
        return

    colunas = list(registros[0].keys())
    placeholders = ", ".join(["%s"] * len(colunas))
    colunas_sql = ", ".join(colunas)

    sql_insert = f"""
        INSERT IGNORE INTO {tabela} ({colunas_sql})
        VALUES ({placeholders})
    """

    valores = [tuple(reg[col] for col in colunas) for reg in registros]
    cursor.executemany(sql_insert, valores)

    
    registrar_arquivo_processado(cursor, arquivo_json.name)

    conn.commit()
    logging.info(f"Carregados {len(registros)} registros de {arquivo_json} para {tabela}")


def processar_data_lake():
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB
        )
        logging.info("Conectado ao MySQL com sucesso!")

        for entidade, tabela in ENTITY_TABLE_MAP.items():
            pattern = f"{entidade}/*/*/*/{entidade}_*.json"
            for arquivo_json in DATA_LAKE_RAW.rglob(pattern):
                carregar_json_para_mysql(arquivo_json, tabela, conn)

        conn.close()
        logging.info("Carga finalizada com sucesso!")
    except Error as e:
        logging.error(f"Erro ao conectar ou inserir no MySQL: {e}")


if __name__ == "__main__":
    processar_data_lake()