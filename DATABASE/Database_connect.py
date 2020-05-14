#creating Database

import mysql.connector
try:
    conn = mysql.connector.connect(
        user='root',
        password='nitish',
        host='localhost',
        database='pdb',
        port=3306
    )
    if(conn.is_connected()):
        print('Connected')
except:
    print('Unable to Connect')
conn.close()