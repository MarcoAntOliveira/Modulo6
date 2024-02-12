import pymysql
import dotenv #type:ignore
import os

dotenv.load_dotenv()
TABLE_NAME = 'customers'

connection = pymysql.connect(
    host =os.environ['MYSQL_HOST'],
    user = os.environ['MYSQL_USER'],
    password =os.environ['MYSQL_PASSWORD'],
    database =os.environ['MYSQL_DATABASE'],
    charset= 'utf8mb4'
)

print(os.environ['MYSQL_HOST'])
with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}('
            'id INT NOT NULL AUTO_INCREMENT,'
            'nome VARCHAR(50) NOT NULL,'
            'idade INT NOT NULL,'
            'PRIMARY KEY(id)'

            ')'
        )
        cursor.execute(f'TRUNCATE {TABLE_NAME}')

    connection.commit()
    with connection.cursor() as cursor:
        sql =(
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade)'
            'VALUES '
            '(%(nome)s, %(idade)s)'
            )
        data = (
        {"idade": 27,"nome": "marcos"},
        {"idade": 29,"nome": "mateus"},
        {"idade": 25,"nome": "raul"},
        {"idade": 27,"nome": "marcos"},
        )
        result = cursor.executemany(sql, data )
  


        with connection.cursor() as cursor:
            sql = (
                f'SELECT * FROM {TABLE_NAME}'
            )
            cursor.execute(sql)
            data5 = cursor.fetchall()
            for row in data5:
                print(row)
    connection.commit()