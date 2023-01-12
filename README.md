# Dashboard_Streamlit 

Esta es una aplicación web para proyectos de ciencia de datos donde hemos usado la biblioteca Streamlit para hacerla. Los datos utilizados son el famoso conjunto de datos incorporado de la flor de iris.

 En esta variación en los parámetros como la longitud del pétalo, el ancho del pétalo, la longitud del sépalo, el ancho del sépalo nos ayuda a saber si se trata de una setosa, versicolor, virginica mediante el uso de SVC, o Support Vector Classifier para la predicción.
## Para mostrar el tablero

pip3 install streamlit

streamlit run dashboard.py

Copiar y pegar la dirección que se muestra en su navegador web para cargar.

![image]('..//DATA//dashboard.png')

La aplicación esta dividida en 4 páginas:

1.Análisis de los datos del Iris Dataset.

2.Gráficas de los datos.

3.Conclusiones.

4.Clasificación del tipo de flor.


![image]('..//DATA//Análisis.png')


## Análisis de datos
En la parte de Análisis de datos, se han creado dos pestañas para poder seleccionar datos globales, es decir, información general del Dataset y datos especificos, donde podemos seleccionar por filas, columnas o  clases a la hora de ver los datos.


![image]('..//DATA//Análisis1.png')

## Gráficos de los datos
En cuanto a las gráficas hay unas pestañas a la izquierda donde elegir el tipo de gráfico con el que se quieren visualizar los datos.

![image]('..//DATA//Gráfico1.png')

En alguno de los graficos se pueden seleccionar  la clases o los atributos del dataset especificos que quieren verse.

![image]('..//DATA//Gráfico2.png')


![image]('..//DATA//Gráfico3.png')
## Conclusiones
En la parte de conclusion tenemos la información sobre los datos y las conclusiones a las que se ha llegado analizando los datos.

![image]('..//DATA//Conclusiones.png')

## Predicción 
La predicción se realiza con el algoritmo Support Vector Classifier, al lado derecho hay una barra donde se pueden seleccionar las medidas del ancho y largo de la flor para predecir de que tipo de flor iris se trata.


![image]('..//DATA//Clasificación.png')


## Documentación
https://docs.streamlit.io/en/estable/
