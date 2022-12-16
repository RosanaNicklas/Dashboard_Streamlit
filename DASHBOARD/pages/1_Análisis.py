# Para ejecutar usaremos streamlit run <nombre del script> :streamlit run dashboard.py

import pandas as pd
import streamlit as st

st.write("Práctica DashBoard - Rosana Longares & Javier López")

df = pd.read_csv("..//DATA//2_IrisSpecies.csv")  

st.title("1.ANALISIS DE LOS DATOS DEL IRIS DATASET")

opciones = st.sidebar.radio("ANALIZANDO LOS DATOS",	["IRIS DATASET","DATOS ESTADISTICOS", "TABLA DEL IRIS DATASET","TAMAÑO DEL IRIS DATASET", 
"TIPOS DE ESPECIES Y CANTIDAD"])

if opciones == "IRIS DATASET":
	st.write("*********** IRIS DATASET ***********")
	st.dataframe(df)
elif opciones == "TAMAÑO DEL IRIS DATASET":
	st.write("El tamaño del Dataset es:", df.shape, df.Species== "Iris-setosa")
elif opciones == "TABLA DEL IRIS DATASET":
	st.write("Tabla del Iris Dataset")
	st.table(df)
elif opciones == "TIPOS DE ESPECIES Y CANTIDAD":
	st.write("Tipos de Especies y Cantidad", df["Species"].value_counts())
elif opciones == "DATOS ESTADISTICOS":
	st.write("************* Datos Estadisticos ***************", df.describe())
