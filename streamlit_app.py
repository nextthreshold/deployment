import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.header('IRIS Flower Dashboard')


st.divider()

with st.sidebar:
    st.header('Desription')
    st.text_area('','The Iris flower data set or Fisher Iris data set is a multivariate data set used and made famous by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.')
    st.image('flower.jpg')
df=pd.read_csv("iris.csv")
data=pd.DataFrame(df)
#st.table(data.head(6))
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("pie chart of species")
    fig1, draw1 = plt.subplots()
    draw1.pie(x=df['variety'].value_counts().values, labels=df['variety'].value_counts().index, autopct="%0.2f%%")
    st.pyplot(fig=fig1)

with col2:
    st.subheader('Flower Species')
    fig2, draw2 = plt.subplots()
    draw2.bar(x=df['variety'].value_counts().index, height=df['variety'].value_counts().values)
    st.pyplot(fig=fig2)   

st.divider()

col3,col4,col5 =st.columns(3)
with col3:
    st.subheader("Sepal length VS Sepal width")
    fig3, ax3 = plt.subplots()
    ax3.scatter(x=df['sepal.length'],y=df['sepal.width'])
    st.pyplot(fig=fig3)

with col4:
    figure = px.scatter_3d(x=df['sepal.length'],y=df['sepal.width'],z=df['petal.length'])
with col5:
    st.subheader("Petal Length vs Petal Width")
    fig5, ax5 = plt.subplots()
    ax5.scatter(x=df['petal.length'],y=df['petal.width'])
    st.pyplot(fig=fig5)


#TREplt.pyplot
