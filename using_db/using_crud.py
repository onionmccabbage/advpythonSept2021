# create read update delete CRUD
import sqlite3

def makeConn():
    # we need a connection and a cursor
    conn  = sqlite3.connect('my_db')
    curs = conn.cursor() 
    return (conn, curs)   

def main():
    conn, curs = makeConn()
    # and a statement to UPDATE our database
    statement = '''
    UPDATE zoo
    SET count=99
    WHERE creature IS "bear"
    '''
    # execute the statement
    curs.execute(statement)

    # commit
    conn.commit() 
    # tidy up
    conn.close()

if __name__ == '__main__':
    main()