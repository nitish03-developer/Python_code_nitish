# creating Database

import mysql.connector
try:
    conn = mysql.connector.connect(
        user='root',
        password='nitish',
        host='localhost',
        port=3306
    )
    if(conn.is_connected()):
        print('Connected')
except:
    print('Unable to connected')
    
sql='CREATE DATABASE pdb'
myc=conn.cursor()
myc.execute(sql)
myc.close()
conn.close
    




