# Importamos librerías
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.calibration import LabelEncoder
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.linear_model import Lasso, Ridge, LinearRegression
from sklearn.linear_model import ElasticNet
from sklearn.svm import LinearSVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import joblib

#Lectura del fichero desde data/raw
data = pd.read_csv(r"src\data\raw\atp_matches_2023.csv", sep=";")

#Eliminamos las columnas que nos nos interesan
data.drop(columns=["tourney_id", "draw_size", "tourney_date", "match_num", "winner_name", "winner_seed", "loser_seed",
                   "loser_name", "score", "winner_rank", "winner_rank_points","loser_rank", "loser_rank_points", "winner_entry", "loser_entry"], inplace=True)

# Tratamiento de NaNs
data.dropna(subset=['w_ace', 'w_df', 'w_svpt', 'w_1stIn', 'w_1stWon'], inplace=True)
data["winner_ht"].fillna(data["winner_ht"].mean(), inplace=True)
data["loser_ht"].fillna(data["loser_ht"].mean(), inplace=True)
data["loser_age"].fillna(data["loser_age"].mean(), inplace=True)
data["minutes"].fillna(data["minutes"].mean(), inplace=True)

#Escalado de datos
columns_LE = ["tourney_name", "winner_ioc", "loser_ioc", "round"]
le = LabelEncoder()

data["tourney_name"] = le.fit_transform(data["tourney_name"])
data["winner_ioc"] = le.fit_transform(data["winner_ioc"])
data["loser_ioc"] = le.fit_transform(data["loser_ioc"])
data["round"] = le.fit_transform(data["round"])

map_surface = {"Hard":0, "Clay": 1, "Grass":2}
map_hand = {"R":0, "L": 1, "U":2}
map_tourney = {"A":0, "M": 1, "G":2}

data["surface"].replace(map_surface, inplace=True)
data["loser_hand"].replace(map_hand, inplace=True)
data["winner_hand"].replace(map_hand, inplace=True)
data["tourney_level"].replace(map_tourney, inplace=True)

#División de datos y Train-test split
X = data.drop("minutes", axis=1)
y = data["minutes"]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8, random_state = 42)

#Entrenamiento del modelo
rforest = RandomForestRegressor(bootstrap= True, max_depth= 80, max_features= 30, min_samples_leaf= 3, min_samples_split= 8, n_estimators= 1000)
rforest.fit(X_train, y_train)

#Guardamos modelo
joblib.dump(rforest, r"src\model\my_model.plk")

print("Modelo guardado")