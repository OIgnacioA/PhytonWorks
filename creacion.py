from coneccion import creardb
import sqlite3 as sql

creardb()

def create_alumn1():
    nombre= "Juan"
    apellido= "Lopez"
    carrera= "Base de datas"
    con=sql.connect("colegio.db")
    cursor=con.cursor()
    S=("""INSERT INTO ALUMNO (nombre,apellido,carrera) 
    VALUES (?,?,?)""") 
    cursor.execute(S,[nombre,apellido,carrera])
    print("alumno creado con exito")  
    con.commit()
    con.close()


def create_alumn2():
    nombre= "lucia"
    apellido= "lumilagro"
    carrera= "Base de ratas"
    con=sql.connect("colegio.db")
    cursor=con.cursor()
    S=("""INSERT INTO ALUMNO (nombre,apellido,carrera) 
    VALUES (?,?,?)""") 
    cursor.execute(S,[nombre,apellido,carrera])
    print("alumno creado con exito")  
    con.commit()
    con.close()


def create_alumn3():
    nombre= "lucia"
    apellido= "Lopez"
    carrera= "Base de ratas"
    con=sql.connect("colegio.db")
    cursor=con.cursor()
    S=("""INSERT INTO ALUMNO (nombre,apellido,carrera) 
    VALUES (?,?,?)""") 
    cursor.execute(S,[nombre,apellido,carrera])
    print("alumno creado con exito")  
    con.commit()
    con.close()    