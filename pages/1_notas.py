import streamlit as st  # Importar la biblioteca Streamlit para crear aplicaciones web interactivas
from googleapiclient.discovery import build  # Importar la biblioteca Google API Python Client Library para interactuar con Google Sheets
from google.oauth2 import service_account  # Importar el módulo service_account para la autenticación
from googleapiclient.errors import HttpError  # Importar la clase HttpError para manejar errores
import pandas as pd


# Crear un encabezado para la aplicación web
st.header('API Google Sheet')

# Definir los alcances para acceder a Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Especificar la ruta al archivo JSON que contiene las credenciales de la cuenta de servicio
SERVICE_ACCOUNT_FILE = 'keys.json'

# Inicializar una variable vacía para almacenar el objeto de servicio de Google Sheets
sheet = None

# Autenticarse utilizando las credenciales de la cuenta de servicio
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Construir el objeto de servicio de Google Sheets
service = build('sheets', 'v4', credentials=creds)

# Acceder a la API de Google Sheets
sheet = service.spreadsheets() 

# Crear un campo de entrada de texto para que el usuario ingrese el ID del documento de Google Sheet
SAMPLE_SPREADSHEET_ID = st.text_input('ID del documento de Google Sheet', '')

# Definir el rango de celdas que se leerán del documento de Google Sheet
SAMPLE_RANGE_NAME = 'Hoja 1!A4:O28'

# Crear un botón para desencadenar el proceso de recuperación de datos
if st.button('Leer rango'):
    # Leer el rango de celdas especificado del documento de Google Sheet
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()

    # Extraer los datos de la respuesta
    datos_hoja = result.get('values', [])

    columnas = ['Nombres','Apellidos','M1C','M1D','M1P','M1T','M2C','M2D','M2P','M2T','M3C','M3D','M3P','M3T','NF']
   
    # Creamos el dataframe
    df = pd.DataFrame(datos_hoja, columns=columnas)


    # Mostrar los datos recuperados como una tabla
    m1t = df.loc[:,['Nombres', 'M1T']] 
    m1t['M1T'] = df['M1T'].str.replace(',', '.').astype(float)

    st.header("Momento 1")
    st.bar_chart(m1t.set_index('Nombres'))


    m2t = df.loc[:,['Nombres', 'M2T']] 
    m2t['M2T'] = df['M2T'].str.replace(',', '.').astype(float)

    st.header("Momento 2")
    st.bar_chart(m2t.set_index('Nombres'))


    m3t = df.loc[:,['Nombres', 'M3T']] 
    m3t['M3T'] = df['M3T'].str.replace(',', '.').astype(float)

    st.header("Momento 3")
    st.bar_chart(m3t.set_index('Nombres'))


    nt = df.loc[:,['Nombres', 'NF']] 
    nt['NF'] = df['NF'].str.replace(',', '.').astype(float)

    st.header("Nota Final")
    st.bar_chart(nt.set_index('Nombres'))  