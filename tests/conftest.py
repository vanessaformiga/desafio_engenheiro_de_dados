import pytest
from src.desafio02.db_utils import connect_db, clear_tables
from src.desafio02.setup_db import criar_banco_e_tabelas  

@pytest.fixture(scope="session")
def db_connection():
    criar_banco_e_tabelas()

    conn = connect_db()
    yield conn
    conn.close()

@pytest.fixture(autouse=True)
def clean_tables(db_connection):
    clear_tables(db_connection)