# Para ejecutar usaremos streamlit run <nombre del script> :streamlit run dashboard.py
import matplotlib.pyplot as plt
import pandas as pd
#import plotly.figure_factory as ff
import plotly.express as px
import seaborn as sns
import streamlit as st
#from PIL import Image

st.write("Práctica DashBoard - Rosana Longares & Javier López")

# image = Image.open('..//DATA//irisris.png')
# st.image(image, caption='FLOR IRIS')
df = pd.read_csv("..//DATA//2_IrisSpecies.csv")
df=df.drop('Id', axis=1) 

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
#st.pyplot(df.SepalLengthCm, df.Species, color = "red")

# st.title("2.PREDICCIÓN")


# import joblib
# from PIL import Image

# #Loading Our final trained Knn model 
# model= open("..//DATA//Clasificador_Svc.pkl", "rb")
# Svc_clf=joblib.load(model)


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
# 	prediction = Svc_clf.predict(input_variables)
# 	if prediction == 1.0:
# 		st.image(setosa)
# 	elif prediction == 2.0: st.image(versicolor)  
# 	else: st.image(virginica) 

st.title("2.GRÁFICOS DE LOS DATOS DEL IRIS DATASET")

MAINcheckBOX = st.sidebar.radio("Elige Gráfico a Mostrar", ["PAIRPLOT","PAIRPLOT HISTOGRAMA", "DISPERSIÓN", "VIOLINES","HISTOGRAMA","KDEPLOT","BOXPLOT","FACETGRID", "FACETGRID_DISPERSION","CLASIFICACION PIE CHART", "CORRELACION PLOT", "SERIES_TIEMPO", "CLASIFICACION SENCILLA"])
if MAINcheckBOX == "PAIRPLOT":
	st.markdown("PAIRPLOT")
	st.markdown("VISUALIZAMOS TODO EL IRIS DATASET")
	fig=sns.pairplot(df, hue="Species")
	st.pyplot(fig)
elif MAINcheckBOX == "PAIRPLOT HISTOGRAMA":
	st.markdown("VISUALIZAMOS SPECIES CON HISTOGRAMA")	 
	g = sns.pairplot(df, hue="Species", diag_kind="hist")
	st.pyplot(g)
elif MAINcheckBOX == "DISPERSIÓN":
	st.markdown("DISPERSIÓN")
	fig = px.scatter(df, x= "SepalWidthCm", y= "SepalLengthCm", color= "Species", size= "PetalLengthCm", hover_data=["PetalWidthCm"])
	fir = px.scatter(df, x= "PetalWidthCm", y= "PetalLengthCm", color= "Species", size= "SepalLengthCm", hover_data=["SepalWidthCm"])

	DISPERSION =  st.sidebar.selectbox("GRÁFICOS DE DISPERSIÓN", ("GRÁFICO DE DISPERSIÓN SEPALOS", "GRÁFICO DE DISPERSIÓN PETALOS"))

	if DISPERSION == "GRÁFICO DE DISPERSIÓN SEPALOS":
		st.markdown("GRÁFICO DE DISPERSIÓN SEPALOS")
		st.plotly_chart(fig)
	elif DISPERSION == "GRÁFICO DE DISPERSIÓN PETALOS":
		st.markdown("GRÁFICO DE DISPERSIÓN PETALOS")
		st.plotly_chart(fir)

elif MAINcheckBOX == "VIOLINES":
	st.markdown("VIOLINES")
		
	#VIOLINES
	vi1 = plt.figure(figsize=(9,7))
	sns.violinplot(y='Species', x='PetalLengthCm', data=df, inner='quartile')
	vi2 = plt.figure(figsize=(9,7))
	sns.violinplot(y='Species', x='PetalWidthCm', data=df, inner='quartile')
	vi3 = plt.figure(figsize=(9,7)) 
	sns.violinplot(y='Species', x='SepalLengthCm', data=df, inner='quartile')
	vi4 = plt.figure(figsize=(9,7))
	sns.violinplot(y='Species', x='SepalWidthCm', data=df, inner='quartile')

	Violin = st.sidebar.selectbox("GRÁFICOS DE VIOLINES", ("ESPECIES Y EL ANCHO DEL PETALO", "ESPECIES Y EL LARGO DEL PETALO",
	"ESPECIES Y EL LARGO DEL SEPALO", "ESPECIES Y EL ANCHO DEL SEPALO"))

	if Violin == "ESPECIES Y EL ANCHO DEL PETALO":
		st.write("ESPECIES Y EL ANCHO DEL PETALO")
		st.pyplot(vi2)
	elif Violin == "ESPECIES Y EL LARGO DEL PETALO":
		st.write("ESPECIES Y EL LARGO DEL PETALO")
		st.pyplot(vi1)
		
	elif Violin == "ESPECIES Y EL ANCHO DEL SEPALO":
		st.write("ESPECIES Y EL ANCHO DEL SEPALO")
		st.pyplot(vi4)
	elif Violin == "ESPECIES Y EL LARGO DEL SEPALO":
		st.write("ESPECIES Y EL LARGO DEL SEPALO")
		st.pyplot(vi3)

elif MAINcheckBOX == "HISTOGRAMA":
	st.markdown("HISTOGRAMA")
	
	fig1 = plt.figure(figsize=(9,7))
	sns.histplot(data= df, x = 'PetalLengthCm', hue = "Species", multiple = "stack")

	fig2 = plt.figure(figsize=(9,7))
	sns.histplot(data= df, x = 'PetalWidthCm', hue = "Species", multiple = "stack")

	fig3 = plt.figure(figsize=(9,7))
	sns.histplot(data= df, x = 'SepalLengthCm', hue = "Species", multiple = "stack")

	fig4 = plt.figure(figsize=(9,7))
	sns.histplot(data= df, x = 'SepalWidthCm', hue = "Species", multiple = "stack")

	HISTOGRAMA =  st.sidebar.selectbox("HISTOGRAMA", ("ESPECIES Y EL ANCHO DEL PETALO", "ESPECIES Y EL LARGO DEL PETALO",
	"ESPECIES Y EL LARGO DEL SEPALO", "ESPECIES Y EL ANCHO DEL SEPALO"))
	if HISTOGRAMA == "ESPECIES Y EL LARGO DEL PETALO":
		plt.title("ESPECIES Y EL LARGO DEL PETALO")
		st.pyplot(fig1)
	elif HISTOGRAMA == "ESPECIES Y EL ANCHO DEL PETALO":
		plt.title("ESPECIES Y EL ANCHO DEL PETALO")
		st.pyplot(fig2)
	elif HISTOGRAMA == "ESPECIES Y EL ANCHO DEL SEPALO":
		plt.title("ESPECIES Y EL ANCHO DEL SEPALO")
		st.pyplot(fig4)	
	elif HISTOGRAMA == "ESPECIES Y EL LARGO DEL SEPALO":
		plt.title("ESPECIES Y EL LARGO DEL SEPALO")
		st.pyplot(fig3)

elif MAINcheckBOX == "KDEPLOT":
	st.markdown("KDEPLOT")
	fig11 = plt.figure(figsize=(9,7))
	sns.kdeplot(data= df, x = 'PetalLengthCm', hue = "Species", multiple = "stack")

	fig22 = plt.figure(figsize=(9,7))
	sns.kdeplot(data= df, x = 'PetalWidthCm', hue = "Species", multiple = "stack")

	fig33 = plt.figure(figsize=(9,7))
	sns.kdeplot(data= df, x = 'SepalLengthCm', hue = "Species", multiple = "stack")

	fig44 = plt.figure(figsize=(9,7))
	sns.kdeplot(data= df, x = 'SepalWidthCm', hue = "Species", multiple = "stack")

	KDEPLOT =  st.sidebar.selectbox("KDEPLOT", ("ESPECIES Y EL ANCHO DEL PETALO", "ESPECIES Y EL LARGO DEL PETALO",
	"ESPECIES Y EL LARGO DEL SEPALO", "ESPECIES Y EL ANCHO DEL SEPALO"))
	if KDEPLOT  == "ESPECIES Y EL LARGO DEL PETALO":
		plt.title("ESPECIES Y EL LARGO DEL PETALO")
		st.pyplot(fig11)
	elif KDEPLOT  == "ESPECIES Y EL ANCHO DEL PETALO":
		plt.title("ESPECIES Y EL ANCHO DEL PETALO")
		st.pyplot(fig22)
	elif KDEPLOT  == "ESPECIES Y EL ANCHO DEL SEPALO":
		plt.title("ESPECIES Y EL ANCHO DEL SEPALO")
		st.pyplot(fig44)	
	elif KDEPLOT  == "ESPECIES Y EL LARGO DEL SEPALO":
		plt.title("ESPECIES Y EL LARGO DEL SEPALO")
		st.pyplot(fig33)
elif MAINcheckBOX == "BOXPLOT":
	st.markdown("BOXPLOT")
	setosa = df[df["Species"] == "Iris-setosa"]
	versicolor = df[df["Species"] == "Iris-versicolor"]
	virginica = df[df["Species"] == "Iris-virginica"] 



	fig50 = plt.figure(figsize=(9,7))
	setosa.boxplot(column=["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"])
	fig60 = plt.figure(figsize=(9,7))
	versicolor.boxplot(column=["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"])
	fig70 = plt.figure(figsize=(9,7))
	virginica.boxplot(column=["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"])

	BOXPLOT = st.sidebar.radio("BOXPLOT POR ESPECIES", ["IRIS-SETOSA", "IRIS-VERSICOLOR", "IRIS-VIRGINICA"])
	if BOXPLOT == "IRIS-SETOSA":
		st.markdown("BOXPLOT DE IRIS-SETOSA")
		st.pyplot(fig50)
	elif BOXPLOT == "IRIS-VERSICOLOR":
		st.markdown("BOXPLOT DE IRIS-VERSICOLOR")
		st.pyplot(fig60)
	elif BOXPLOT == "IRIS-VIRGINICA":
		st.markdown("BOXPLOT DE IRIS-VIRGINICA")
		st.pyplot(fig70)	

elif MAINcheckBOX == "FACETGRID":
	st.markdown("FACETGRID")


	plat = sns.FacetGrid(df, hue="Species")
	plat.map(sns.distplot, "SepalLengthCm").add_legend()
	plet = sns.FacetGrid(df, hue="Species")
	plet.map(sns.distplot, "SepalWidthCm").add_legend()
	plit = sns.FacetGrid(df, hue="Species")
	plit.map(sns.distplot, "PetalLengthCm").add_legend()
	plut = sns.FacetGrid(df, hue="Species")
	plut.map(sns.distplot, "PetalWidthCm").add_legend()

	FACETGRID = st.sidebar.radio("FACETGRID", ["FACETGRID PARA EL LARGO DEL SÉPALO", "FACETGRID PARA EL ANCHO DEL SÉPALO", "FACETGRID PARA EL LARGO DEL PÉTALO", "FACETGRID PARA EL ANCHO DEL PÉTALO"])

	if FACETGRID == "FACETGRID PARA EL LARGO DEL SÉPALO":
		st.pyplot(plat)
	elif FACETGRID == "FACETGRID PARA EL ANCHO DEL SÉPALO":
		st.pyplot(plet)
	elif FACETGRID == "FACETGRID PARA EL LARGO DEL PÉTALO":
		st.pyplot(plit)
	elif FACETGRID == "FACETGRID PARA EL ANCHO DEL PÉTALO":
		st.pyplot(plut)	

elif MAINcheckBOX == "FACETGRID_DISPERSION":
	st.markdown("FACETGRID DISPERSION")
	gub = sns.FacetGrid(df, hue="Species", height=6.4).map(plt.scatter, "PetalLengthCm", "PetalWidthCm")
	geb = sns.FacetGrid(df, hue="Species", height=6.4).map(plt.scatter, "SepalLengthCm", "SepalWidthCm")
	
	FACETGRID_DISPERSION = st.sidebar.radio("FACETGRID DISPERSION",["FACETGRID DISPERSION PARA EL PÉTALO", "FACETGRID DISPERSION PARA EL SÉPALO"])
    
	if FACETGRID_DISPERSION == "FACETGRID DISPERSION PARA EL SÉPALO":
		st.pyplot(geb)
	elif FACETGRID_DISPERSION == "FACETGRID DISPERSION PARA EL PÉTALO":
		st.pyplot(gub)

elif MAINcheckBOX == "CLASIFICACION PIE CHART":
	st.markdown("CLASIFICACION PIE CHART")
	st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
	st.pyplot()
	st.write(df.iloc[:,-1].value_counts())	

elif MAINcheckBOX == "CORRELACION PLOT":
	st.markdown("CORRELACION PLOT")
	st.write("### Heatmap")
	fig, ax = plt.subplots(figsize=(10,10))
	st.write(sns.heatmap(df.corr(), annot=True,linewidths=0.5))
	st.pyplot() 


elif MAINcheckBOX  == "SERIES_TIEMPO":
	st.markdown("SeriesTiempo")
	columns = df.columns.tolist()
	df.set_index(columns[0], inplace=True)
	if st.checkbox("Plot Time Series Data"):
		st.write("#### Select type of plot: ")
		plot_type = st.selectbox("", ["area", "line", "bar"])
		if st.button("Generate"):
			if plot_type == "area":
				st.area_chart(df)
			if plot_type == "line":
				st.line_chart(df)
			if plot_type == "bar":
				st.bar_chart(df)

elif MAINcheckBOX == "CLASIFICACION SENCILLA":
	st.markdown("Classification")
	st.write("#### Select column to visualize: ")
	columns = df.columns.tolist()
	class_name = columns[-1]
	column_name = st.selectbox("",columns)
	st.write("#### Select type of plot: ")
	plot_type = st.selectbox("Select info", ["kde", "box", "violin", "swarm"])
	generate = st.button("Generate")
	if generate:
		if plot_type == "kde":
			st.write(sns.FacetGrid(df, hue=class_name, palette="husl", height=6).map(sns.kdeplot, column_name).add_legend())
			st.pyplot()
		if plot_type == "box":
			st.write(sns.boxplot(x=class_name, y=column_name, palette="husl", data=df))
			st.pyplot()
		if plot_type == "violin":
			st.write(sns.violinplot(x=class_name, y=column_name, palette="husl", data=df))
			st.pyplot()
		if plot_type == "swarm":
			st.write(sns.swarmplot(x=class_name, y=column_name, data=df,color="y", alpha=0.9))
			st.pyplot()