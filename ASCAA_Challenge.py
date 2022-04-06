import pandas as pd
import streamlit as st

st.image('./ASCAA_logo.jpg')

st.title ("Challenge Hivernal ASCAA")
st.subheader('Résultats définitifs')

df=pd.read_csv("Rapport_Challenge_ASCAA.csv",sep=";", encoding='Latin_1', index_col = 0)
print(df.info())
df.head(30)

df.rename(columns={"Boosts reçus":"Boosts", "Nombre de quizz bien répondus":"Quizz", "Missions validées":"Missions",
                   "Distance totale":"Distance", "Nombre de pas":"Pas",
                  }, inplace=True
         )


df = df.sort_values(by = ['Points'], key= abs, ascending = False)
df = df.reindex()

st.markdown('Points')
st.bar_chart(df['Points'], use_container_width=True)

df = df.sort_values(by = ['Distance'], key= abs, ascending = False)
df = df.reindex()

st.markdown('Distance totale')
st.bar_chart(df['Distance'])


st.markdown('Nombre de pas')
st.bar_chart(df['Pas'])


st.markdown('Nombre de missions validées')
st.bar_chart(df['Missions'])


st.markdown('Nombre de Boosts attribués')
st.bar_chart(df['Boosts'])


st.markdown('Nombre de Quizz Ok')
st.bar_chart(df['Quizz'])

st.markdown('Regroupements multicritères')
st.image('./Dendro_0228.jpg')

df=df.drop(['Nombre de Commentaires', 'Nombre de likes émis', 'Boosts envoyés', 'Nombre de personnes',
            'Nombre de quizz répondus',
           ], axis=1)

st.markdown('Données chiffrées')
st.write(df)

st.markdown('Statistiques')
st.write(df.describe().transpose().round())





