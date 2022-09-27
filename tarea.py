from json.tool import main
from smtplib import OLDSTYLE_AUTH
import sqlite3 as sql
from creacion import create_alumn3, create_alumn2



def creardb():
    try:
     con=sql.connect("colegio.db")
     con.commit()
     con.close()

    except Exception as ex:
     print (ex) 
    
    
def create_table():
    con=sql.connect("colegio.db")
    cursor=con.cursor()
    cursor.execute("""CREATE TABLE if not exists
    ALUMNO(id_alumno integer primary key autoincrement,
    nombre text,
    apellido text,
    carrera text)""")
    cursor.execute("""CREATE TABLE if not exists
    NOTAS  (id_nota integer primary key autoincrement,
    id_alumno integer,
    nota integer,    
    foreign key ("id_alumno") references "ALUMNO" ("id_alumno")) """)
    con.commit()
    con.close()



def create_alumn():
    nombre= input("ingrese nombre: ")
    apellido= input("ingrese apellido: ")
    carrera= input("ingrese carrera: ")
    con=sql.connect("colegio.db")
    cursor=con.cursor()
    S=("""INSERT INTO ALUMNO (nombre,apellido,carrera) 
    VALUES (?,?,?)""") 
    cursor.execute(S,[nombre,apellido,carrera])
    print("alumno creado con exito")  
    con.commit()
    con.close()
    
def consulta():
    con=sql.connect("colegio.db")
    cursor=con.cursor()
    cursor.execute("""SELECT * FROM ALUMNO""")
    for i in cursor:
        print(i)
    con.commit()
    con.close()
  
def buscar():
    nombre=input("Ingrese el nombre a buscar: ")
    apellido=input("Ingrese el apellido a buscar: ")
    con=sql.connect("colegio.db")
    cursor=con.cursor()

    if ((nombre == '*') and (apellido != '*')):
       
        instruccion = "SELECT * FROM ALUMNO where apellido =" + "'" + apellido + "'"
        cursor.execute(instruccion)
        datos =cursor.fetchall()
        con.commit()
        con.close()
        print (datos)

    elif ((nombre != '*') and (apellido == '*')):
           
        instruccion = "SELECT * FROM ALUMNO where nombre =" + "'" + nombre + "'"
        cursor.execute(instruccion)
        datos =cursor.fetchall()
        con.commit()
        con.close()
        print (datos)

    elif ((nombre == '*') and (apellido == '*')):

        instruccion = "SELECT * FROM ALUMNO "
        cursor.execute(instruccion)
        datos =cursor.fetchall()
        con.commit()
        con.close()
        print (datos)


def borrar():
    legajo=input("Ingrese legajo de alumno a eliminar: ")
    #buscar()
    con=sql.connect("colegio.db")
    cursor=con.cursor()
    instruccion = "DELETE FROM ALUMNO where id_alumno=" + "'" + legajo + "'"
    cursor.execute(instruccion)
    con.commit()
    con.close()
    print("Se borro todo.")
    consulta()

def modificar():
    id_alumno=int(input("Ingrese legajo de alumno a modificar: "))    
    con=sql.connect("colegio.db")
    cursor=con.cursor()   
    cursor.execute("SELECT * FROM ALUMNO where id_alumno="+str(id_alumno))
    for i in cursor:
        print(i)              
    opcion=int(input("1)Nombre 2)Apellido: "))
    nuevo=input("Ingrese nuevo nombre/apellido: ")
    if opcion == 1:
        cursor.execute("UPDATE ALUMNO set nombre=" + "'" + nuevo + "'" + "where id_alumno="+str(id_alumno))
        
    
    
    else:
        print("No se encontro")

    con.commit()
    con.close()
    return("No se encontro") 
    
    

def main():
    opcion=int(input('''Ingrese una opcion: 
    0) Salir 
    1) Agregar alumno 
    2) Mostrar lista 
    3) Buscar 
    4) Borrar alumno
    5) Modificar
    '''))

    while opcion!=0:
        if opcion==1:
            create_alumn()
        if opcion==2:
            consulta()
        if opcion==3:
            print(buscar())
        if opcion==4:
            borrar()
        if opcion==5:
            modificar()

        opcion=int(input('''Ingrese una opcion: 
        0) Salir 
        1) Agregar alumno 
        2) Mostrar listado completo 
        3) Buscar 
        4) Borrar alumno
        5) Modificar
        '''))

    print("Finalizado")


creardb()
create_table()
#create_alumn1()
#create_alumn2()
#create_alumn3()
main()