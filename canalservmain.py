from config import *
from main import *
from curs import *
from update import *
from create import *

if __name__ == '__main__':

    values = result.get('values', [])
    try:
        create()
    except psycopg2.errors.UniqueViolation:
        pass
    finally:
        while True:
            for i in range(1, len(values)):
                update(values[i][0], values[i][1], float(values[i][2]) * data['Valute']['USD']["Value"], values[i][3])

