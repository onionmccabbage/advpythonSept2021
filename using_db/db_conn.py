import sqlite3 # built in to Python

# make a connection to a database
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
