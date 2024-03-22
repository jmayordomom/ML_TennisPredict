import streamlit as st
import time
import numpy as np
import pandas as pd

st.set_page_config(page_title="MatchStats", page_icon="📈")

st.markdown("# MatchStats")
st.sidebar.header("MatchStats")
st.write("Esta página muestra información relativa a los partidos jugados en el ranking ATP en el año 2023")

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)

for i in range(1, 101):
    
    status_text.text("%i%% Complete" % i)
    progress_bar.progress(i)
    time.sleep(0.01)

progress_bar.empty()

data = pd.read_csv("../data/raw/atp_matches_2023.csv", sep=";")
# data = pd.read_csv("../data/processed/tennisResults.csv")

torneos = sorted(data["tourney_name"].unique())
st.sidebar.subheader('Filtro de datos')

# Por Torneo
st.sidebar.text('Por Torneo')
torneo = st.sidebar.selectbox('Seleccione un Torneo',torneos)
data = data.query("tourney_name == @torneo")

# Por ronda
st.sidebar.text('Por ronda')

ronda = data["round"].unique()
round = st.sidebar.selectbox('Seleccione una ronda',ronda)
data =  data.query("round == @round")
# st.write(data)
st.markdown('---')
#Datos torneo
st.write('## Información del torneo')

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.write('### Nombre')
    name = data["tourney_name"].iloc[0]
    st.write(name)

with col2:
    st.write('### Categoría')
    if data["tourney_level"].iloc[0] == "G":
        level = "Grand Slam"
    elif data["tourney_level"].iloc[0] == "D":
        level = "Copa Davis"
    elif data["tourney_level"].iloc[0] == "A":
        level = "ATP 250/500"
    elif data["tourney_level"].iloc[0] == "M":
        level = "Masters 1000"
    else:
        level = "Other"
    st.write(level)

with col3:
    st.write('### Superficie')
    surface = data["surface"].iloc[0]
    st.write(surface)
    
with col4:
    st.write('### Nº jugadores')
    plyers = str(data["draw_size"].iloc[0])
    st.write(plyers)
    
st.markdown('---')

# Datos partido
st.write('## Estadísticas del partido')

col1, col2, col3 = st.columns(3)
with col1:
    st.write('### Duración (min.)')
    minu = str(data["minutes"].iloc[0]).split(".")[0]
    st.write(minu)

with col2:
    st.write('### Resultado')
    res = str(data["score"].iloc[0])
    st.write(res)
    
with col3:
    st.write('### Ronda')
    if round == "F":
        level = "Final"
    elif round == "SF":
        level = "Semi Final"
    elif round == "QF":
        level = "Cuartos de Final"
    elif round == "R16":
        level = "Octavos de Final"
    elif round == "R32":
        level = "Tercera Ronda"
    elif round == "R64":
        level = "Segunda Ronda"
    elif round == "R128":
        level = "Primera Ronda"
    elif round == "RR":
        level = "Round Robin"
    else:
        level = "Other"
    st.write(level)

st.markdown('---')

# Datos ganador
st.write('## Estadísticas del ganador')

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.write('### Ganador')
    winner = data["winner_name"].iloc[0] + " - " + data["winner_ioc"].iloc[0]
    st.write(winner)

with col2:
    st.write('### Edad')
    age = str(data["winner_age"].iloc[0]).split(".")[0]
    st.write(age)
    
with col3:
    st.write('### Mano dominante')
    if data["winner_hand"].iloc[0] == "R":
        hand = "Diestro"
    elif data["winner_hand"].iloc[0] == "L":
        hand = "Zurdo"
    else:
        hand = "Ambidiestro"
    st.write(hand)
# column 4 - Count of cities
with col4:
    st.write('### Nº Aces Ganador')
    ace = str(data["w_ace"].iloc[0]).split(".")[0]
    st.write(ace)
with col5:
    st.write('### Nº DF Ganador')
    df = str(data["w_df"].iloc[0]).split(".")[0]
    st.write(df)


st.sidebar.markdown('---')

st.sidebar.markdown('App creada por Jaime Mayordomo')