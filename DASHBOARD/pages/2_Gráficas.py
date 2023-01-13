# Para ejecutar usaremos streamlit run <nombre del script> :streamlit run dashboard.py
import CRUD as crud
import datasettings
import matplotlib.pyplot as plt
import pandas as pd
#import plotly.figure_factory as ff
import plotly.express as px
import seaborn as sns
import streamlit as st

#from PIL import Image
st.set_option('deprecation.showPyplotGlobalUse', False)

st.write("Práctica DashBoard - Rosana Longares & Javier López")


if datasettings.ENTORNOLOCAL:#datasettings.ENTORNO==datasettings.ENTORNOJAVI or datasettings.ENTORNOROSANA:
	#st.info(datasettings.ENTORNOLOCAL)
	st.info("Datos Cargados de BBDD...")
	df=crud.show_All_Tabla(datasettings.IRISTABLE)
else:
	st.info("Datos Cargandos de CSV...")
	df = pd.read_csv("..//DATA//2_IrisSpecies.csv")  

df=df.drop(datasettings.IRISCOL1, axis=1) 


st.title("2.GRÁFICOS DE LOS DATOS DEL IRIS DATASET")

MAINcheckBOX = st.sidebar.radio("Elige Gráfico a Mostrar", ["PAIRPLOT","PAIRPLOT HISTOGRAMA", "DISPERSIÓN", "VIOLINES","HISTOGRAMA","KDEPLOT","BOXPLOT","FACETGRID", "FACETGRID_DISPERSION","CLASIFICACION PIE CHART", "CORRELACION PLOT", "CLASIFICACION SENCILLA"])
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