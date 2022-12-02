# Para ejecutar usaremos streamlit run <nombre del script> :streamlit run dashboard.py

import pandas as pd
import streamlit as st

st.write("Práctica DashBoard - Rosana Longares & Javier López")
st.write("Esta es la primera versión para el Iris Dataset...")

df = pd.read_csv("..\\DATA\\2_IrisSpecies.csv")  

st.title("Iris AGAIN!!")
st.write(df)

st.write("Podemos plotear un gráfico de barras")
st.bar_chart(df.SepalLengthCm)