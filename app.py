#Import the necessary libraries for this project
import streamlit as st
import pandas as pd
import plotly_express as px

#Extract the information from our dataset
car_data = pd.read_csv('vehicles_us.csv')

#Create a header
st.title("Used Vehicles Analysis")

#Checkbox to display histogram
if st.checkbox('Show price histogram'):
    st.write("Vehicle price distribution")
    fig_hist = px.histogram(car_data, x='price', nbins=50,
                            title='Price distribution')
    st.plotly_chart(fig_hist)

#Checkbox to display scatter plot
if st.checkbox('Show scatter plot: price vs odometer'):
    st.write("Relationship between price and mileage (odometer)")
    fig_scatter = px.scatter(car_data, x='odometer', y='price',
                             title='Price vs Odometer',
                             labels={
                                 'odometer': 'Mileage (miles)', 'price': 'Price (USD)'},
                             opacity=0.6)
    st.plotly_chart(fig_scatter)
