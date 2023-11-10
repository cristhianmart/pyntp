import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('BBDD - suicidios.csv')

df.columns

columna = df.loc[:,'nombre_comuna'].unique() 
columna

option = st.selectbox(
    'Ingrese el genero',
    columna)

st.write('You selected:', option)

df =df[df['nombre_comuna'] == option]

df
