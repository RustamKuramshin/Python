# pymssql

import pymssql
conn = pymssql.connect(host='CAT\SQLEXPRESS', user='sa', password='15112016', database='pydb')
cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
cursor = conn.cursor()
conn.commit()
conn.close()
row = cursor.fetchone()



# pyodbc
import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=CAT\SQLEXPRESS;PORT=1433;DATABASE=pydb;UID=sa;PWD=15112016')

