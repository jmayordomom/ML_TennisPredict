import joblib
import numpy as np
from sklearn.metrics import mean_absolute_percentage_error
import streamlit as st
import pandas as pd
from io import StringIO


from sklearn.calibration import LabelEncoder

from sklearn.model_selection import cross_validate, train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(page_title="Predictor", page_icon="📈")
st.sidebar.header("Predict Yourself")

st.markdown("# Mi Predicción")
st.write("Esta página permite realizar una prediccion con datos propios")
st.write("Hay que subir un fichero con formato **csv** y los siguientes campos:")

options = [('winner_id','Identificador del jugador ganador','Un número entero'),
           ('winner_hand','Mano predominante del ganador','R (diestro), L (zurdo) o U (ambidiestro)'), 
           ('winner_age','Edad del ganador','Un número entero'), 
           ('loser_id','Identificador del jugador perdedor','Un número entero'), 
           ('loser_hand','Mano predominante del perdedor', 'R (diestro), L (zurdo) o U (ambidiestro)'),
            ('loser_age','Edad del perdedor','Un número entero'), 
            ('best_of','Número de sets a los que se juega el partido','El número 3 o el número 5'), 
       ('round','Ronda del partido','F (Final), SF (Semifinal), QF (cuartos de final), R16 (Octavos), R32 (Tercera ronda), R64 (Segunda ronda), R128 (Primera ronda) o  RR (Round Robin)'), 
       ('w_ace','Número de aces del ganador','Un número entero'), 
       ('w_df','Número de dobles faltas del ganador','Un número entero'), 
       ('w_svpt','Número de puntos ganados al servicio del ganador','Un número entero'), 
       ('w_1stIn','Número de primeros saques metidos del ganador','Un número entero'),
       ('w_1stWon','Puntos ganados con el primer servicio del ganador','Un número entero'), 
       ('w_2ndWon','Puntos ganados con el segundo servicio del ganador','Un número entero'), 
       ('w_SvGms','Juegos al servicio ganados por el ganador','Un número entero'), 
       ('w_bpSaved','Número de Break Points salvados por el ganador','Un número entero'), 
       ('w_bpFaced','Número de Break Points jugados por el ganador','Un número entero'), 
       ('l_ace','Número de aces del perdedor','Un número entero'),
       ('l_df','Número de dobles faltas del perdedor','Un número entero'), 
       ('l_svpt','Número de puntos ganados al servicio del perdedor','Un número entero'), 
       ('l_1stIn','Número de primeros saques metidos del perdedor','Un número entero'), 
       ('l_1stWon','Puntos ganados con el primer servicio del perdedor','Un número entero'), 
       ('l_2ndWon','Puntos ganados con el segundo servicio del perdedor','Un número entero'), 
       ('l_SvGms','Juegos al servicio ganados por el perdedor','Un número entero'),
       ('l_bpSaved','Número de Break Points salvados por el perdedor','Un número entero'), 
       ('l_bpFaced','Número de Break Points jugados por el perdedor','Un número entero')]

dfOptions = pd.DataFrame(options, columns=["Campo", "Descripción", "Tipo"])
st.write(dfOptions)

uploaded_file = st.file_uploader("Elige un fichero")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

    # To read file as string:
    string_data = stringio.read()

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file, sep=";")

    #Preparacion de datos entrada
    le = LabelEncoder()
    dataframe["round"] = le.fit_transform(dataframe["round"])

    map_hand = {"R":0, "L": 1, "U":2}

    dataframe["loser_hand"].replace(map_hand, inplace=True)
    dataframe["winner_hand"].replace(map_hand, inplace=True)

    loaded_model = joblib.load( "../model/my_model.pkl")
        
    pred = loaded_model.predict(dataframe)
    dfPred = pd.DataFrame(pred, columns=["Predicción (en minutos)"])
    st.write(dfPred.round())