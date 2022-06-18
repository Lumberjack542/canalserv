# import psycopg2
#
#
# from config import *
# from main import *
# from curs import *
#
#
# def delete(No_id, order_no, prise, delivery_time):
#     try:
#         connection = psycopg2.connect(host=host,
#                                       user=user,
#                                       password=password,
#                                       database=db_name)
#
#         cursor = connection.cursor()
#
#         # Update single record now
#         sql_delete = """Delete from canal
#         where order_no = %s,
#         prise = %s,
#         delivery_time = %s
#         No_id = %s """
#
#         cursor.execute(sql_delete, 1, 1, 1, '9999-12-31' )
#
#         connection.commit()
#         count = cursor.rowcount
#         print(count, "Record deleted successfully ")
#
#     except (Exception, psycopg2.Error) as error:
#         print("Error in Delete operation", error)
#
#     finally:
#         # closing database connection.
#         if connection:
#             cursor.close()
#             connection.close()
#             print("PostgreSQL connection is closed")
#
#
# if __name__ == '__main__':
#     delete(1, 1, 1, '9999-12-31')