import joblib
from PIL import Image
import streamlit as st
import pandas as pd

st.write("Práctica DashBoard - Rosana Longares & Javier López")

st.title("4.PREDICCIÓN")


#Loading Our final trained Knn model 
model= open("..//DATA//Clasificador_Svc.pkl", "rb")
Svc_clf=joblib.load(model)


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
	prediction = Svc_clf.predict(input_variables)
	if prediction == 1.0:
		st.image(setosa)
	elif prediction == 2.0: st.image(versicolor)  
	else: st.image(virginica) 
	 