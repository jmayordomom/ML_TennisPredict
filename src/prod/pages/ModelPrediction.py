from sklearn.calibration import LabelEncoder
from sklearn.linear_model import ElasticNet, Lasso, Ridge
from sklearn.model_selection import cross_validate, train_test_split
from sklearn.svm import LinearSVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import ElasticNet
from sklearn.svm import LinearSVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

import sklearn
import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="ModelPrediction", page_icon="📈")

st.markdown("# ModelPrediction")
st.sidebar.header("ModelPrediction")
st.write("#### Esta página muestra información relativa a la métrica a predecir, y a los modelos utilizados")

#Carga datos
data = pd.read_csv("src/data/processed/tennisResults.csv")

#Escalado
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

#Train Test Split
X = data.drop(columns=["minutes", "tourney_name", "surface",	"tourney_level",'winner_ioc','loser_ioc','winner_ht','loser_ht'], axis=1)
X = np.log(X + 1)
y = data["minutes"]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8, random_state = 42)

#CV + Base Lines
modelos = {
   "Ridge": Ridge(alpha=0.1, solver="cholesky"),
    "Lasso": Lasso(alpha=0.1),
    "ElasticNet": ElasticNet(alpha=0.1, l1_ratio=0.5),
    "LinearSVR": LinearSVR(epsilon=0.5, dual=True, random_state=42),
    "DecissionTree":DecisionTreeRegressor(max_depth=2, random_state=42),
    "RandomForest":RandomForestRegressor(n_estimators=10, random_state=42)
}

# Define las métricas a usar
metricas = ["neg_mean_absolute_percentage_error", "neg_root_mean_squared_error"]

resultados_dict = {}

for nombre_modelo, modelo in modelos.items():
    cv_resultados = cross_validate(modelo, X_train, y_train, cv=5, scoring=metricas)
    
    for metrica in metricas:
        clave = f"{nombre_modelo}_{metrica}"
        resultados_dict[clave] = cv_resultados[f"test_{metrica}"].mean()

# Convertir el diccionario de resultados en DataFrame
resultados_df = pd.DataFrame([resultados_dict])
resultados_df = resultados_df.T
resultados_df = abs(resultados_df).sort_values(by=0, ascending=True)

st.write('## Medida a predecir')
st.write("Se va a predecir el número de minutos que va a durar un partido")

st.write('## Modelos utilizados para CV')
s = ""
models = ["Ridge", "Lasso", "ElasticNet", "LinearSVR", "DecissionTree", "RandomForest"]
for mode in models:
    s += "- " + mode + "\n"

st.markdown(s)
s = ""
st.write('## Métricas utilizadas para CV')
for mode in metricas:
    s += "- " + mode + "\n"

st.markdown(s)
# Datos partido
st.write('## Resultados tras Cross Validation')

col1, col2, col3 = st.columns(3)
with col1:
    st.write('### Mejor modelo')
    st.write("Random Forest Regressor")

with col2:
    st.write('### Mejor métrica')
    st.write("MAPE")

with col3:
    st.write('### Score')
    st.write("0.0094")

st.write(r"#### Podemos ver que se obtiene un buen resultado, con un 9% de error")