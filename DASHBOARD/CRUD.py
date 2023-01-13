import os

import datasettings
import pandas as pd
import psycopg2
import psycopg2.errors
import settings
from connection import cerrar, conectar


def existeDataBase():
    try:
        cur, conn = conectar()

        sql=f"SELECT DISTINCT table_name FROM information_schema.columns WHERE table_catalog = '{settings.DATABASE}'"
        cur.execute(sql)
        
        rows = cur.fetchall()
        cerrar(cur, conn)

        if rows == []:
            return False#{f"msg":"No existe BBDD"}
        else:
            return True#print("Database exists correctly........")
    except psycopg2.Error as e:
        return str(e)

def existeTabla(n_table:str):
    try:
        cur, conn = conectar()

        sql=f"SELECT DISTINCT table_name FROM information_schema.columns WHERE table_catalog = '{settings.DATABASE}' AND table_name='{n_table}'"
        cur.execute(sql)
        
        rows = cur.fetchall()
        cerrar(cur, conn)

        if rows == []:
            return False#{f"msg":"No existe BBDD"}
        else:
            return True#print("Database exists correctly........")
    except psycopg2.Error as e:
        return str(e)

def createDatabase(n_database:str):
    try:
        conn = psycopg2.connect(database=datasettings.INIDATABASE,
                            user=settings.USER,
                            password=settings.PASSWORD,
                            host=settings.HOST,
                            port=settings.PORT)

        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(f"CREATE DATABASE {n_database};")
        cerrar(cur, conn)
    except psycopg2.Error as e:
        return e

    return f"{n_database } Database created successfully........"

def createTabla(n_table:str):
    try:
        cur, conn = conectar()
        conn.autocommit = True
        sql=""
        #Creating a cursor object using the cursor() method
        if n_table==datasettings.IRISTABLE:
            sql=f"CREATE TABLE {n_table}(Id int PRIMARY KEY, PetalLengthCm real, PetalWidthCm real, SepalLengthCm real, SepalWidthCm real, Species varchar(80));"
        elif  n_table==datasettings.RESULTSTABLE:
            sql=f"CREATE TABLE {n_table}(Id SERIAL PRIMARY KEY, PetalLengthCm real, PetalWidthCm real, SepalLengthCm real, SepalWidthCm real, Prediction varchar(80));"
        
        cur.execute(sql) 
        cerrar(cur, conn)
    except psycopg2.Error as e:
        print(f"Error crear la tabla {n_table}: %s" % str(e))
        return e
    
    return f"{n_table} Table created successfully........"
def insertar(n_table:str,id:int, PL:float, PW:float, SL:float, SW:float, tipo:str):
    try:
        cur, conn = conectar()
        sql=""
        #Creating a cursor object using the cursor() method
        if n_table==datasettings.IRISTABLE:
            sql=f"INSERT INTO {n_table} (Id, PetalLengthCm, PetalWidthCm, SepalLengthCm, SepalWidthCm, Species) VALUES({id}, {PL}, {PW}, {SL}, {SW}, '{tipo}');"
        elif  n_table==datasettings.RESULTSTABLE:
            sql=f"INSERT INTO {n_table} (PetalLengthCm, PetalWidthCm, SepalLengthCm, SepalWidthCm, Prediction) VALUES( {PL}, {PW}, {SL}, {SW}, '{tipo}');"

        cur.execute(sql)     
            
        cerrar(cur, conn)
    except psycopg2.Error as e:
        return e
    return True
            
def insertIris(flores):
    for flor in flores:
        linea=False
        linea=insertar(datasettings.IRISTABLE,flor['Id'], flor['PetalLengthCm'], flor['PetalWidthCm'], flor['SepalLengthCm'], flor['SepalWidthCm'], flor['Species'])
        if type(linea)==psycopg2.errors.UniqueViolation:
            return linea
    return "DataSet Inserted successfully........"
def show_All_Tabla(tabla):
        # Conexión a base de datos PostgreSQL
    cur, conn = conectar()
    datos={}

    # Generamos y ejecutamos la query
    try:
        query = f"SELECT * FROM {tabla};"
        cur.execute(query)
        rows = cur.fetchall()
        if rows == []:
            return {f"msg":"Sin registros"}
        else:
            columns_list=[]
            if tabla==datasettings.IRISTABLE:
                columns_list = datasettings.IRISCOLLIST
            elif tabla==datasettings.RESULTSTABLE:
                columns_list = datasettings.RESULTSCOLLIST
            datos = pd.DataFrame (rows, columns = columns_list)

            cerrar(cur, conn)
            return datos

    except psycopg2.Error as e:
        error = "Error mostrar registros: %s" + str(e)

        cerrar(cur, conn)
        return {f"msg":error}   
        
def show_Tabla(tabla, column, valor):
        # Conexión a base de datos PostgreSQL
    cur, conn = conectar()
    datos={}

        # Generamos y ejecutamos la query
    try:
        query = f"SELECT * FROM {tabla} WHERE {column} = {valor};"
        cur.execute(query)
        rows = cur.fetchall()
        if rows == []:
            return {"id":valor , f"msg":"Iris Not Found"}
        else:

            columns_list=[]
            if tabla==datasettings.IRISTABLE:
                columns_list = datasettings.IRISCOLLIST
            elif tabla==datasettings.RESULTSTABLE:
                columns_list = datasettings.RESULTSCOLLIST
            datos = pd.DataFrame (rows, columns = columns_list)

            cerrar(cur, conn)
            return datos

    except psycopg2.Error as e:
        error = "Error mostrar registros: %s" + str(e)

        cerrar(cur, conn)
        return {f"msg":error}   

def filtrar(tabla:str,column:str, valor1:float, valor2:float):
    cur, conn = conectar()
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {tabla} WHERE {column} BETWEEN {valor1} AND {valor2};")
    rows = cur.fetchall()
    print(f"\n---- Datos en tabla {tabla} con\
        {column} entre {valor1} y {valor2}--\n")
        
    for row in rows:
        print(row)
        
        
    cerrar(cur, conn)

def delete_All_Tabla(tabla):
    try:
        cur, conn = conectar()
        conn.autocommit = True

        cur.execute(f"DROP TABLE {tabla};")

        cerrar(cur, conn)
    except psycopg2.Error as e:
        print('Error eliminar tabla: %s', str(e))
    return f"Borrado correcto de la tabla '{tabla}'"

def delete_Tabla(tabla, columna, valor):
    try:
        cur, conn = conectar()
        conn.autocommit = True

        cur.execute(f"DELETE FROM {tabla} WHERE {columna}={valor};")

        cerrar(cur, conn)
    except psycopg2.Error as e:
        print('Error eliminar dato: %s', str(e))
    return f"Columna/s {columna} con valor '{valor}' borrado correctamente de la tabla {tabla}"

borrarPantalla=lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def funcion_menu():
    while True:
            #C:\Users\Matusaleno\Documents\Apuntes\Curso Data Science\Ejercicios\Míos\Dataset\git_test\Data-Science\media
        borrarPantalla()
        print("*************************** MENU **************************")
        print("************************ EJERCICIOS ***********************")
        print("***** 1. Crear BD *****************************************")
        print("***** 2. Crear Tabla Iris *************************************")
        print("***** 3. Insertar **************************************")
        print("***** 4. Mostrar **************************************")
        print("***** 5. Existe BD **************************************")
        print("***** 6. Existe Tabla **************************************")
        # print("***** 7. Unir Tablas **************************************")
        # print("***** 8. Borrar **************************************")
        print("***** 99. Salir (del menú) ********************************")
        print("***********************************************************")
        print("\n")
            
        opcion = int(input("Inserte su opción: "))
            
        if opcion == 1:         
                
            createDatabase("dashboard")
                
            click=input("Press to continue...")
        elif opcion == 2:               

            createTabla("iris")

            click=input("Press to continue...")
        elif opcion == 3: 
                
            df = pd.read_csv("..//DATA//2_IrisSpecies.csv")     #DATA\2_IrisSpecies.csv                
            print(df)
            Flores=df.to_dict('records')
            print(Flores)
            insertIris(Flores)

            click=input("Press to continue...")
        elif opcion == 4:   
        
            print(show_all_Iris("iris"))

            click=input("Press to continue...")
        elif opcion == 5:      

            if existeDataBase():
                print("SI")
            else:
                print("NO")
            #     actualizar('notas', 5.2, 'María Castro')

            click=input("Press to continue...")
        elif opcion == 6: 

            print(existeTabla("iris"))
    

            #     filtrar("notas", "grades", 5.0, 6.5)

            #     click=input("Press to continue...")
            # elif opcion == 7:
                
            #     unirTablas("notas", 'DOS')
                
            #     click=input("Press to continue...")
            # elif opcion == 8:
                
            #     delete('notas', "Pedro López")

            #     click=input("Press to continue...")
        elif opcion == 99:
            break
        else:
            print("por favor, escriba una opción correcta. ")
            print("\n")

#funcion_menu()
            
