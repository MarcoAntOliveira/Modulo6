import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR/DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

"""cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)"""
connection.commit()
sql =  (f'INSERT INTO {TABLE_NAME}'
        '(name, weight)'
        'VALUES'    
        '(:nome, :peso)')
cursor.executemany(sql,( {'nome': 'joana','peso' :5},
                    {'nome': 'marcos','peso' :9},
                    {'nome': 'rafael','peso' :87}))
connection.commit()

if __name__ == "__main__":
    cursor.execute(f'SELECT * FROM {TABLE_NAME} '
               'WHERE id = "3"')
    for row in cursor.fetchall():
        _id, name, weight = row
        print (_id, name, weight)
    connection.commit()

    cursor.execute(
        f'UPDATE {TABLE_NAME}'
        'SET name="Qualquer"'
        'WHERE id = 1'
    )
    connection.commit()

    cursor.execute(f'DELETE  FROM {TABLE_NAME} '
               'WHERE id = "2"')
    connection.commit()

    cursor.close()
    connection.close    