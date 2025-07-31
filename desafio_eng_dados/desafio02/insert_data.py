import mysql.connector
from mysql.connector import Error
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_DB = "desafio_engenheiro_de_dados"

def inserir_dados_teste():
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB
        )
        cursor = conn.cursor()

        logging.info("Inserindo dados de teste...")

        cursor.execute("INSERT INTO store (loc_ref) VALUES ('Lago');")
        store_id = cursor.lastrowid
        logging.info(f"Store inserida com id={store_id}")

        cursor.execute("""
            INSERT INTO guest_check (
                store_id, chk_num, opn_bus_dt, opn_utc, clsd_bus_dt, clsd_utc, 
                gst_cnt, sub_ttl, chk_ttl, dsc_ttl, pay_ttl, bal_due_ttl, 
                tbl_num, tbl_name, emp_num, clsd_flag
            )
            VALUES (
                %s, 1234, '2025-07-30', '2025-07-30 12:00:00', 
                '2025-07-30', '2025-07-30 13:00:00', 
                4, 100.00, 120.00, 10.00, 110.00, 0.00, 
                10, 'Mesa 10', 101, 1
            );
        """, (store_id,))
        guest_check_id = cursor.lastrowid
        logging.info(f"Guest_check inserido com id={guest_check_id}")

        
        cursor.execute("""
            INSERT INTO detail_line (
                guest_check_id, line_num, dtl_id, detail_utc, bus_dt, 
                dsp_ttl, dsp_qty, agg_ttl, agg_qty, seat_num, svc_rnd_num
            )
            VALUES (
                %s, 1, 1001, '2025-07-30 12:05:00', '2025-07-30',
                30.00, 1, 30.00, 1, 1, 1
            );
        """, (guest_check_id,))
        detail_line_id = cursor.lastrowid
        logging.info(f"Detail_line inserida com id={detail_line_id}")

        
        cursor.execute("""
            INSERT INTO menu_item (detail_line_id, mi_num, mod_flag, incl_tax, prc_lvl, active_taxes)
            VALUES (%s, 501, 0, 2.50, 1, 'TX1,TX2');
        """, (detail_line_id,))
        menu_item_id = cursor.lastrowid
        logging.info(f"Menu_item inserido com id={menu_item_id}")

        
        cursor.execute("""
            INSERT INTO tax (guest_check_id, tax_num, txbl_sls_ttl, tax_coll_ttl, tax_rate, type)
            VALUES (%s, 1, 100.00, 5.00, 0.05, 1);
        """, (guest_check_id,))
        tax_id = cursor.lastrowid
        logging.info(f"Tax inserido com id={tax_id}")

        
        conn.commit()
        logging.info(" Dados de teste inseridos com sucesso!")

    except Error as e:
        logging.error(f"Erro ao inserir dados: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            logging.info("Conexão encerrada.")

if __name__ == "__main__":
    inserir_dados_teste()