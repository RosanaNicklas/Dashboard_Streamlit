import CRUD as crud
import datasettings
import joblib
import pandas as pd
import psycopg2.errors
import streamlit as st
from PIL import Image

def fun_resultado(prediccion):	
	res=""
	if prediccion == 1.0: res="SETOSA"
	elif prediccion == 2.0: res="VERSICOLOR"
	else: res="VIRGINICA"

	return res
st.write("Práctica DashBoard - Rosana Longares & Javier López")

st.info("Datos Cargados de PKL...")

st.title("4.PREDICCIÓN")

image = Image.open('..//DATA//iris5.png')
st.image(image, caption='FLOR IRIS')
#Loading Our final trained Knn model 
model= open("..//DATA//Clasificador_Svc.pkl", "rb")
Svc_clf=joblib.load(model)


st.title("Predicción - Clasificador de Flores Iris")

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

prediction = Svc_clf.predict(input_variables)
res=""

if st.button("Click Here to Classify"):
	if prediction == 1.0:
		st.image(setosa)
	elif prediction == 2.0: 
		st.image(versicolor)  
	else: 
		st.image(virginica) 

st.info("Datos Cargados/Guardados en BBDD...")
res=fun_resultado(prediction)
with st.expander("PREDICTIONS DATABASE..."):  
		c10, c11 ,c12 = st.columns(3)    
		c13, c14 ,c15 = st.columns(3)
		opciones = c10.radio("Elige opción..",	["COMPROBAR TABLA RESULTADOS","CREAR TABLA RESULTADOS","INSERTAR TABLA RESULTADOS", "MOSTRAR TABLA RESULTADOS","ELIMINAR FILAS RESULTADOS","ELIMINAR TABLA RESULTADOS"])

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
		elif opciones=="INSERTAR TABLA RESULTADOS":
			if c11.button("¿Seguro?"):
				c14.info(crud.insertar(datasettings.RESULTSTABLE,0,parameter_input_values[2],parameter_input_values[3],parameter_input_values[0],parameter_input_values[1],res))
	 