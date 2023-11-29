import pandas as pd
import plotly.express as px
import streamlit as st


df = pd.read_csv('BBDD - suicidios.csv')


df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y', dayfirst=True)
df['año'] = df['fecha'].dt.year

# Cálculo de la cantidad total de intentos suicidas por año
intentos_por_año = df.groupby('año')['Intentos suicidas'].sum().reset_index()
total_intentos_año = intentos_por_año['Intentos suicidas'].sum()

#Cantidad de intentos suicidas por año
st.title('Cantidad de intentos suicidas por año')
fig_line = px.line(intentos_por_año, x='año', y='Intentos suicidas', 
                   labels={'año': 'Año', 'Intentos suicidas': 'Cantidad de intentos suicidas'},
                   title=f'Cantidad de intentos suicidas por año - Total: {total_intentos_año}')

fig_line.update_traces(mode='markers+lines', text=intentos_por_año['Intentos suicidas'], textposition='top center')
st.plotly_chart(fig_line)

#Cantidad de intentos suicidas por estrato
st.title('Cantidad de intentos suicidas por estrato')
intentos_por_estrato = df.groupby('estrato')['Intentos suicidas'].sum().reset_index()
total_intentos_estrato = intentos_por_estrato['Intentos suicidas'].sum()

fig_bar = px.bar(intentos_por_estrato, x='estrato', y='Intentos suicidas', 
                 labels={'estrato': 'Estrato', 'Intentos suicidas': 'Cantidad de intentos suicidas'},
                 title='Cantidad de intentos suicidas por estrato')
fig_bar.update_traces(text=intentos_por_estrato['Intentos suicidas'], textposition='outside')
fig_bar.update_layout(yaxis=dict(range=[0, total_intentos_estrato + 100]))
st.plotly_chart(fig_bar)

#Barrios con más intentos suicidas
st.title('Barrios con más intentos suicidas')
df_filtrado = df[df['nombre_barrio'] != 'Sin información']
intentos_por_barrio = df_filtrado.groupby('nombre_barrio')['Intentos suicidas'].sum().sort_values(ascending=False)
top_20_barrios = intentos_por_barrio.head(20)
barrios_df = pd.DataFrame({'Barrio': intentos_por_barrio.index, 'Intentos Suicidas': intentos_por_barrio.values})
fig_barrios = px.bar(barrios_df[:20], x='Barrio', y='Intentos Suicidas', 
                     labels={'Barrio': 'Barrio', 'Intentos Suicidas': 'Cantidad de intentos suicidas'},
                     title='Barrios con más intentos suicidas')
fig_barrios.update_layout(height=600, yaxis=dict(range=[0, max(barrios_df['Intentos Suicidas']) + 50]))
fig_barrios.update_traces(text=barrios_df[:20]['Intentos Suicidas'], textposition='outside')
barrio_seleccionado = st.selectbox('Selecciona un barrio', barrios_df['Barrio'])
st.plotly_chart(fig_barrios)
st.write(f"El barrio '{barrio_seleccionado}' tiene {intentos_por_barrio[barrio_seleccionado]} intentos suicidas.")

#Porcentaje de intentos suicidas por método
st.title('Porcentaje de intentos suicidas por método')
porcentaje_por_metodo = df['Metodo'].value_counts(normalize=True) * 100
top_20_metodos = porcentaje_por_metodo.head(20)
fig_pie = px.pie(names=top_20_metodos.index, values=top_20_metodos.values,
                 title='Los 20 métodos más utilizados en intentos de suicidio')
st.plotly_chart(fig_pie)
