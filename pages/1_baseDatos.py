import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('BBDD - suicidios.csv', parse_dates=['fecha'], dayfirst=True)

#Selector por año
año_seleccionado = st.selectbox("Selecciona un año:", df['fecha'].dt.year.unique())

# filtro por año que se seleccione
#datos_filtrados = df[df['fecha'].dt.year == año_seleccionado]

#Selector por sexo 
sexo = st.selectbox("Genero:", df['sexo_'].unique())

#Selector por localidad
localidad = st.selectbox("Seleccione localidad", df['localidad_'].unique())

#Selector por Barrio
barrio = st.selectbox("Seleccione Barrio", df['nombre_barrio'].unique())

#Selector por metodo 
metodo = st.selectbox("Metodos recurridos", df['Metodo'].unique())

#Selector por estrato
estrato = st.selectbox("Estrato", df['estrato'].unique())

