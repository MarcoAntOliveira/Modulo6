import sqlite3 
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3' 
DB_FILE =ROOT_DIR/DB_NAME
TABLE_NAME = 'costumers'

connection =sqlite3.connect(DB_FILE)
cursor = connection.cursor()
# cuidado: fazendo delete   sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

cursor.execute(
    f'DELETE FROM sqlite_sequece WHERE name="{TABLE_NAME}" '
)
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()
#registrar valores na coluna da tabela
# CUIDADO: sql injection
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id, name, weight)'
    'VALUES '
    '(NULL,  "Helena", 6.7), (NULL , "Eduardo", 10)'
    )

cursor.close()
connection.close()
