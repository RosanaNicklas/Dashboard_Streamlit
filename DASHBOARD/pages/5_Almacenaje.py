import time

import CRUD as crud
import datasettings
import hydralit_components as hc
import pandas as pd
import psycopg2.errors
import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="❃ IRIS DATABASE",
)


st.header('CHECKING DATABASE...')



bd=datasettings.DATABASE
opciones=""

with st.expander("DATABASE CHECK..."):    
    
    c1, c2 ,c3 = st.columns(3)
    if datasettings.ENTORNO==datasettings.ENTORNOJAVI or datasettings.ENTORNOROSANA:
        
        c1.info("Acceso: Usuario Local -> Usaremos Bases de Datos")
        
        hp=c2.empty()   
        check = c2.checkbox("Check")

        if not check:#button("Check"):
            hp.empty()
        else:
            with hc.HyLoader('',hc.Loaders.standard_loaders,index=5):
            #with hc.HyLoader('...',hc.Loaders.pretty_loaders,index=11):#[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
                time.sleep(1)
            if crud.existeDataBase():  
                c3.success("Database exists correctly........")
            else: 
                c3.error("Database doesn't exist!!!")

with st.expander("DATABASE OPTIONS..."):  
    c4, c5 ,c6 = st.columns(3)    
    c7, c8 ,c9 = st.columns(3)
    opciones = c4.radio("Elige opción..",	["COMPROBAR BBDD","CREAR BBDD","COMPROBAR TABLA IRIS","CREAR TABLA IRIS", "INSERTAR IRISDATASET EN BBDD","MOSTRAR TABLA IRIS","ELIMINAR FILAS IRIS","ELIMINAR TABLA IRIS"])

    if opciones=="COMPROBAR BBDD":
        if crud.existeDataBase():
            c5.success(f"{bd} Database exists correctly........")
        else: c5.warning(f"{bd} Database doesn't exist!!!...")
    elif opciones == "CREAR BBDD":
        creacion=crud.createDatabase(bd)
        if type(creacion)==psycopg2.errors.DuplicateDatabase:
            c5.error(creacion)
        else:
            c5.success(creacion)
    elif opciones == "CREAR TABLA IRIS":
        creacion=crud.createTabla(datasettings.IRISTABLE)
        if type(creacion)==psycopg2.errors.DuplicateTable:
            c5.error(creacion)
        else:
            c5.success(creacion)
    elif opciones == "INSERTAR IRISDATASET EN BBDD":
        df = pd.read_csv("..//DATA//2_IrisSpecies.csv")     #DATA\2_IrisSpecies.csv   
        Flores=df.to_dict('records')
        llenado=crud.insertIris(Flores)
        if type(llenado)==psycopg2.errors.UniqueViolation:
            c5.warning(llenado)
        else:
            c5.success(llenado)
    elif opciones == "MOSTRAR TABLA IRIS":
        st.write(crud.show_All_Tabla(datasettings.IRISTABLE))
    elif opciones == "ELIMINAR FILAS IRIS":
        opcion=c5.selectbox("Elige columna..",	datasettings.IRISCOLLIST)
        valor=c6.text_input("...valor")
        if c5.button("¿Seguro?"):
            if opcion==datasettings.IRISCOL6:
                valor=f"'{valor}'"
            c8.info(crud.delete_Tabla(datasettings.IRISTABLE,opcion,valor))
    elif opciones=="ELIMINAR TABLA IRIS":
        if c5.button("¿Seguro?"):
            c8.info(crud.delete_All_Tabla(datasettings.IRISTABLE))
    elif opciones=="COMPROBAR TABLA IRIS":
        if crud.existeTabla(datasettings.IRISTABLE):
            c5.success(f"{datasettings.IRISTABLE} Table exists correctly........")
        else: c5.warning(f"{datasettings.IRISTABLE} Table doesn't exist!!!...")

with st.expander("PREDICTIONS OPTIONS..."):  
    c10, c11 ,c12 = st.columns(3)    
    c13, c14 ,c15 = st.columns(3)
    opciones = c10.radio("Elige opción..",	["COMPROBAR TABLA RESULTADOS","CREAR TABLA RESULTADOS", "MOSTRAR TABLA RESULTADOS","ELIMINAR FILAS RESULTADOS","ELIMINAR TABLA RESULTADOS"])

    if opciones == "CREAR TABLA RESULTADOS":
        creacion=crud.createTabla(datasettings.RESULTSTABLE)
        if type(creacion)==psycopg2.errors.DuplicateTable:
            c11.error(creacion)
        else:
            c11.success(creacion)
    elif opciones == "MOSTRAR TABLA RESULTADOS":
        st.write(crud.show_All_Tabla(datasettings.RESULTSTABLE))
    elif opciones == "ELIMINAR FILAS RESULTADOS":
        opcion=c11.selectbox("Elige columna..",	datasettings.RESULTSCOLLIST)
        valor=c12.text_input("...valor")
        if c11.button("¿Seguro?"):
            if opcion==datasettings.RESULTSCOL6:
                valor=f"'{valor}'"
            c14.info(crud.delete_Tabla(datasettings.IRISTABLE,opcion,valor))
    elif opciones=="ELIMINAR TABLA RESULTADOS":
        if c11.button("¿Seguro?"):
            c14.info(crud.delete_All_Tabla(datasettings.RESULTSTABLE))
    elif opciones=="COMPROBAR TABLA RESULTADOS":
        if crud.existeTabla(datasettings.RESULTSTABLE):
            c11.success(f"{datasettings.RESULTSTABLE} Table exists correctly........")
        else: c11.warning(f"{datasettings.RESULTSTABLE} Table doesn't exist!!!...")









