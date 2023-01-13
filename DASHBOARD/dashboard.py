# Para ejecutar usaremos streamlit run <nombre del script> :streamlit run dashboard.py

# import pandas as pd
# import matplotlib.pyplot as plt
# import plotly.figure_factory as ff
# import plotly.express as px
# import seaborn as sns
import streamlit as st
from PIL import Image


st.set_page_config(
    layout="wide",
    page_title="IRIS DASHBOARD & PREDICCIÓN",
    page_icon="❃",
)

st.write("Práctica DashBoard - Rosana Longares & Javier López")

st.write("# IRIS DASHBOARD ❃")

image = Image.open('..//DATA//irisris.png')
st.image(image, caption='FLOR IRIS')
# df = pd.read_csv("..//DATA//2_IrisSpecies.csv")  

# st.title("Iris AGAIN!!")
# st.title("1.ANALISIS DE LOS DATOS DEL IRIS DATASET")

# opciones = st.sidebar.radio("ANALIZANDO LOS DATOS",	["IRIS DATASET","DATOS ESTADISTICOS", "TABLA DEL IRIS DATASET","TAMAÑO DEL IRIS DATASET", 
# "TIPOS DE ESPECIES Y CANTIDAD"])

# if opciones == "IRIS DATASET":
# 	st.write("*********** IRIS DATASET ***********")
# 	st.dataframe(df)
# elif opciones == "TAMAÑO DEL IRIS DATASET":
# 	st.write("El tamaño del Dataset es:", df.shape, df.Species== "Iris-setosa")
# elif opciones == "TABLA DEL IRIS DATASET":
# 	st.write("Tabla del Iris Dataset")
# 	st.table(df)
# elif opciones == "TIPOS DE ESPECIES Y CANTIDAD":
# 	st.write("Tipos de Especies y Cantidad", df["Species"].value_counts())
# elif opciones == "DATOS ESTADISTICOS":
# 	st.write("************* Datos Estadisticos ***************", df.describe())


# st.write("Podemos plotear un gráfico de barras")
# st.bar_chart(df.SepalLengthCm)
# #st.pyplot(df.SepalLengthCm, df.Species, color = "red")

# st.title("2.PREDICCIÓN")


# import joblib
# from PIL import Image

# #Loading Our final trained Knn model 
# model= open("..//DATA//Clasificador_Knn.pkl", "rb")
# knn_clf=joblib.load(model)


# st.title("Iris flower species Classification App")

# #Loading images

# setosa= Image.open('..//DATA//setosa.png')
# versicolor= Image.open('..//DATA//versicolor.png')
# virginica = Image.open('..//DATA//virginica.png')

# st.sidebar.title("Features")

# #Intializing
# parameter_list=['Sepal length (cm)','Sepal Width (cm)','Petal length (cm)','Petal Width (cm)']
# parameter_input_values=[]
# parameter_default_values=['5.2','3.2','4.2','1.2']

# values=[]

# #Display
# for parameter, parameter_df in zip(parameter_list, parameter_default_values):
	
# 	values= st.sidebar.slider(label=parameter, key=parameter,value=float(parameter_df), min_value=0.0, max_value=8.0, step=0.1)
# 	#st.write(values)
# 	parameter_input_values.append(values)
	
# input_variables=pd.DataFrame([parameter_input_values],columns=parameter_list,dtype=float)
# st.write('\n\n')

# if st.button("Click Here to Classify"):
# 	prediction = knn_clf.predict(input_variables)
# 	if prediction == 1.0:
# 		st.image(setosa)
# 	elif prediction == 2.0: st.image(versicolor)  
# 	else: st.image(virginica) 
	 
# st.title("3.GRÁFICOS DE LOS DATOS DEL IRIS DATASET")

# st.markdown("VISUALIZAMOS TODO EL IRIS DATASET")
# fig=sns.pairplot(df, hue="Species")
# st.pyplot(fig)
	 
# st.markdown("VISUALIZAMOS SPECIES CON HISTOGRAMA")	 
# g = sns.pairplot(df, hue="Species", diag_kind="hist")
# st.pyplot(g)

# fig = px.scatter(df, x= "SepalWidthCm", y= "SepalLengthCm", color= "Species", size= "PetalLengthCm", hover_data=["PetalWidthCm"])
# fir = px.scatter(df, x= "PetalWidthCm", y= "PetalLengthCm", color= "Species", size= "SepalLengthCm", hover_data=["SepalWidthCm"])


# DISPERSION =  st.sidebar.selectbox("GRÁFICOS DE DISPERSIÓN", ("GRÁFICO DE DISPERSIÓN SEPALOS", "GRÁFICO DE DISPERSIÓN PETALOS"))

# if DISPERSION == "GRÁFICO DE DISPERSIÓN SEPALOS":
# 	st.markdown("GRÁFICO DE DISPERSIÓN SEPALOS")
# 	st.plotly_chart(fig)
# elif DISPERSION == "GRÁFICO DE DISPERSIÓN PETALOS":
# 	st.markdown("GRÁFICO DE DISPERSIÓN PETALOS")
# 	st.plotly_chart(fir)

# #VIOLINES
# vi1 = plt.figure(figsize=(9,7))
# sns.violinplot(y='Species', x='PetalLengthCm', data=df, inner='quartile')
# vi2 = plt.figure(figsize=(9,7))
# sns.violinplot(y='Species', x='PetalWidthCm', data=df, inner='quartile')
# vi3 = plt.figure(figsize=(9,7)) 
# sns.violinplot(y='Species', x='SepalLengthCm', data=df, inner='quartile')
# vi4 = plt.figure(figsize=(9,7))
# sns.violinplot(y='Species', x='SepalWidthCm', data=df, inner='quartile')



# Violin = st.sidebar.selectbox("GRÁFICOS DE VIOLINES", ("ESPECIES Y EL ANCHO DEL PETALO", "ESPECIES Y EL LARGO DEL PETALO",
# "ESPECIES Y EL LARGO DEL SEPALO", "ESPECIES Y EL ANCHO DEL SEPALO"))

# if Violin == "ESPECIES Y EL ANCHO DEL PETALO":
# 	st.write("ESPECIES Y EL ANCHO DEL PETALO")
# 	st.pyplot(vi2)
# elif Violin == "ESPECIES Y EL LARGO DEL PETALO":
# 	st.write("ESPECIES Y EL LARGO DEL PETALO")
# 	st.pyplot(vi1)
	
# elif Violin == "ESPECIES Y EL ANCHO DEL SEPALO":
# 	st.write("ESPECIES Y EL ANCHO DEL SEPALO")
# 	st.pyplot(vi4)
# elif Violin == "ESPECIES Y EL LARGO DEL SEPALO":
# 	st.write("ESPECIES Y EL LARGO DEL SEPALO")
# 	st.pyplot(vi3)

# fig1 = plt.figure(figsize=(9,7))
# sns.histplot(data= df, x = 'PetalLengthCm', hue = "Species", multiple = "stack")

# fig2 = plt.figure(figsize=(9,7))
# sns.histplot(data= df, x = 'PetalWidthCm', hue = "Species", multiple = "stack")

# fig3 = plt.figure(figsize=(9,7))
# sns.histplot(data= df, x = 'SepalLengthCm', hue = "Species", multiple = "stack")

# fig4 = plt.figure(figsize=(9,7))
# sns.histplot(data= df, x = 'SepalWidthCm', hue = "Species", multiple = "stack")

# HISTOGRAMA =  st.sidebar.selectbox("HISTOGRAMA", ("ESPECIES Y EL ANCHO DEL PETALO", "ESPECIES Y EL LARGO DEL PETALO",
# "ESPECIES Y EL LARGO DEL SEPALO", "ESPECIES Y EL ANCHO DEL SEPALO"))
# if HISTOGRAMA == "ESPECIES Y EL LARGO DEL PETALO":
# 	plt.title("ESPECIES Y EL LARGO DEL PETALO")
# 	st.pyplot(fig1)
# elif HISTOGRAMA == "ESPECIES Y EL ANCHO DEL PETALO":
# 	plt.title("ESPECIES Y EL ANCHO DEL PETALO")
# 	st.pyplot(fig2)
# elif HISTOGRAMA == "ESPECIES Y EL ANCHO DEL SEPALO":
# 	plt.title("ESPECIES Y EL ANCHO DEL SEPALO")
# 	st.pyplot(fig4)	
# elif HISTOGRAMA == "ESPECIES Y EL LARGO DEL SEPALO":
# 	plt.title("ESPECIES Y EL LARGO DEL SEPALO")
# 	st.pyplot(fig3)


# fig11 = plt.figure(figsize=(9,7))
# sns.kdeplot(data= df, x = 'PetalLengthCm', hue = "Species", multiple = "stack")

# fig22 = plt.figure(figsize=(9,7))
# sns.kdeplot(data= df, x = 'PetalWidthCm', hue = "Species", multiple = "stack")

# fig33 = plt.figure(figsize=(9,7))
# sns.kdeplot(data= df, x = 'SepalLengthCm', hue = "Species", multiple = "stack")

# fig44 = plt.figure(figsize=(9,7))
# sns.kdeplot(data= df, x = 'SepalWidthCm', hue = "Species", multiple = "stack")

# KDEPLOT =  st.sidebar.selectbox("KDEPLOT", ("ESPECIES Y EL ANCHO DEL PETALO", "ESPECIES Y EL LARGO DEL PETALO",
# "ESPECIES Y EL LARGO DEL SEPALO", "ESPECIES Y EL ANCHO DEL SEPALO"))
# if KDEPLOT  == "ESPECIES Y EL LARGO DEL PETALO":
# 	plt.title("ESPECIES Y EL LARGO DEL PETALO")
# 	st.pyplot(fig11)
# elif KDEPLOT  == "ESPECIES Y EL ANCHO DEL PETALO":
# 	plt.title("ESPECIES Y EL ANCHO DEL PETALO")
# 	st.pyplot(fig22)
# elif KDEPLOT  == "ESPECIES Y EL ANCHO DEL SEPALO":
# 	plt.title("ESPECIES Y EL ANCHO DEL SEPALO")
# 	st.pyplot(fig44)	
# elif KDEPLOT  == "ESPECIES Y EL LARGO DEL SEPALO":
# 	plt.title("ESPECIES Y EL LARGO DEL SEPALO")
# 	st.pyplot(fig33)