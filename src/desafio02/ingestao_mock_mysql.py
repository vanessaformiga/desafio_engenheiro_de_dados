import json
from pathlib import Path
from datetime import datetime
import logging
import argparse
import sys
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do .env (se existir)
load_dotenv()

# Config MySQL via .env
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
MYSQL_DB = os.getenv("MYSQL_DB")

# Paths Data Lake
DATA_LAKE_PATH = Path("data_lake")
RAW_PATH = DATA_LAKE_PATH / "raw"
SCHEMAS_PATH = DATA_LAKE_PATH / "schemas"
METADATA_PATH = DATA_LAKE_PATH / "metadata"
LOG_PATH = DATA_LAKE_PATH / "log"
PROCESSED_PATH = DATA_LAKE_PATH / "processed"

# Cria pastas se não existirem
for path in [RAW_PATH, SCHEMAS_PATH, METADATA_PATH, LOG_PATH, PROCESSED_PATH]:
    path.mkdir(parents=True, exist_ok=True)

# Setup logging para arquivo e console
log_file = LOG_PATH / f"ingestao_mock_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)

# Mock de dados (exemplo)
MOCK_DATA = {
    "store": [
        {"id_store": 1, "loc_ref": "SP-001"},
        {"id_store": 2, "loc_ref": "RJ-001"}
    ],
    "guest_check": [
        {"id_guest_check": 101, "store_id": 1, "chk_ttl": 120.50, "opn_bus_dt": "2025-07-31"},
        {"id_guest_check": 102, "store_id": 2, "chk_ttl": 89.90, "opn_bus_dt": "2025-07-31"}
    ],
    "detail_line": [
        {"id_detail_line": 201, "guest_check_id": 101, "line_num": 1},
        {"id_detail_line": 202, "guest_check_id": 102, "line_num": 1}
    ],
    "menu_item": [
        {"id_menu_item": 301, "detail_line_id": 201, "mi_num": 10},
        {"id_menu_item": 302, "detail_line_id": 202, "mi_num": 20}
    ],
    "tax": [
        {"id_tax": 401, "guest_check_id": 101, "type": 1, "tax_rate": 0.05},
        {"id_tax": 402, "guest_check_id": 102, "type": 2, "tax_rate": 0.10}
    ]
}

arquivos_gerados = []  # lista para metadata

# --- FUNÇÕES MYSQL ---

def conectar_mysql():
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB
        )
        logging.info("Conectado ao MySQL com sucesso!")
        return conn
    except Error as e:
        logging.error(f"Erro ao conectar no MySQL: {e}")
        return None

def salvar_no_mysql(entidade: str, dados: list):
    conn = conectar_mysql()
    if not conn:
        logging.error("Conexão MySQL não estabelecida. Abortando inserção.")
        return

    cursor = conn.cursor()

    tabela = entidade  # Assumindo nome da tabela igual à entidade

    if not dados:
        logging.warning(f"Nenhum dado para inserir na tabela {tabela}.")
        conn.close()
        return

    colunas = list(dados[0].keys())
    colunas_sql = ", ".join(colunas)
    placeholders = ", ".join(["%s"] * len(colunas))

    sql_insert = f"INSERT IGNORE INTO {tabela} ({colunas_sql}) VALUES ({placeholders})"

    valores = [tuple(item[col] for col in colunas) for item in dados]

    try:
        cursor.executemany(sql_insert, valores)
        conn.commit()
        logging.info(f"{cursor.rowcount} registros inseridos na tabela {tabela}.")
    except Error as e:
        logging.error(f"Erro ao inserir dados na tabela {tabela}: {e}")
    finally:
        cursor.close()
        conn.close()

# --- FUNÇÕES DATA LAKE ---

def gerar_schema(entidade: str, dados: list):
    schema_file = SCHEMAS_PATH / f"{entidade}_schema.json"
    if schema_file.exists():
        logging.info(f"Schema para {entidade} já existe em {schema_file}")
        return

    if not dados:
        logging.warning(f"Sem dados para criar schema para {entidade}")
        return

    primeiro = dados[0]
    schema = {k: type(v).__name__ for k, v in primeiro.items()}

    try:
        with open(schema_file, "w", encoding="utf-8") as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)
        logging.info(f"Schema criado para {entidade} em {schema_file}")
    except Exception as e:
        logging.error(f"Erro ao criar schema para {entidade}: {e}")

def salvar_processed(entidade: str, dados: list):
    hoje = datetime.now()
    dir_processed = PROCESSED_PATH / entidade / hoje.strftime("%Y/%m/%d")
    dir_processed.mkdir(parents=True, exist_ok=True)

    id_field = None
    if dados:
        for key in dados[0].keys():
            if "id" in key.lower():
                id_field = key
                break

    arquivo = dir_processed / f"{entidade}_processed_{hoje.strftime('%Y%m%d%H%M%S')}.csv"

    try:
        with open(arquivo, "w", encoding="utf-8") as f:
            if id_field:
                f.write(f"{id_field}\n")
                for item in dados:
                    f.write(f"{item.get(id_field)}\n")
                logging.info(f"Processed salvo (IDs) para {entidade} em {arquivo}")
            else:
                json.dump(dados, f, indent=2, ensure_ascii=False)
                logging.info(f"Processed salvo (JSON) para {entidade} em {arquivo}")
    except Exception as e:
        logging.error(f"Erro ao salvar processed para {entidade}: {e}")

def salvar_mock(entidade: str, dados: list) -> None:
    if not dados:
        logging.warning(f"Nenhum dado para salvar em {entidade}.")
        return

    hoje = datetime.now()
    dir_entidade = RAW_PATH / entidade / hoje.strftime("%Y/%m/%d")
    dir_entidade.mkdir(parents=True, exist_ok=True)

    arquivo = dir_entidade / f"{entidade}_{hoje.strftime('%Y%m%d%H%M%S')}.json"
    try:
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)
        logging.info(f"Arquivo salvo com sucesso: {arquivo}")

        arquivos_gerados.append({
            "entidade": entidade,
            "arquivo": arquivo.name,
            "caminho_completo": str(arquivo.resolve()),
            "qtd_registros": len(dados),
            "status": "ok",
            "data_ingestao": hoje.strftime("%Y-%m-%d %H:%M:%S")
        })

        gerar_schema(entidade, dados)
        salvar_processed(entidade, dados)

        # Grava no MySQL
        salvar_no_mysql(entidade, dados)

    except Exception as e:
        logging.error(f"Erro ao salvar {entidade}: {e}")
        arquivos_gerados.append({
            "entidade": entidade,
            "arquivo": arquivo.name,
            "caminho_completo": str(arquivo.resolve()),
            "qtd_registros": len(dados),
            "status": f"erro: {e}",
            "data_ingestao": hoje.strftime("%Y-%m-%d %H:%M:%S")
        })

def salvar_metadata():
    if not arquivos_gerados:
        logging.warning("Nenhum arquivo gerado para salvar no metadata.")
        return

    agora = datetime.now().strftime("%Y%m%d_%H%M%S")
    metadata_file = METADATA_PATH / f"ingestao_{agora}.json"

    with open(metadata_file, "w", encoding="utf-8") as f:
        json.dump(arquivos_gerados, f, indent=2, ensure_ascii=False)

    logging.info(f"Metadata gerado em: {metadata_file}")

def main():
    parser = argparse.ArgumentParser(description="Simulador de ingestão de dados mockados em JSON para Data Lake.")
    parser.add_argument(
        "--entidade",
        type=str,
        required=False,
        default="all",
        help="Nome da entidade a salvar (ex: store, guest_check, detail_line, menu_item, tax, all). Se não informado, processa todas."
    )
    args = parser.parse_args()

    entidade = args.entidade.lower()

    if entidade == "all":
        logging.info("Iniciando simulação de TODAS as entidades...")
        for ent, dados in MOCK_DATA.items():
            salvar_mock(ent, dados)
        logging.info("Simulação finalizada para todas as entidades!")
    elif entidade in MOCK_DATA:
        logging.info(f"Iniciando simulação para entidade: {entidade}")
        salvar_mock(entidade, MOCK_DATA[entidade])
        logging.info(f"Simulação finalizada para entidade: {entidade}")
    else:
        logging.error(f"Entidade '{entidade}' não encontrada. Use uma das seguintes: {list(MOCK_DATA.keys()) + ['all']}")

    salvar_metadata()

if __name__ == "__main__":
    main()
    logging.info(f"Logs salvos em: {log_file}")