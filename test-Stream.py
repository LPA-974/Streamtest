#!/usr/bin/env python
# coding: utf-8

# In[5]:

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
#import plotly.express as px


# In[6]:


st.title ("Test Streamlite sur Data ASCAA")
st.markdown('premier essai sur Streamlite')

df=pd.read_csv("Rapport_Hebdo_2802.csv",sep=";", encoding='Latin_1', index_col = 0)
print(df.info())
df.head(30)

st.header('Chargement des données')


st.dataframe(df.head(30))

st.dataframe(df.describe().transpose().round())

st.dataframe(df.median().round())

st.dataframe(df=df.drop(['Boosts reçus', 'Nombre de Posts', 'Nombre de Commentaires', 'Nombre de likes émis', 'Points'], axis=1))

scaler=preprocessing.StandardScaler().fit(df)
df_scaled=scaler.transform(df)
plt.figure(figsize=(20, 10))

# Génération de la matrice des liens
Z = linkage(df_scaled, method = 'ward', metric = 'euclidean')

# Affichage du dendrogramme
plt.title("Challenge ASCAA Hivernal - Regroupement des équipes")
dendrogram(Z, labels = df.index, leaf_rotation = 75, color_threshold = 7)
plt.show()

# In[ ]:




