from dotenv import load_dotenv
import os
import mysql.connector
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = int(os.getenv("MYSQL_PORT"))
MYSQL_DB = os.getenv("MYSQL_DB")

def criar_banco_e_tabelas():
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD
        )
        cursor = conn.cursor()

        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DB};")
        cursor.execute(f"USE {MYSQL_DB};")

        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        cursor.execute("DROP TABLE IF EXISTS guest_check_versioned;")
        cursor.execute("DROP TABLE IF EXISTS guest_check;")
        cursor.execute("DROP TABLE IF EXISTS store;")
        cursor.execute("DROP TABLE IF EXISTS load_log;")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS store (
                id_store INT PRIMARY KEY,
                location VARCHAR(100)
            );
        """)

        cursor.execute("""
            INSERT INTO store (id_store, location)
            VALUES 
                (10, 'Local 10'),
                (11, 'Local 11')
            ON DUPLICATE KEY UPDATE location = VALUES(location);
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS guest_check (
                id_guest_check INT PRIMARY KEY,
                store_id INT NOT NULL,
                guest_count INT,
                FOREIGN KEY (store_id) REFERENCES store(id_store)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS guest_check_versioned (
                id_version INT AUTO_INCREMENT PRIMARY KEY,
                id_guest_check INT NOT NULL,
                version_number INT NOT NULL,
                store_id INT NOT NULL,
                guest_count INT,
                valid_from DATETIME,
                valid_to DATETIME,
                FOREIGN KEY (id_guest_check) REFERENCES guest_check(id_guest_check)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS load_log (
                id INT AUTO_INCREMENT PRIMARY KEY,
                file_name VARCHAR(255) UNIQUE NOT NULL,
                load_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        conn.commit()
        logging.info("Banco e tabelas criados com sucesso!")

    except mysql.connector.Error as err:
        logging.error(f"Erro ao criar banco/tabelas: {err}")

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    criar_banco_e_tabelas()