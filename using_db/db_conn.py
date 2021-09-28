import sqlite3 # built in to Python

# make a connection to a database

# DB2
# import DB2
# conn = DB2.connect(dsn='ibm-DB', uid='analyst', pwd='db2pwd')

# Sybase
# import Sybase
# conn = Sybase.connect('SYBASE', 'username', 'passwd', 'databasename')

# Oracle
# import cx_Oracle
# conn = cx_Oracle.connect('username', 'passwd', 'hostname:port/SID')
# conn2 = cx_Oracle.connect('username/passwd@hostname:portno/SID')
# dsn_tns = cx_Oracle.makedsn('hostname', portno, 'SID')
# conn3 = cx_Oracle.connect('username', 'passwd', dsn_tns)

# MySQL
# import MySQLdb
# conn = MySQLdb.connect(host = "hostname", user = "username",
# passwd = "password", db = "dbname")

# PySQLite
# from pysqlite2 import dbapi2 as sqlite
# conn = sqlite.connect("mydb", connectionproperties)

# ODBC
# import odbc
# conn = odbc. odbc("myDSN/username/password")

conn = sqlite3.connect('my_db') # create the db if not exist (open if exist)

# create a cursor (to access members of the DB)
curs = conn.cursor() # a cursor allows us to work with the db

# we will have a zoo table, containing creatures with count, cost members

# we need an SQL statement (here we follow SQL conventions)
statement = '''
CREATE TABLE zoo
(creature VARCHAR(20) PRIMARY KEY,
 count INT,
 cost FLOAT
)

'''
# .. which we can execute
curs.execute(statement)

# always tidy up when done
conn.commit() # the statement is not committed until this point
conn.close()
