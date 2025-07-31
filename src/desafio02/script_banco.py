from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()  

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = int(os.getenv("MYSQL_PORT"))
MYSQL_DB = os.getenv("MYSQL_DB")
MYSQL_PATH_SQL = os.getenv("MYSQL_PATH_SQL")


def criar_banco_e_tabelas():
    connection = None
    cursor = None
    try:
        
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD
        )

        cursor = connection.cursor()

        
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DB};")
        logging.info(f"Banco '{MYSQL_DB}' criado ou já existente.")

        
        cursor.execute(f"USE {MYSQL_DB};")

        
        with open(MYSQL_PATH_SQL, 'r', encoding='utf-8') as f:
            sql_script = f.read()

        
        comandos = sql_script.split(';')

        for comando in comandos:
            comando = comando.strip()
            if comando:
                cursor.execute(comando)

        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS load_log (
                id INT AUTO_INCREMENT PRIMARY KEY,
                file_name VARCHAR(255) UNIQUE NOT NULL,
                load_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        connection.commit()
        logging.info("Tabelas criadas com sucesso, incluindo load_log!")

    except Error as e:
        logging.error(f"Erro ao criar banco/tabelas: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            logging.info("Conexão encerrada.")


if __name__ == "__main__":
    criar_banco_e_tabelas()