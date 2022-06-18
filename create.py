import psycopg2


from config import *
from main import *
from curs import *


def create():
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            '''CREATE TABLE if not exists canal(
            No_id integer PRIMARY KEY ,
            order_no varchar(50) NOT NULL ,
            prise float NOT NULL  ,
            delivery_time date not null default DATE '9999-12-31'
            )
            '''
        )

    with connection.cursor() as cursor:
        for i in range(1, len(values)):

            sql = "INSERT INTO  canal(No_id, order_no, prise, delivery_time) VALUES (%s, %s, %s, %s);"
            val = (values[i][0], values[i][1], float(values[i][2]) * data['Valute']['USD']["Value"], values[i][3])
            cursor.execute(sql, val)
