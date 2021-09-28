import sqlite3
from sqlite3.dbapi2 import IntegrityError

# a connection
conn = sqlite3.connect('my_db') 
# a cursor
curs = conn.cursor()
# a statement
statement = '''
INSERT INTO zoo
VALUES ("Ocelot", 256, 1.09)
'''
# execute
try:
    curs.execute(statement)
    # commit
    conn.commit()
except IntegrityError as err:
    print('Integrity Exception Occurred: {}'.format(err))
except Exception as err:
    # handle any other kind of exception here
    print ('Generic Exception: {}'.format(err))
finally: # this always runs, even if there was an exception
    # close
    conn.close()