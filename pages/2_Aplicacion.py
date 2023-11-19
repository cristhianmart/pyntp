# Importar Streamlit para construir la aplicación web 
import streamlit as st  

# Importar el modelo YOLO de Ultralytics para la detección de objetos
from ultralytics import YOLO

# Importar PIL para el procesamiento de imágenes
from PIL import Image

# Cargar el modelo YOLO preentrenado para detectar monedas
modelo = YOLO('coins.pt')

# Establecer el título de la aplicación
st.title("Identificar monedas") 

# Crear una lista vacía para almacenar las clases detectadas
clases = []

# Permitir al usuario cargar un archivo de imagen 
archivo_cargado = st.file_uploader("Elige una imagen", type=["png","jpg"])

# Si se carga un archivo
if archivo_cargado is not None:

  # Abrir la imagen
  imagen_cargada = Image.open(archivo_cargado)
  
  # Mostrar la imagen cargada
  #st.image(imagen_cargada, caption='Imagen subida', use_column_width=True, width=500)

  # Usar el modelo para detectar monedas en la imagen
  resultados = modelo(imagen_cargada)

  # Imprimir los resultados
  for r in resultados:
    print(r)

  # Graficar las detecciones sobre la imagen
  matriz_imagen = r.plot()

  # Convertir la matriz a una imagen PIL
  imagen = Image.fromarray(matriz_imagen[..., ::-1])

  # Mostrar los resultados de la detección
  st.image(imagen, caption='Resultado de la detección')

  # Analizar las cajas de detección
  for deteccion in r.boxes:

    # Extraer la clase y la confianza
    clases.append({"clase":deteccion.cls.data.item(),"confianza":deteccion.conf.data.item()})

  # Inicializar el conteo de dinero
  dinero_total = 0

  # Revisar cada objeto detectado 
  for moneda in clases:

    # Imprimir los detalles
    print(moneda)

    # Verificar la clase y la confianza para contar el dinero
    if moneda['clase'] == 0.0:
      if moneda['confianza'] > 0.7:
        dinero_total += 1000
    elif moneda['clase'] == 1.0:
      if moneda['confianza'] > 0.7:
        dinero_total += 200
    elif moneda['clase'] == 2.0:
      if moneda['confianza'] > 0.7:
        dinero_total += 500
  
  # Mostrar el dinero total
  st.header("Total dinero detectado")
  st.header(dinero_total)