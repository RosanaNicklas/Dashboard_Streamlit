# Para ejecutar usaremos streamlit run <nombre del script> :streamlit run dashboard.py

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

st.write("Práctica DashBoard - Rosana Longares & Javier López")

df = pd.read_csv("..//DATA//2_IrisSpecies.csv")  

st.title("1.ANALISIS DE LOS DATOS DEL IRIS DATASET")


fig45 = plt.figure(figsize=(9,7))
sns.heatmap(df.corr(), annot=True)
opciones = st.sidebar.radio("ANALIZANDO LOS DATOS",	["IRIS DATASET","INFORMACIÓN", "TABLA DEL IRIS DATASET","DATOS ESTADISTICOS","TAMAÑO DEL IRIS DATASET", 
"TIPOS DE ESPECIES Y CANTIDAD", "CORRELACIÓN"])

if opciones == "IRIS DATASET":
	st.write("*********** IRIS DATASET ***********")
	st.dataframe(df)
elif opciones == "TAMAÑO DEL IRIS DATASET":
	st.write("El tamaño del Dataset es:", df.shape)
elif opciones == "TABLA DEL IRIS DATASET":
	st.write("Tabla del Iris Dataset")
	st.table(df)
elif opciones == "TIPOS DE ESPECIES Y CANTIDAD":
	st.write("Tipos de Especies y Cantidad", df["Species"].value_counts())
elif opciones == "DATOS ESTADISTICOS":
	st.write("************* Datos Estadisticos ***************", df.describe())
elif opciones == "CORRELACIÓN":
	st.pyplot(fig45)
elif opciones == "INFORMACIÓN":
	st.write("Información",df.info())


setosa = df[df["Species"] == "Iris-setosa"]
versicolor = df[df["Species"] == "Iris-versicolor"]
virginica = df[df["Species"] == "Iris-virginica"] 

ESPECIES = st.sidebar.radio("SELECCIONAR DATOS POR ESPECIES", ["IRIS-SETOSA", "IRIS-VERSICOLOR", "IRIS-VIRGINICA"])
if ESPECIES == "IRIS-SETOSA":
	st.table(setosa)
elif ESPECIES == "IRIS-VERSICOLOR":
	st.table(versicolor)
elif ESPECIES == "IRIS-VIRGINICA":
	st.table(virginica)	


setosap = setosa.loc[:,3,4]
setosas = setosa.loc[:,1,2]
versicolorp = versicolor.loc[:,3,4]
versicolors = versicolor.loc[:,1,2]
virginicas = virginica.loc[:,1,2]
virginicap = virginica.loc[:,3,4]

"""PETALOSANDSEPALOS = st.sidebar.selectbox("SELECCIONAR DATOS POR PETALOS Y SEPALOS", ("IRIS-SETOSA PETALOS", "IRIS-SETOSA SEPALOS", "IRIS-VERSICOLOR PETALOS", "IRIS-VERSICOLOR SEPALOS", "IRIS-VIRGINICA PETALOS", "IRIS-VIRGINICA PETALOS"))
if PETALOSANDSEPALOS  == "IRIS-SETOSA PETALOS":
	st.table(setosap)
elif PETALOSANDSEPALOS  == "IRIS-SETOSA SEPALOS":
	st.table(setosas)
elif PETALOSANDSEPALOS  == "IRIS-VERSICOLOR PETALOS":
	st.table(versicolorp)
elif PETALOSANDSEPALOS   == "IRIS-VERSICOLOR SEPALOS":
	st.table(versicolors)
elif PETALOSANDSEPALOS   == "IRIS-VIRGINICA PETALOS":
	st.table(virginicap)
elif PETALOSANDSEPALOS  == "IRIS-VIRGINICA SEPALOS":
	st.table(virginicas)"""
