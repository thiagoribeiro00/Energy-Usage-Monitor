import sqlite3
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_connection(database_name):
    try:
        connection = sqlite3.connect(database_name)
        return connection
    except sqlite3.Error as e:
        logger.exception(f"Erro ao conectar ao banco de dados: {e}")
        return None

def execute_query(connection, query, params=None):
    try:
        with connection:
            cursor = connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            return results
    except sqlite3.Error as e:
        logger.exception(f"Erro ao executar a consulta: {e}")
        return []

def close_connection(connection):
    if connection:
        connection.close()

def create_table(connection):
    sql_create_table = '''
        CREATE TABLE IF NOT EXISTS consumo_energia (
            data TEXT,
            consumo_kw REAL,
            consumo_mwh REAL,
            consumo_normalizado REAL
        )
    '''
    connection.execute(sql_create_table)

# Exemplo de uso:
if __name__ == "__main__":
    db_name = "my_database.db"
    connection = create_connection(db_name)

    try:
        # Exemplo de consulta usando prepared statement
        query = "SELECT * FROM consumo_energia WHERE data = ?"
        date_to_search = "2023-08-06"
        results = execute_query(connection, query, (date_to_search,))
        print(results)

        # Exemplo de inserção de dados
        insert_query = "INSERT INTO consumo_energia (data, hora, consumo_kw) VALUES (?, ?, ?)"
        data_to_insert = ("2023-08-07", "12:00", 100.5)
        execute_query(connection, insert_query, data_to_insert)

    finally:
        close_connection(connection)
