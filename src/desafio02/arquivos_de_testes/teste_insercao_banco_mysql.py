import mysql.connector
from mysql.connector import Error
import logging
from dotenv import load_dotenv
import os

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = int(os.getenv("MYSQL_PORT"))
MYSQL_DB = os.getenv("MYSQL_DB")


def inserir_dados():
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB
        )

        cursor = conn.cursor()

       
        lojas = [("Unidade A",), ("Unidade B",)]
        cursor.executemany("INSERT INTO store (loc_ref) VALUES (%s)", lojas)
        conn.commit()
        logging.info("Lojas inseridas com sucesso.")

       
        cursor.execute("SELECT id_store FROM store WHERE loc_ref = 'Unidade A'")
        store_id = cursor.fetchone()[0]

       
        cursor.execute("""
            INSERT INTO guest_check 
            (store_id, chk_num, opn_bus_dt, opn_utc, clsd_bus_dt, clsd_utc, gst_cnt,
             sub_ttl, chk_ttl, dsc_ttl, pay_ttl, bal_due_ttl, tbl_num, tbl_name, emp_num, clsd_flag)
            VALUES 
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            store_id, 1234, '2025-07-30', '2025-07-30 12:00:00', '2025-07-30', '2025-07-30 13:00:00', 4,
            100.00, 120.00, 10.00, 110.00, 0.00, 10, 'Mesa 10', 101, 1
        ))
        guest_check_id = cursor.lastrowid
        logging.info(f"guest_check inserido com id {guest_check_id}")

       
        cursor.execute("""
            INSERT INTO detail_line 
            (guest_check_id, line_num, dtl_id, detail_utc, bus_dt, dsp_ttl, dsp_qty, agg_ttl, agg_qty, seat_num, svc_rnd_num)
            VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            guest_check_id, 1, 1001, '2025-07-30 12:05:00', '2025-07-30', 30.00, 1, 30.00, 1, 1, 1
        ))
        detail_line_id = cursor.lastrowid
        logging.info(f"detail_line inserido com id {detail_line_id}")

        
        cursor.execute("""
            INSERT INTO menu_item 
            (detail_line_id, mi_num, mod_flag, incl_tax, prc_lvl, active_taxes)
            VALUES
            (%s, %s, %s, %s, %s, %s)
        """, (
            detail_line_id, 501, 0, 2.50, 1, 'TX1,TX2'
        ))

        cursor.execute("""
            INSERT INTO tax 
            (guest_check_id, tax_num, txbl_sls_ttl, tax_coll_ttl, tax_rate, type)
            VALUES
            (%s, %s, %s, %s, %s, %s)
        """, (
            guest_check_id, 1, 100.00, 5.00, 0.05, 1
        ))

        conn.commit()
        logging.info("Todos os dados inseridos com sucesso.")

    except Error as e:
        logging.error(f"Erro ao inserir dados: {e}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            logging.info("Conexão encerrada.")


if __name__ == "__main__":
    inserir_dados()