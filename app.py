import streamlit  as st
import pandas as pd
import plotly_express  as pl

vehicles = pd.read_csv('vehicles_us.csv')

#**Verificamos y corregimos valores vacios**
vehicles['model_year'].fillna('1900', inplace=True)
vehicles['cylinders'].fillna('0', inplace=True)
vehicles['odometer'].fillna('0', inplace=True)
vehicles['paint_color'].fillna('unknown', inplace=True)
vehicles['is_4wd'].fillna('0', inplace=True) 

#Corregimos los tipos de columnas
vehicles['model_year'] = vehicles['model_year'].astype(int)
vehicles['cylinders'] = vehicles['cylinders'].astype(int)
vehicles['odometer'] = vehicles['odometer'].astype(int)
vehicles['is_4wd'] = vehicles['is_4wd'].astype(int)
vehicles['date_posted'] = vehicles['date_posted'].astype('datetime64[ns]')

st.header('Este es el encabezado')

hist_button = st.button('Construir histograma') 
disp_button = st.button('Construir grafico de dispersion')

if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = pl.histogram(vehicles, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

if disp_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = pl.scatter(vehicles, x="odometer", y="price")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)