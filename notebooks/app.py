# Importamos las librerías necesarias para este proyecto
import streamlit as st
import pandas as pd
import plotly_express as px

# Extraemos la información de nuestro dataset
car_data = pd.read_csv('vehicles_us.csv')

# Creamos un encabezado
st.title("Análisis de Vehículos Usados")

# Casilla para mostrar histograma
if st.checkbox('Mostrar histograma del precio'):
    st.write("Distribución de precios de los vehículos")
    fig_hist = px.histogram(car_data, x='price', nbins=50,
                            title='Distribución de precios')
    st.plotly_chart(fig_hist)

# Casilla para mostrar gráfico de dispersión
if st.checkbox('Mostrar gráfico de dispersión: precio vs odómetro'):
    st.write("Relación entre precio y kilometraje (odómetro)")
    fig_scatter = px.scatter(car_data, x='odometer', y='price',
                             title='Precio vs Odómetro',
                             labels={
                                 'odometer': 'Kilometraje (millas)', 'price': 'Precio (USD)'},
                             opacity=0.6)
    st.plotly_chart(fig_scatter)
