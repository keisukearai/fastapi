# -*- coding: utf-8 -*-
import mysql.connector
import env

def get_data(sql):
    conn = mysql.connector.connect(user=env.user, password=env.password,
                                   host=env.host, database=env.database)

    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    rows = cursor.fetchall ()
    cursor.close()
    conn.close()

    return rows

# ret = get_data('select * from switch_info')
# print(ret)