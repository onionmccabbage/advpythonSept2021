import sqlite3

# we need a connection and a cursor
conn  = sqlite3.connect('my_db')
curs = conn.cursor()
# and a statement
statement = '''
SELECT * FROM zoo
'''
# execute the statement
curs.execute(statement)
rows = curs.fetchall()
print(rows) # a list of tuples
# commit
conn.commit()
# tidy up
conn.close()
