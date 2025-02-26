import sqlite3

conexion = sqlite3.connect ("bd1.db")
try: 
    conexion.execute(""" CREATE TABLE users (
                            id TEXT NOT NULL,
                            firstname TEXT NOT NULL,
                            lastname TEXT NOT NULL,
                            username TEXT NOT NULL,
                            country TEXT NOT NULL, 
                            password_user TEXT NOT NULL)""")
    print ("se creo la tabla de articulos")
except sqlite3.OperationalError:
    print ("la tabla de articulos ya existe")
conexion.close

