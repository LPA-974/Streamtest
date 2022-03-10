#!/usr/bin/env python
# coding: utf-8

# In[5]:

import pandas as pd
import streamlit as st
#import matplotlib.pyplot as plt

#from sklearn import preprocessing
#from sklearn.preprocessing import StandardScaler
#import plotly.express as px


# In[6]:


st.title ("Test Streamlite sur Data ASCAA")
st.markdown('premier essai sur Streamlite')

df=pd.read_csv("Rapport_Hebdo_2802.csv",sep=";", encoding='Latin_1', index_col = 0)
print(df.info())
df.head(30)

st.header('Chargement des données')


st.dataframe(df.head(30))

st.markdown('Calcul des statistiques')
st.dataframe(df.describe().transpose().round())


st.markdown('Calcul de la médiane')
st.dataframe(df.median().round())


df=df.drop(['Boosts reçus', 'Nombre de Posts', 'Nombre de Commentaires', 'Nombre de likes émis', 'Points'], axis=1)


st.dataframe(df.head(30))

st.button('Click me')

st.checkbox('I agree')

st.radio('Pick one', ['cats', 'dogs'])

st.multiselect('Buy', ['milk', 'apples', 'potatoes'])

st.slider('Pick a number', 0, 100)
st.select_slider('Pick a size', ['S', 'M', 'L'])
st.text_input('First name')
st.number_input('Pick a number', 0, 10)
st.text_area('Text to translate')
st.date_input('Your birthday')
st.time_input('Meeting time')
st.file_uploader('Upload a CSV')
st.camera_input('Take a picture')
st.download_button('Download file', data)

st.color_picker('Pick a color')