import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

# Separar la columna 'model' en 'manufacturer' y 'model'
car_data[
    ['manufacturer', 'model']
] = car_data['model'].str.split(' ', n=1, expand=True)

cols = list(car_data.columns)  # lista actual de columnas

# Quitar 'manufacturer' y 'model' para reinsertarlos en el orden deseado
cols.remove('manufacturer')
cols.remove('model')

idx = cols.index('model_year')          # índice de 'model_year'
cols.insert(idx + 1, 'manufacturer')    # reposicionar 'manufacturer'
cols.insert(idx + 2, 'model')           # reposicionar 'model'
car_data = car_data[cols]               # reordenar el DataFrame

st.markdown('# Car Sales')  # title

st.markdown('## Data viewer')  # header
st.dataframe(car_data)

st.markdown('## Car Sales Filtered **')  # header
# filtro para manufacturers
manufacturers = ['All'] + list(car_data['manufacturer'].unique())
selected_manufacturer = st.selectbox(
    'Select a manufacturer to filter:', options=manufacturers)


# aplicar filtros
if selected_manufacturer != 'All':
    filtered_by_manufacturer = car_data[car_data['manufacturer']
                                        == selected_manufacturer]
else:
    filtered_by_manufacturer = car_data.copy()

models = ['All'] + sorted(filtered_by_manufacturer['model'].unique())
selected_model = st.selectbox("Select Model", options=models)

if selected_model != 'All':
    filtered_by_model = filtered_by_manufacturer[filtered_by_manufacturer['model']
                                                 == selected_model]
else:
    filtered_by_model = filtered_by_manufacturer.copy()

years = ['All'] + sorted(filtered_by_model['model_year'].unique())
selected_year = st.selectbox("Select Model Year", options=years)

if selected_year != 'All':
    filtered_data = filtered_by_model[filtered_by_model['model_year']
                                      == selected_year]
else:
    filtered_data = filtered_by_model

st.write(f"Showing data filtered:")
st.dataframe(filtered_data)


hist_button = st.checkbox('Build Histogram')  # primer botón
# opciones Histograma: 1. Odometro, 2. Promedio por marca

# hist_odom_button = st.checkbox('Distribution of Odometer Values')


if hist_button:  # al hacer clic en el botón
    st.text("")
    if st.checkbox('🚗 I, Distribution of Odometer Values'):
        st.subheader(
            'Histogram: Distribution of Odometer Values')

        # crear un histograma
        fig = px.histogram(car_data, x="odometer")

        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig, use_container_width=True)

    if st.checkbox('🚗 II, Histogram by Manufacturer'):
        st.subheader('Histogram: Average price by Manufacturer')
        fig = px.histogram(car_data, x="manufacturer",
                           y="price", histfunc="avg", color="manufacturer")
        st.plotly_chart(fig, use_container_width=True)

    st.text("")
    st.text("")

scatter_button = st.checkbox(
    'Build Scatter Plot')  # segundo botón

if scatter_button:
    st.text("")

    if st.checkbox('🚗 I, Odometer vs.  Vehicle Price'):
        st.subheader(
            'Scatter Plot: Odometer vs. Price')

        # crear un gráfico de dispersión
        fig = px.scatter(car_data, x="odometer", y="price")

        # mostrar gráfico de dispersión
        st.plotly_chart(fig, use_container_width=True)

    if st.checkbox('🚗 II, Vehicle Price by Model Year and Manufacturer'):
        st.subheader(
            'Scatter Plot: Model year vs. Price')

        # crear un gráfico de dispersión
        fig = px.scatter(car_data, x="model_year",
                         y="price", color="manufacturer")

        # mostrar gráfico de dispersión
        st.plotly_chart(fig, use_container_width=True)
