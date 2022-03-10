import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


st.title ("Challenge hivernal ASCAA")
st.subheader('Résultats intermédaires au 28 Février 2022')

df=pd.read_csv("Rapport_Hebdo_2802.csv",sep=";", encoding='Latin_1', index_col = 0)
print(df.info())
df.head(30)

df.rename(columns={"Boosts envoyés":"Boosts", "Nombre de quizz bien répondu":"Quizz", "Missions validés":"Missions",
                   "Distance totale":"Distance",
                  }, inplace=True
         )

df=df.sort_values(by=['Points'])
st.markdown('Points')
st.bar_chart(df['Points'], use_container_width=True)

df=df.sort_values(by=['Distance'])
st.markdown('Distance totale')
st.bar_chart(df['Distance'])

df=df.sort_values(by=['Missions'])
st.markdown('Nombre de missions validées')
st.bar_chart(df['Missions'])

df=df.sort_values(by=['Boosts'])
st.markdown('Nombre de Boosts')
st.bar_chart(df['Boosts'])

df=df.sort_values(by=['Quizz'])
st.markdown('Nombre de Quizz bien répondu')
st.bar_chart(df['Quizz'])


st.write(df)

st.markdown('Calcul des statistiques')
st.write(df.describe().transpose().round())


st.markdown('Calcul de la médiane')
st.write(df.median().round())



df=df.drop(['Boosts reçus', 'Nombre de Posts', 'Nombre de Commentaires', 'Nombre de likes émis', 'Points', 'Nombre de personnes'], axis=1)