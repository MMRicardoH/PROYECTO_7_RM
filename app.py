import streamlit as st
import pandas as pd
import plotly.express as px

dt_cars = pd.read_csv('vehicles_us.csv')

st.header('Proyecto 7')  # Encabezado
hist_button = st.button('Construcción histrograma')  # Creación del botón

# Funcionalidad del botón - Histograma
if hist_button:
    # Mensaje a mostrar
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Creación del histograma
    fig = px.histogram(dt_cars, x="odometer")

    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig, width='stretch')


disp_button = st.button(
    'Construcción gráfica dispersión')  # Creación del botón

# Funcionalidad del botón - Gráfica dispersión
if disp_button:
    # Mensaje a mostrar
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Creación del gráfico de dispersión
    fig = px.scatter(dt_cars, x="odometer", y="price")

    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig, width='stretch')
