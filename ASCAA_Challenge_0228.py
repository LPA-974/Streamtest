import pandas as pd
import streamlit as st

st.title ("Challenge hivernal ASCAA")
st.subheader('Résultats au 28 Février 2022')

df=pd.read_csv("Rapport_Hebdo_2802.csv",sep=";", encoding='Latin_1', index_col = 0)
print(df.info())
df.head(30)

df.rename(columns={"Boosts envoyés":"Boosts", "Nombre de quizz bien répondu":"Quizz", "Missions validés":"Missions",
                   "Distance totale":"Distance",
                  }, inplace=True
         )


st.markdown('Points au 28 Février')
st.bar_chart(df['Points'])

st.markdown('Distance totale au 28 Février')
st.bar_chart(df['Distance'])

st.markdown('Nombre de missions validées')
st.bar_chart(df['Missions'])

st.markdown('Nombre de Boosts')
st.bar_chart(df['Boosts'])

st.markdown('Nombre de Quizz bien répondu')
st.bar_chart(df['Quizz'])


st.write(df)

st.markdown('Calcul des statistiques')
st.write(df.describe().transpose().round())


st.markdown('Calcul de la médiane')
st.write(df.median().round())



df=df.drop(['Boosts reçus', 'Nombre de Posts', 'Nombre de Commentaires', 'Nombre de likes émis', 'Points', 'Nombre de personnes'], axis=1)