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

st.markdown("# ModelPrediction")
st.write("Esta página permite realizar una prediccion con datos propios")


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

    
    #Lectura del fichero desde data/raw
    # data = pd.read_csv("../data/raw/atp_matches_2023.csv", sep=";")

    # #Eliminamos las columnas que nos nos interesan
    # data.drop(columns=["tourney_id", "draw_size", "tourney_date", "match_num", "winner_name", "winner_seed", "loser_seed",
    #                 "loser_name", "score", "winner_rank", "winner_rank_points","loser_rank", "loser_rank_points", "winner_entry", "loser_entry"], inplace=True)

    # # Tratamiento de NaNs
    # data.dropna(subset=['w_ace', 'w_df', 'w_svpt', 'w_1stIn', 'w_1stWon'], inplace=True)
    # data["winner_ht"].fillna(data["winner_ht"].mean(), inplace=True)
    # data["loser_ht"].fillna(data["loser_ht"].mean(), inplace=True)
    # data["loser_age"].fillna(data["loser_age"].mean(), inplace=True)
    # data["minutes"].fillna(data["minutes"].mean(), inplace=True)

    # #Escalado de datos
    # columns_LE = ["tourney_name", "winner_ioc", "loser_ioc", "round"]
    # le = LabelEncoder()

    # data["tourney_name"] = le.fit_transform(data["tourney_name"])
    # data["winner_ioc"] = le.fit_transform(data["winner_ioc"])
    # data["loser_ioc"] = le.fit_transform(data["loser_ioc"])
    # data["round"] = le.fit_transform(data["round"])

    # map_surface = {"Hard":0, "Clay": 1, "Grass":2}
    # map_hand = {"R":0, "L": 1, "U":2}
    # map_tourney = {"A":0, "M": 1, "G":2}

    # data["surface"].replace(map_surface, inplace=True)
    # data["loser_hand"].replace(map_hand, inplace=True)
    # data["winner_hand"].replace(map_hand, inplace=True)
    # data["tourney_level"].replace(map_tourney, inplace=True)

    # data = np.log(data + 1)

    # #División de datos y Train-test split
    # X = data.drop(columns=["minutes", "tourney_name", "surface","tourney_level",'winner_ioc','loser_ioc','winner_ht','loser_ht'], axis=1)
    # y = data["minutes"]

    # X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8, random_state = 42)

    # #Entrenamiento del modelo
    # rforest = RandomForestRegressor(bootstrap= False, max_depth= 80, max_features= 15, min_samples_leaf= 3, min_samples_split= 8, n_estimators= 500)
    # rforest.fit(X_train, y_train)

    #Preparacion de datos entrada
    le = LabelEncoder()
    dataframe["round"] = le.fit_transform(dataframe["round"])

    map_hand = {"R":0, "L": 1, "U":2}

    dataframe["loser_hand"].replace(map_hand, inplace=True)
    dataframe["winner_hand"].replace(map_hand, inplace=True)

    loaded_model = joblib.load( "../model/my_model.pkl")
        
    mape = loaded_model.predict(dataframe)
    # pred = rforest.predict(dataframe)
    # st.markdown(y_test.shape[0])
    # st.markdown(pred.shape[0])
    # mape = mean_absolute_percentage_error(y_test, pred)
    st.markdown(mape)