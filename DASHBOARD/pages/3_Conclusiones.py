# Para ejecutar usaremos streamlit run <nombre del script> :streamlit run dashboard.py

import streamlit as st
from PIL import Image
st.write("Práctica DashBoard - Rosana Longares & Javier López")

st.title("3.CONCLUSIONES")


st.markdown(
    """
    # PRIMERAS IMPRESIONES

    **Se trata de un dataset con información sobre distintas especies de la planta Iris, en el que se dan la longitud y la anchura de los pétalos y sépalos, y la especie que es con dichas características.**
    Sacamos primeras conclusiones:
    * Tiene un tamaño de **150 filas** y **6 columnas**
    * Las columnas de **Sépalos y Pétalos** contienen datos **Float**
    * La columna **Species** es una **cadena**
    * **No hay valores Nulos**
    * Tres posibles Species:
        * **Iris-setosa**
        * **Iris-versicolor**
        * **Iris-virginica**  
    * El ID no nos sirve de nada
    """
)

image = Image.open('..//DATA//iris3.png')
st.image(image, caption='FLOR IRIS')
st.markdown(
    """
    # CONCLUSIONES

    * La especie **SETOSA** está distrbuída de una forma más homogénia y diferenciada
    * Las especies **VERSICOLOR y VIRGINICA** se encuentran más mezcladas
    * A su vez los **PÉTALOS** de las tres especies están distribuídos de forma más homogénea que los **SÉPALOS**
    * La especie con los **PÉTALOS** de **mayor longitud** es **VIRGINICA**
    * La especie con los **PÉTALOS** de **MENOR longitud** es **SETOSA**, de hecho no llega nunga a los de **VERSICOLOR y VIRGINICA**
    * La especie con los **PÉTALOS** de **mayor anchura** es **VIRGINICA**
    * La especie con los **PÉTALOS** de **MENOR anchura** es **SETOSA**, de hecho no llega nunga a los de **VERSICOLOR y VIRGINICA**
    * La especie con los **SÉPALOS** de **mayor longitud** es **VIRGINICA**
    * La especie con los **SÉPALOS** de **MENOR longitud** es **SETOSA**, pero coincide en muchas ocasiones con **VERSICOLOR** y algo menos con **VIRGINICA**
    * La especie con los **SÉPALOS** de **mayor anchura** es **SETOSA**
    * La especie con los **SÉPALOS** de **MENOR anchura** es **VERSICOLOR**, pero coincide en muchas ocasiones con **VIRGINICA** y algo menos con **SETOSA**
    """
)