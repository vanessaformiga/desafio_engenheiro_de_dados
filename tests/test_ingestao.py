import datetime
from src.desafio02.db_utils import insert_version, query_current_version

def test_versioning(db_connection):
    now = datetime.datetime.now()

    
    cursor = db_connection.cursor()
    cursor.execute(
        "INSERT INTO guest_check (id_guest_check, store_id, guest_count) VALUES (%s, %s, %s)",
        (1, 10, 5)
    )
    db_connection.commit()
    cursor.close()

    
    insert_version(db_connection, 1, 1, 10, 5, now - datetime.timedelta(days=2), now - datetime.timedelta(days=1))
    insert_version(db_connection, 1, 2, 10, 6, now - datetime.timedelta(days=1), None)

    
    current = query_current_version(db_connection, 1)
    assert current['version_number'] == 2
    assert current['guest_count'] == 6