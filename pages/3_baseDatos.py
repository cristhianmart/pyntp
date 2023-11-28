import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import folium
import streamlit as st

df = pd.read_csv('BBDD - suicidios.csv')

df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y', dayfirst=True)

df['año'] = df['fecha'].dt.year

#cantidad de intentos suicidas por año
intentos_por_año = df.groupby('año')['Intentos suicidas'].sum()
plt.figure(figsize=(8, 6))
plt.plot(intentos_por_año.index, intentos_por_año.values, marker='o')
plt.xlabel('Año')
plt.ylabel('Cantidad de intentos suicidas')
plt.title('Cantidad de intentos suicidas por año')

for i, txt in enumerate(intentos_por_año.values):
    plt.text(intentos_por_año.index[i], txt, str(txt), ha='right', va='bottom')
    
st.pyplot(plt)  

#cantidad de intentos suicidas por estrato en un gráfico de línea
intentos_por_estrato = df.groupby('estrato')['Intentos suicidas'].sum()
plt.figure(figsize=(8, 6))
intentos_por_estrato.plot(kind='bar', color='skyblue')
plt.xlabel('Estrato')
plt.ylabel('Cantidad de intentos suicidas')
plt.title('Cantidad de intentos suicidas por estrato')

for i, valor in enumerate(intentos_por_estrato.values):
    plt.text(i, valor, str(valor), ha='center', va='bottom')

plt.xticks(range(len(intentos_por_estrato.index)), intentos_por_estrato.index)
st.pyplot(plt)

#nombre del barrio con más intentos suicidas
barrio_mas_intentos = df.groupby('nombre_barrio')['Intentos suicidas'].sum().idxmax()

#intentos suicidas por barrio
intentos_por_barrio = df.groupby('nombre_barrio')['Intentos suicidas'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
intentos_por_barrio.plot(kind='bar', color='skyblue')
plt.xlabel('Barrio')
plt.ylabel('Cantidad de intentos suicidas')
plt.title('Intentos suicidas por barrio')
plt.xticks(rotation=45)  
plt.tight_layout()
st.title('Barrio con más intentos suicidas y cantidad por barrio')
st.write(f"El barrio con más intentos suicidas es: {barrio_mas_intentos}")
st.pyplot(plt)

#porcentaje de intentos suicidas por método
porcentaje_por_metodo = df['Metodo'].value_counts(normalize=True) * 100
plt.figure(figsize=(8, 6))
porcentaje_por_metodo.plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'lightcoral', 'lightskyblue'])
plt.title('Porcentaje de intentos suicidas por método')
plt.ylabel('')
plt.tight_layout()
st.title('Porcentaje de intentos suicidas por método')
st.pyplot(plt)
