Análisis de Datos de Suicidios
Descripción General
Este script en Python analiza datos de suicidios de un conjunto de datos utilizando diversas técnicas de visualización. El conjunto de datos se carga mediante la biblioteca Pandas, y el análisis se realiza con Matplotlib, Seaborn, Plotly Express, Folium y Streamlit.
Prerrequisitos
•	Asegúrate de tener instaladas las bibliotecas de Python necesarias. Puedes instalarlas con el siguiente comando:
Copy code
pip install pandas matplotlib seaborn plotly folium streamlit 
Uso
1.	Carga de Datos:
•	El script lee el conjunto de datos 'BBDD - suicidios.csv' en un DataFrame de Pandas.
2.	Preprocesamiento de Datos:
•	Convierte la columna 'fecha' al formato de fecha y hora con el formato especificado.
•	Extrae el año de la columna 'fecha' y crea una nueva columna 'año'.
3.	Visualización 1: Intentos a lo largo de los Años
•	Agrupa los datos por año y grafica el número total de intentos de suicidio por año.
•	Utiliza Matplotlib para el gráfico de línea.
•	Muestra el gráfico mediante Streamlit.
4.	Visualización 2: Intentos por Estrato Socioeconómico
•	Agrupa los datos por estrato socioeconómico y grafica el número total de intentos de suicidio para cada estrato.
•	Utiliza Matplotlib para el gráfico de barras.
•	Muestra el gráfico mediante Streamlit.
5.	Análisis: Barrio más Afectado
•	Identifica el barrio con el mayor número de intentos de suicidio.
•	Agrupa los datos por barrio y grafica el número total de intentos para cada barrio.
•	Muestra el barrio con más intentos y un gráfico de barras de intentos por barrio mediante Streamlit.
6.	Visualización 3: Porcentaje de Intentos por Método
•	Calcula la distribución porcentual de intentos de suicidio por método.
•	Utiliza Matplotlib para el gráfico circular.
•	Muestra el gráfico circular mediante Streamlit.
Cómo Ejecutar
1.	Asegúrate de que el conjunto de datos requerido ('BBDD - suicidios.csv') esté en el mismo directorio que el script.
2.	Ejecuta el script con el siguiente comando:

streamlit run app.py 

3.	Abre el enlace de Streamlit proporcionado en tu navegador para interactuar con las visualizaciones.
Nota
•	Este script proporciona información valiosa sobre datos de suicidios mediante diversas visualizaciones. Se pueden realizar ajustes y mejoras según requisitos específicos o fuentes de datos adicionales.




Identificación de Monedas con YOLO
Descripción General
Este script en Python utiliza la biblioteca Streamlit para construir una aplicación web que permite a los usuarios cargar una imagen y detectar monedas en ella utilizando el modelo YOLO (You Only Look Once) de Ultralytics. El código también emplea la biblioteca PIL (Python Imaging Library) para el procesamiento de imágenes.
Prerrequisitos
•	Asegúrate de tener instaladas las bibliotecas necesarias. Puedes instalarlas mediante el siguiente comando:
bashCopy code
pip install streamlit ultralytics torch 
Uso
1.	Cargar Modelo YOLO:
•	Importa la clase YOLO de Ultralytics para la detección de objetos.
•	Carga un modelo YOLO preentrenado ('coins.pt') para identificar monedas.
2.	Interfaz de Usuario con Streamlit:
•	Establece el título de la aplicación como "Identificar monedas".
•	Permite al usuario cargar una imagen desde su dispositivo.
3.	Detección de Monedas:
•	Utiliza el modelo YOLO para realizar la detección de monedas en la imagen cargada.
•	Muestra los resultados de la detección en una imagen junto con las cajas delimitadoras y las clases detectadas.
4.	Análisis de Resultados:
•	Extrae la clase y la confianza de cada detección.
•	Asigna valores monetarios a las clases y confianzas específicas.
•	Calcula el dinero total detectado en la imagen.
5.	Interfaz de Usuario (Streamlit):
•	Muestra el dinero total detectado como encabezado en la aplicación web.
Cómo Ejecutar
1.	Asegúrate de tener el modelo YOLO preentrenado ('coins.pt') en el mismo directorio que el script.
2.	Ejecuta el script con el siguiente comando:

streamlit run app.py 
3.	Abre el enlace de Streamlit proporcionado en tu navegador para interactuar con la aplicación web.
Nota
•	Este script puede servir como una herramienta práctica para la detección de monedas en imágenes, proporcionando información sobre las clases detectadas y el valor monetario total. Ajusta los umbrales de confianza y los valores monetarios según tus necesidades específicas.

