# Dashboard_Streamlit 

Esta es una aplicación web para proyectos de ciencia de datos donde hemos usado la biblioteca Streamlit para hacerla. Los datos utilizados son el famoso conjunto de datos incorporado de la flor de iris.

 En esta variación en los parámetros como la longitud del pétalo, el ancho del pétalo, la longitud del sépalo, el ancho del sépalo nos ayuda a saber si se trata de una setosa, versicolor, virginica mediante el uso de SVC, o Support Vector Classifier para la predicción.
## Para mostrar el tablero

pip3 install streamlit

streamlit run dashboard.py

Copiar y pegar la dirección que se muestra en su navegador web para cargar.
![dashboard](https://user-images.githubusercontent.com/98030137/212059026-442e1cd9-cc9a-4f9b-876b-6506fa62e1c1.png)



La aplicación esta dividida en 4 páginas:

1.Análisis de los datos del Iris Dataset.

2.Gráficas de los datos.

3.Conclusiones.

4.Clasificación del tipo de flor.





## Análisis de datos
En la parte de Análisis de datos, se han creado dos pestañas para poder seleccionar datos globales, es decir, información general del Dataset y datos especificos, donde podemos seleccionar por filas, columnas o  clases a la hora de ver los datos.

![Análisis](https://user-images.githubusercontent.com/98030137/212059052-15ec035e-fec4-469b-9af1-52f0b929447b.png)
![Análisis2](https://user-images.githubusercontent.com/98030137/212059350-ed0c0781-4c14-4b20-8c7d-bd2472f1224a.png)



## Gráficos de los datos
En cuanto a las gráficas hay unas pestañas a la izquierda donde elegir el tipo de gráfico con el que se quieren visualizar los datos.
![Gráfico1](https://user-images.githubusercontent.com/98030137/212059106-c5ccf1db-9df7-4ee2-a2ac-83fb77a20a0e.png)

![Grafico 1]('..//DATA//Gráfico1.png')

En alguno de los graficos se pueden seleccionar  la clases o los atributos del dataset especificos que quieren verse.

![Gráfico3](https://user-images.githubusercontent.com/98030137/212059146-e2e43a8e-8229-4e72-bb3b-e97e2a301a57.png)



## Conclusiones
En la parte de conclusion tenemos la información sobre los datos y las conclusiones a las que se ha llegado analizando los datos.
![Conclusiones](https://user-images.githubusercontent.com/98030137/212059184-aa090670-fafc-4911-8071-517060412ce8.png)



## Predicción 
La predicción se realiza con el algoritmo Support Vector Classifier, al lado derecho hay una barra donde se pueden seleccionar las medidas del ancho y largo de la flor para predecir de que tipo de flor iris se trata.


![Clasificación](https://user-images.githubusercontent.com/98030137/212059224-ce8fbfdb-4db2-48dd-b0fc-c2f64e7521a5.png)



## Documentación
https://docs.streamlit.io/en/estable/
