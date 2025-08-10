import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv(r'C:\Users\GATEWAY\Documents\Sprint7\vehicles_us.csv')
hist_button = st.checkbox('Construir histograma')  # primer botón
scatter_button = st.checkbox(
    'Construir grafico de dispersión')  # segundo botón


if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    st.write(
        'Creación de un grafico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)
