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
        result = cursor.execute(
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES ("Luiz", 25), ("Marcos", 27)'
        )

        result = cursor.execute(
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES ("Luiz", 25), ("Marcos", 27)'
        )

        result = cursor.execute(
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES ("Luiz", 25), ("Marcos", 27)'
        )
        print(result)    
        #onnection.commit()
        #print(cursor)

    connection.commit()