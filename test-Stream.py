#!/usr/bin/env python
# coding: utf-8

# In[5]:

import pandas as pd
import streamlit as st
import plotly.express as px


# In[6]:


st.title ("Test Streamlite sur Data ASCAA")
st.markdown('premier essai sur Streamlite')

df=pd.read_csv("Rapport_Hebdo_2802.csv",sep=";", encoding='Latin_1', index_col = 0)
print(df.info())
df.head(30)

st.header('Chargement des données')

st.dataframe(df.head())

# In[ ]:




