import sqlite3

# we need a connection and a cursor
conn  = sqlite3.connect('my_db')
curs = conn.cursor()
# and a statement
statement = '''
SELECT creature, cost, count FROM zoo
WHERE creature LIKE '%e%'
ORDER BY cost ASC
'''
# execute the statement
curs.execute(statement)
rows = curs.fetchall()
print(rows) # a list of tuples
# we can iterate over the returned data
for animal in rows:
    # print(animal)
    print('Creature:{0} Cost:{1:.2f} Qty:{2}'.format(animal[0],animal[1], animal[2] ))

# commit
conn.commit() # not needed - no changes were made
# tidy up
conn.close()
