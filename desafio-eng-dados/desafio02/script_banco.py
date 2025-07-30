from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error

load_dotenv()  

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = int(os.getenv("MYSQL_PORT"))
MYSQL_DB = os.getenv("MYSQL_DB")
MYSQL_PATH = os.getenv("MYSQL_PATH")

def criar_banco_e_tabelas():
    try:
       
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD
        )

        cursor = connection.cursor()
       
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DB};")
        print(f"Banco '{MYSQL_DB}' criado ou já existente.")

    
        cursor.execute(f"USE {MYSQL_DB};")

    
        with open(MYSQL_PATH, 'r', encoding='utf-8') as f:
            sql_script = f.read()


        comandos = sql_script.split(';')

        for comando in comandos:
            comando = comando.strip()
            if comando:
                cursor.execute(comando)

        connection.commit()
        print("Tabelas criadas com sucesso!")

    except Error as e:
        print("Erro ao criar banco/tabelas:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão encerrada.")

if __name__ == "__main__":
    criar_banco_e_tabelas()