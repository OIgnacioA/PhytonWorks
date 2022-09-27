import sqlite3 as sql

import sqlite3 as sql

def creardb():
    try:
     con=sql.connect("colegio.db")
     con.commit()
     con.close()

    except Exception as ex:
     print (ex) 
    
    