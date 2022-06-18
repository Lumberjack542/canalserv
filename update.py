import psycopg2


from config import *
from main import *
from curs import *


def update(No_id, order_no, prise, delivery_time):
    """ update vendor name based on the vendor id """
    sql = """ UPDATE canal SET 
                order_no = %s, 
                prise = %s,
                delivery_time = %s
                WHERE No_id = %s"""
    conn = None
    updated_rows = 0
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=db_name
                                )
        cur = conn.cursor()
        cur.execute(sql, (order_no, prise, delivery_time, No_id))
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


if __name__ == '__main__':

    for i in range(1, len(values)):
        update(values[i][0], values[i][1], float(values[i][2]) * data['Valute']['USD']["Value"], values[i][3])













