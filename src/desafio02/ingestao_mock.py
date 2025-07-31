import json
from pathlib import Path
from datetime import datetime
import logging

DATA_LAKE_RAW_PATH = Path("data_lake/raw")
LOGS_PATH = Path("logs")
LOGS_PATH.mkdir(parents=True, exist_ok=True)  


log_file = LOGS_PATH / f"ingestao_mock_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8"),
        logging.StreamHandler()
    ]
)


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

def salvar_mock(entidade: str, dados: list):
    """Salva os dados mockados em um arquivo JSON na estrutura raw/ano/mês/dia"""
    hoje = datetime.now()
    ano = str(hoje.year)
    mes = str(hoje.month).zfill(2)
    dia = str(hoje.day).zfill(2)

    dir_entidade = DATA_LAKE_RAW_PATH / entidade / ano / mes / dia
    dir_entidade.mkdir(parents=True, exist_ok=True)

    arquivo = dir_entidade / f"{entidade}_{hoje.strftime('%Y%m%d%H%M%S')}.json"
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

    logging.info(f"Arquivo salvo: {arquivo}")

if __name__ == "__main__":
    logging.info("Iniciando simulação das APIs...")

    for entidade, dados in MOCK_DATA.items():
        salvar_mock(entidade, dados)

    logging.info("Simulação finalizada com sucesso!")
    logging.info(f"Logs salvos em: {log_file}")