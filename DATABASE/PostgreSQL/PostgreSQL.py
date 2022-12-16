import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def crear():
    #establishing the connection
    conn = psycopg2.connect(database="postgres", user='postgres', password='password', host='127.0.0.1', port= '5432')
    #conn = psycopg2.connect(database="actividad", user="yo",password="cursoPython",host="localhost", port=5432)

    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Preparing query to create a database
    sql = '''CREATE database mydb''';

    #Creating a database
    cursor.execute(sql)
    print("Database created successfully........")

    #Closing the connection
    cursor.close()
    conn.close()

def conectar():
    #conn = psycopg2.connect(database="actividad", user="yo",password="cursoPython",host="localhost", port=5432)
    conn = psycopg2.connect(database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432')
    cur = conn.cursor()
    # Close communication with the database
    return conn, cur

def cerrar(conn,cur):
    #conn.commit()
    cur.close()
    conn.close()

def createTablaNotas():
    try:
        conn = psycopg2.connect(database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432')
        #conn = psycopg2.connect(database="actividad", user="yo",password="cursoPython",host="localhost", port=5432)

        conn.autocommit = True

        #Creating a cursor object using the cursor() method
        cur = conn.cursor()
        cur.execute("CREATE TABLE notas(ID_notas SERIAL PRIMARY KEY, name varchar(80), age int, grades real, ID_edic INT REFERENCES edicion(ID_edic));")
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print("Error crear la tabla Notas: %s" % str(e))

def createTablaEdicion():
    try:
        conn = psycopg2.connect(database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432')
        #conn = psycopg2.connect(database="actividad", user="yo",password="cursoPython",host="localhost", port=5432)

        conn.autocommit = True

        #Creating a cursor object using the cursor() method
        cur = conn.cursor()
        cur.execute("CREATE TABLE edicion(ID_edic SERIAL PRIMARY KEY,Numero varchar(80));")
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print("Error crear la tabla Edicion: %s" % str(e))

def insertarEdicion(value):
    try:
        conn = psycopg2.connect(database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432')
        #conn = psycopg2.connect(database="actividad", user="yo",password="cursoPython",host="localhost", port=5432)

        conn.autocommit = True

        #Creating a cursor object using the cursor() method
        cur = conn.cursor()
        cur.execute(f"INSERT INTO edicion (Numero) VALUES('{value}');")
        
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print('Error Insertar dato: %s', str(e))
        
def insertarEdic(ediciones):
    for edicion in ediciones:
     insertarEdicion(edicion)

def insertarNotas(name:str, age:int, notas:float, ID_edic:int):
    try:
        conn = psycopg2.connect(database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432')
        #conn = psycopg2.connect(database="actividad", user="yo",password="cursoPython",host="localhost", port=5432)

        conn.autocommit = True

        #Creating a cursor object using the cursor() method
        cur = conn.cursor()
        cur.execute(f"INSERT INTO notas (Name, age, grades, ID_edic) VALUES('{name}', {age}, {notas}, {ID_edic});")
        
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print("Error crear registro: %s" % str(e))
        
def insertNotas(notas):
    for nota in notas:
        insertarNotas(nota['name'], nota['age'], nota['notas'], nota['id_ed'])

def actualizar(tabla:str, nota:float, name:str):
    try:
        conn = psycopg2.connect(database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432')
        #conn = psycopg2.connect(database="actividad", user="yo",password="cursoPython",host="localhost", port=5432)

        conn.autocommit = True

        #Creating a cursor object using the cursor() method
        cur = conn.cursor()
        cur.execute(f"UPDATE {tabla} SET grades={nota} WHERE name='{name}';")
        
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print("Error actualizar registro: %s" % str(e))
        
def mostrar(tabla:str):
    try:
        conn = psycopg2.connect(database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432')
        #conn = psycopg2.connect(database="actividad", user="yo",password="cursoPython",host="localhost", port=5432)

        conn.autocommit = True

        #Creating a cursor object using the cursor() method
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {tabla};")
        
        rows = cur.fetchall()
        for row in rows:
            print(row)
        
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print("Error mostrar registros: %s" % str(e))

def filtrar(tabla:str,column:str, nota1:float, nota2:float):
    conn = psycopg2.connect(database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432')
    #conn = psycopg2.connect(database="actividad", user="yo",password="cursoPython",host="localhost", port=5432)

    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {tabla} WHERE {column} BETWEEN {nota1} AND {nota2};")
    rows = cur.fetchall()
    print(f"\n---- Datos en tabla {tabla} con\
        {column} entre {nota1} y {nota2}--\n")
    
    for row in rows:
        print(row)
       
    cur.close()
    conn.close()
def unirTablas(tabla:str, value:str):
    
    conn = psycopg2.connect(database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432')
    #conn = psycopg2.connect(database="actividad", user="yo",password="cursoPython",host="localhost", port=5432)

    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {tabla} n INNER JOIN edicion e ON n.ID_edic = e.ID_edic WHERE numero = '{value}';")
    rows = cur.fetchall()
    print("\n---- Datos en de personas en la edicion DOS---\n")
    for row in rows:
        print(row)
       
    cur.close()
    conn.close()

def delete(tabla:str, name:str):
    try:
        
        conn = psycopg2.connect(database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432')
        #conn = psycopg2.connect(database="actividad", user="yo",password="cursoPython",host="localhost", port=5432)

        conn.autocommit = True

        #Creating a cursor object using the cursor() method
        cur = conn.cursor()
        cur.execute(f"DELETE FROM {tabla} WHERE name='{name}';")
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print('Error eliminar dato: %s', str(e))

import os

borrarPantalla=lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def funcion_menu():
    while True:
        #C:\Users\Matusaleno\Documents\Apuntes\Curso Data Science\Ejercicios\Míos\Dataset\git_test\Data-Science\media
        borrarPantalla()
        print("*************************** MENU **************************")
        print("************************ EJERCICIOS ***********************")
        print("***** 1. Crear BD *****************************************")
        print("***** 2. Crear Tablas *************************************")
        print("***** 3. Insertar **************************************")
        print("***** 4. Mostrar **************************************")
        print("***** 5. Update **************************************")
        print("***** 6. Mostrar entre notas **************************************")
        print("***** 7. Unir Tablas **************************************")
        print("***** 8. Borrar **************************************")
        print("***** 99. Salir (del menú) ********************************")
        print("***********************************************************")
        print("\n")
        
        opcion = int(input("Inserte su opción: "))
        
        if opcion == 1:         
            
            crear()
            
            click=input("Press to continue...")
        elif opcion == 2:               

            createTablaEdicion()
            createTablaNotas()

            click=input("Press to continue...")
        elif opcion == 3: 
            
            ediciones = ["UNO","DOS","TRES"]
            notas = [{"name": 'Isabel Maniega', "age": 30, "notas": 5.6, "id_ed": 1},
                        {"name": 'José Manuel Peña', "age": 30, "notas": 7.8, "id_ed": 1},
                        {"name": 'Pedro López', "age": 25, "notas": 8.4, "id_ed": 2},
                        {"name": 'Amparo Mayora', "age": 28, "notas": 7.3, "id_ed": 3},
                        {"name": 'Juan Martínez', "age": 30, "notas": 6.8, "id_ed": 3},
                        {"name": 'Fernando López', "age": 35, "notas": 6.1, "id_ed": 2},
                        {"name": 'María Castro', "age": 41, "notas": 5.9, "id_ed": 3},
                    ]                    

            conn,cur=conectar()

            insertarEdic(ediciones)
            insertNotas(notas)

            click=input("Press to continue...")
        elif opcion == 4:   
      
            mostrar("notas")
            mostrar("edicion")

            click=input("Press to continue...")
        elif opcion == 5:      

            actualizar('notas', 6.4, 'Pedro López')
            actualizar('notas', 5.2, 'María Castro')

            click=input("Press to continue...")
        elif opcion == 6: 

            filtrar("notas", "grades", 5.0, 6.5)

            click=input("Press to continue...")
        elif opcion == 7:
            
            unirTablas("notas", 'DOS')
            
            click=input("Press to continue...")
        elif opcion == 8:
            
            delete('notas', "Pedro López")

            click=input("Press to continue...")
        elif opcion == 99:
            break
        else:
            print("por favor, escriba una opción correcta. ")
            print("\n")
            
funcion_menu()

print("Enhorabuena acabaste los ejercicios")