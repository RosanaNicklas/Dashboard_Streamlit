# Para ejecutar usaremos streamlit run <nombre del script> :streamlit run dashboard.py

import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.express as px
import seaborn as sns
import streamlit as st

st.write("Práctica DashBoard - Rosana Longares & Javier López")
st.write("Esta es la primera versión para el Iris Dataset...")

df = pd.read_csv("..//DATA//2_IrisSpecies.csv")  

st.title("Iris AGAIN!!")
st.title("1.ANALISIS DE LOS DATOS DEL IRIS DATASET")

opciones = st.sidebar.radio("ANALIZANDO LOS DATOS",	["IRIS DATASET","DATOS ESTADISTICOS", "TABLA DEL IRIS DATASET","TAMAÑO DEL IRIS DATASET", 
"TIPOS DE ESPECIES Y CANTIDAD"])

if opciones == "IRIS DATASET":
	st.write("*********** IRIS DATASET ***********")
	st.dataframe(df)
elif opciones == "TAMAÑO DEL IRIS DATASET":
	st.write("El tamaño del Dataset es:", df.shape)
elif opciones == "TABLA DEL IRIS DATASET":
	st.write("Tabla del Iris Dataset")
	st.table(df)
elif opciones == "TIPOS DE SPECIES Y CANTIDAD":
	st.write("Tipos de Especies y Cantidad", df.Species.value_counts())
elif opciones == "DATOS ESTADISTICOS":
	st.write("************* Datos Estadisticos ***************", df.describe())


st.write("Podemos plotear un gráfico de barras")
st.bar_chart(df.SepalLengthCm)
#st.pyplot(df.SepalLengthCm, df.Species, color = "red")

st.title("2.PREDICCIÓN")


import joblib
from PIL import Image

#Loading Our final trained Knn model 
model= open("..//DATA//Clasificador_Knn.pkl", "rb")
knn_clf=joblib.load(model)


st.title("Iris flower species Classification App")

#Loading images

setosa= Image.open('..//DATA//setosa.png')
versicolor= Image.open('..//DATA//versicolor.png')
virginica = Image.open('..//DATA//virginica.png')

st.sidebar.title("Features")

#Intializing
parameter_list=['Sepal length (cm)','Sepal Width (cm)','Petal length (cm)','Petal Width (cm)']
parameter_input_values=[]
parameter_default_values=['5.2','3.2','4.2','1.2']

values=[]

#Display
for parameter, parameter_df in zip(parameter_list, parameter_default_values):
	
	values= st.sidebar.slider(label=parameter, key=parameter,value=float(parameter_df), min_value=0.0, max_value=8.0, step=0.1)
	#st.write(values)
	parameter_input_values.append(values)
	
input_variables=pd.DataFrame([parameter_input_values],columns=parameter_list,dtype=float)
st.write('\n\n')

if st.button("Click Here to Classify"):
	prediction = knn_clf.predict(input_variables)
	if prediction == 1.0:
		st.image(setosa)
	elif prediction == 2.0: st.image(versicolor)  
	else: st.image(virginica) 
	 
st.title("3.GRÁFICOS DE LOS DATOS DEL IRIS DATASET")

st.markdown("VISUALIZAMOS TODO EL IRIS DATASET")
fig=sns.pairplot(df, hue="Species")
st.pyplot(fig)
	 
st.markdown("VISUALIZAMOS SPECIES CON HISTOGRAMA")	 
g = sns.pairplot(df, hue="Species", diag_kind="hist")
st.pyplot(g)

fig = px.scatter(df, x= "SepalWidthCm", y= "SepalLengthCm", color= "Species", size= "PetalLengthCm", hover_data= "PetalWidthCm")
st.plotly.chart(fig)