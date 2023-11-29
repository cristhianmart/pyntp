import streamlit as st


def main():
    st.title('Proyecto integrador')


    st.markdown("""
    Este proyecto se hizo con el fin de aplicar todos los conocimientos aquiridos en el sudmodulo 
    de nuevas tecnologias con el docente Jhon Valencia. 

    Espero disfruten tanto de este, como nosotros lo hicimos. 

    """)

    # Cargar una imagen desde una ruta local
    imagen_path = 'imag/Screenshot_11.png'
    st.image(imagen_path, use_column_width=True)

    st.markdown("""
    ## Notas

    El proyecto consiste en una aplicación capaz de leer archivos de Google Sheet a través de un Id del documento.
    A continuación, filtra toda esa información y te regala los gráficos correspondientes a esta.
    """)

    st.markdown("""
    ## Aplicación

    Este script en Python utiliza la biblioteca Streamlit para construir una aplicación web que permite a los usuarios cargar una imagen y detectar monedas en ella utilizando el modelo YOLO (You Only Look Once) de Ultralytics. El código también emplea la biblioteca PIL (Python Imaging Library) para el procesamiento de imágenes.
    """)
    
    st.markdown("""
    ## Base de datos

    Este script en Python analiza datos de suicidios de un conjunto de datos utilizando diversas técnicas de visualización. El conjunto de datos se carga mediante la biblioteca Pandas, y el análisis se realiza con Matplotlib, Seaborn, Plotly Express, Folium y Streamlit.
    """)

if __name__ == '__main__':
    main()
