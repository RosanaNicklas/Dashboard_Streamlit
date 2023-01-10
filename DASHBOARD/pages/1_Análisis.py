# Para ejecutar usaremos streamlit run <nombre del script> :streamlit run dashboard.py

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import io
#import plotly.express as px
import seaborn as sns
from PIL import Image

st.write("Práctica DashBoard - Rosana Longares & Javier López")
image = Image.open('..//DATA//iris4.png')
st.image(image, caption='FLOR IRIS')

df = pd.read_csv("..//DATA//2_IrisSpecies.csv")  
df=df.drop('Id', axis=1) 

st.title("1.ANALISIS DE LOS DATOS DEL IRIS DATASET")

option = st.selectbox("ANALIZANDO LOS DATOS", ["Selecciona una opción...","Análisis Datos Globales","Análisis Datos Específicos", "Dataset por filas", "Dataset por columnas", "Seleccionando columnas"])

if option == "Análisis Datos Globales":
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
		st.write("Información")
		
		buffer = io.StringIO()
		df.info(buf=buffer)
		s = buffer.getvalue()

		st.text(s) 

elif option == "Análisis Datos Específicos":
	opciones = st.sidebar.radio("ELEGIR DATOS ESPECIFICOS PARA ANALIZAR",["Especies", "Petalos&Sepalos"])
	setosa = df[df["Species"] == "Iris-setosa"]
	versicolor = df[df["Species"] == "Iris-versicolor"]
	virginica = df[df["Species"] == "Iris-virginica"] 

	setosap = setosa.iloc[:,3:4]
	setosas = setosa.iloc[:,1:2]
	versicolorp = versicolor.iloc[:,3:4]
	versicolors = versicolor.iloc[:,1:2]
	virginicas = virginica.iloc[:,1:2]
	virginicap = virginica.iloc[:,3:4]
	if opciones == "Especies":
		ESPECIES = st.sidebar.radio("SELECCIONAR DATOS POR ESPECIES", ["IRIS-SETOSA", "IRIS-VERSICOLOR", "IRIS-VIRGINICA"])
		if ESPECIES == "IRIS-SETOSA":
			st.table(setosa)
		elif ESPECIES == "IRIS-VERSICOLOR":
			st.table(versicolor)
		elif ESPECIES == "IRIS-VIRGINICA":
			st.table(virginica)	

		
	elif opciones == "Petalos&Sepalos":
		print("Estamos en Petalos....######")
		PETALOSANDSEPALOS = st.sidebar.selectbox("SELECCIONAR DATOS POR PETALOS Y SEPALOS", ("IRIS-SETOSA PETALOS", "IRIS-SETOSA SEPALOS", "IRIS-VERSICOLOR PETALOS", "IRIS-VERSICOLOR SEPALOS", "IRIS-VIRGINICA PETALOS", "IRIS-VIRGINICA PETALOS"))
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
			st.table(virginicas)

elif option == "Dataset por filas":
	
    st.write("Introduce el numero de filas a ver")
    rows = st.number_input("", min_value=0,value=150)
    if rows > 0:
        st.dataframe(df.head(rows))

elif option == "Dataset por columnas":
	
    st.write("Introduce el numero de columnas a ver")
    columns = st.number_input("", min_value=0,value=5)
    if columns > 0:
        st.dataframe(df.head(columns))

elif option == "Seleccionando columnas":
	
    columns = df.columns.tolist()
    st.write("#### Selecciona las columnas a mostrar:")
    selected_cols = st.multiselect("", columns)
    if len(selected_cols) > 0:
        selected_df = df[selected_cols]
        st.dataframe(selected_df)

