# 1. connection to db
# 2. script
# 3. execute the query
# 4.understanding the result

import sqlite3

# def test_sqlite3():
#     dataTables = sqlite3.connect("C:\\Users\\Nikitha\\AppData\\Roaming\\DBeaverData\\workspace6\\.metadata\\sample-database-sqlite-1\\Chinook.db")
#     script = dataTables.cursor()
#     script.execute('select * from Album a')
#     # print(script.fetchall())
#     # print(script.fetchone())
#     # print(script.fetchmany(5))
#     print(script.description)
#     totlarecords = script.fetchall()
#     print(len(totlarecords))
#     dataTables.close()


#pip install mysql-connector-python

# def test_mySql():
#     dataTables = mysql.connector.connect(
#         host="localhost",
#         user="your_username",
#         password="your_password",
#         database="your_database",
#         port=3306
#     )
#     script = dataTables.cursor()
#     script.execute('select * from Album a')
#     # print(script.fetchall())
#     # print(script.fetchone())
#     # print(script.fetchmany(5))
#     print(script.description)
#     totlarecords = script.fetchall()
#     print(len(totlarecords))
#     dataTables.close()


#pip install oracledb

# def test_oracle():
#     dataTables = oracledb.connect(
#         host="localhost",
#         user="your_username",
#         password="your_password",
#         role="your_role",
#         port=3306
#     )
#     script = dataTables.cursor()
#     script.execute('select * from Album a')
#     # print(script.fetchall())
#     # print(script.fetchone())
#     # print(script.fetchmany(5))
#     print(script.description)
#     totlarecords = script.fetchall()
#     print(len(totlarecords))
#     dataTables.close()


##pip install psycopg2

# def test_postgresql():
#     dataTables = psycopg2.connect(
#         host="localhost",
#         user="your_username",
#         password="your_password",
#         database="your_database",
#         port=5432
#     )
#     script = dataTables.cursor()
#     script.execute('select * from Album a')
#     # print(script.fetchall())
#     # print(script.fetchone())
#     # print(script.fetchmany(5))
#     print(script.description)
#     totlarecords = script.fetchall()
#     print(len(totlarecords))
#     dataTables.close()
        