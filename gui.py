import tkinter  as tk
import sqlite3 as sql

from coneccion import *

var ="" 


def Create():

    global var 

    nombre= entry1.get()
    apellido= entry2.get()
    carrera= entry3.get()

    con=sql.connect("colegio.db")
    cursor=con.cursor()
    S=("""INSERT INTO ALUMNO (nombre,apellido,carrera) 
    VALUES (?,?,?)""") 
    cursor.execute(S,[nombre,apellido,carrera])
    
    texto.insert('1.0', "Alta exitosa" )   
    var = "Alta"
    BuscarTodo()
    con.commit()
    con.close()

def BuscarTodo(): # tambien da respuesta en pamtalla en los otros casos. 
    global var 
    texto.delete("1.0","end")
    Limpiar()
    con=sql.connect("colegio.db")
    cursor=con.cursor()

    if (var == ""):

        cursor.execute("""SELECT * FROM ALUMNO""")
        for i in cursor:
            
            texto.insert('1.0', i )
            texto.insert('1.0', "\n")

    elif(var == "Alta" ):

       texto.insert('1.0', "Agregado con exito!" )
       

    elif(var == "update" ):

       texto.insert('1.0', "Update exitoso!" )

    var =""      
    con.commit()
    con.close()

def Buscar():
    texto.delete("1.0","end")
    Limpiar()
    con=sql.connect("colegio.db")
    cursor=con.cursor()
    contenido = ""
    nombre=entry1.get()
    apellido=entry2.get()
    carrera=entry3.get()


    if ((nombre == '*') and (apellido != '*') and (carrera == "")):
       
        instruccion = "SELECT * FROM ALUMNO where apellido =" + "'" + apellido + "'"
        cursor.execute(instruccion)
        
        for i in cursor:
             contenido = i
             texto.insert('1.0', i )
             texto.insert('1.0', "\n")
        
        txt = texto.get('1.0',tk.END)    
        print(txt) 
      

        if (cursor==0):
            contenido = i
            print("jolow")
            texto.insert('1.0', "no se encuentrar registros con estos datos" )     
       

    elif ((nombre != '*') and (apellido == '*')and (carrera == "")):
           
        instruccion = "SELECT * FROM ALUMNO where nombre =" + "'" + nombre + "'"
        cursor.execute(instruccion)
        
        for i in cursor:
             contenido = i
             texto.insert('1.0', i )
             texto.insert('1.0', "\n")

        txt = texto.get('1.0',tk.END)     
        print(txt) 
       
        if (cursor==0):
            print("jolow")
            texto.insert('1.0', "no se encuentrar registros con estos datos" )     
      
      

    elif ((nombre == '*') and (apellido == '*')and (carrera == "")):

        instruccion = "SELECT * FROM ALUMNO "
        cursor.execute(instruccion)
        
        for i in cursor:
             contenido = i
             texto.insert('1.0', i )
             texto.insert('1.0', "\n")

        txt = texto.get('1.0',tk.END)     
        print(txt) 
    
        if (cursor== 0):
            print("jolow")
            texto.insert('1.0', "no se encuentrar registros con estos datos" )

    elif (((nombre == '') or (apellido == '') or (nombre == '*') or (apellido == '*')) and (carrera != '') ):

        instruccion = "SELECT * FROM ALUMNO where carrera = " + "'" + carrera + "'" 
        cursor.execute(instruccion)
        
    

        for i in cursor:
            contenido = i
            texto.insert('1.0', i )
            texto.insert('1.0', "\n")
    
        txt = texto.get('1.0',tk.END)     
        print(txt) 
        print(cursor.fetchall())

    if(contenido == ""):
           
        texto.insert('1.0', "no se encuentrar registros" )

    con.commit()
    con.close()

def Update():
    global var 
    
    nombre=entry1.get()
    apellido=entry2.get()
    carrera=entry3.get()
    ID = entry4.get()
    con=sql.connect("colegio.db")
    cursor=con.cursor()
    cursor.execute("UPDATE ALUMNO set nombre=" + "'" + nombre + "'" + ", apellido=" + "'" + apellido + "'" + ", carrera=" + "'" + carrera + "'"+"where id_alumno="+str(ID))
    con.commit()
   
    var = "update"
    BuscarTodo()
    Limpiar()

def Delete():

   
    id_alumno=entry4.get()

    con=sql.connect("colegio.db")
    cursor=con.cursor()
    instruccion = "DELETE FROM ALUMNO where id_alumno=" + "'" + id_alumno + "'"
    cursor.execute(instruccion)

    texto.insert('1.0', "Legajo: " + id_alumno + "borrado" )
    con.commit()
    con.close()
    Limpiar()
    BuscarTodo()
   


def traer():
    Limpiar()
    texto.delete("1.0","end")
    con=sql.connect("colegio.db")
    cursor=con.cursor()

    instruccion = "SELECT * FROM ALUMNO where id_alumno = " + "'" + entry4.get() + "'" 
    cursor.execute(instruccion)
    info =  cursor.fetchall()

    for i in info :
      entry1.insert(0, i[1])
      entry2.insert(0, i[2])
      entry3.insert(0, i[3])
    
def Limpiar():
    
    texto.delete("1.0","end")
    entry1.delete("0","end")
    entry2.delete("0","end")
    entry3.delete("0","end")



root = tk.Tk()

root.title("Ventana de Ejemplo")
root.geometry("400x550")

texto = tk.Text(root)
texto.pack()
texto.config(width=50, height=10, font=("Consolas",12),padx=15, pady=15, selectbackground="red")

#   Etiquetas -----------------------------

label1 = tk.Label(root,text="nombre: ")
label1.pack()
label1.place(x=30, y=230)

label1 = tk.Label(root,text="Apellido: ")
label1.pack()
label1.place(x=30, y=270)

label1 = tk.Label(root,text="Carrera: ")
label1.pack()
label1.place(x=30, y=310)

label1 = tk.Label(root,text="ID :(Update/Delete) : ")
label1.pack()
label1.place(x=250, y=360)


#  Botones --------------------------



boton = tk.Button(text="Ver BBDD", command=BuscarTodo)
boton.place(x=180, y=490)

boton = tk.Button(text="   Buscar x Dato  ", command=Buscar)
boton.place(x=250, y=250)

boton = tk.Button(text="   Alta  ", command=Create)
boton.place(x=250, y=290)

boton = tk.Button(text="   Editar   ", command=Update)
boton.place(x=250, y=410)



entry4 = tk.Entry()  #--------------------------- ID
entry4.place(x=250, y=380)


boton = tk.Button(text="   Eliminar   ", command=Delete)
boton.place(x=320, y=410)

boton = tk.Button(text="   Limpiar campos   ", command=Limpiar)
boton.place(x=50, y=490)

boton = tk.Button(text="   Traer Datos  ", command=traer)
boton.place(x=150, y=380)



#entradas: --Nombre-Apellido--------------------------    

entry1 = tk.Entry()
entry1.place(x=30, y=250)

entry2 = tk.Entry()
entry2.place(x=30, y=290)

#entradas: --carrera--------------------------

entry3 = tk.Entry()
entry3.place(x=30, y=330)




root.mainloop()