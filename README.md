# 📊 Proyecto de Machine Learning: ML TennisPredict 🎾
¡Bienvenidos a ML Tennis Predict! Un proyecto de predicción de estadísticas sobre partidos de tenis

## 🎯 Objetivo 
EL objetivo de este proyecto de Machine Learning es predecir la duración en minutos de un partido de tenis

## 🔗 Enlace a API
[Enlace a API en Streamlit](https://mltennispredict.streamlit.app/)

## ℹ️ Datos con los que vamos a trabajar
|Nombre    | Descripción      |
|----------|------------------|
|Campo|Descripción|
|winner_id|Identificador del jugador ganador|
|winner_hand|Mano predominante del ganador|
|winner_age|Edad del ganador|
|w_svpt|Número de puntos ganados al servicio del ganador|
|w_SvGms|Juegos al servicio ganados por el ganador|
|w_df|Número de dobles faltas del ganador|
|w_bpSaved|Número de Break Points salvados por el ganador|
|w_bpFaced|Número de Break Points jugados por el ganador|
|w_ace|Número de aces del ganador|
|w_2ndWon|Puntos ganados con el segundo servicio del ganador|
|w_1stWon|Puntos ganados con el primer servicio del ganador|
|w_1stIn|Número de primeros saques metidos del ganador|
|round|Ronda del partido|F (Final), SF (Semifinal), QF (cuartos de final), R16 (Octavos), R32 (Tercera ronda), R64 (Segunda ronda), R128 (Primera ronda) o  RR (Round Robin)
|loser_id|Identificador del jugador perdedor|
|loser_hand|Mano predominante del perdedor|
|loser_age|Edad del perdedor|
|l_svpt|Número de puntos ganados al servicio del perdedor|
|l_SvGms|Juegos al servicio ganados por el perdedor|
|l_df|Número de dobles faltas del perdedor|
|l_bpSaved|Número de Break Points salvados por el perdedor|
|l_bpFaced|Número de Break Points jugados por el perdedor|
|l_ace|Número de aces del perdedor|
|l_2ndWon|Puntos ganados con el segundo servicio del perdedor|
|l_1stWon|Puntos ganados con el primer servicio del perdedor|
|l_1stIn|Número de primeros saques metidos del perdedor|
|best_of|Número de sets a los que se juega el partido|

## 🛠️ Tecnologías Utilizadas

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- scikit-learn
- joblib
- streamlit

## 📂 Estructura del Repositorio

- **data**: Carpeta que contiene los conjuntos de datos utilizados en el análisis. Contiene los datos en bruto (subcarpeta **raw**), procesados (subcarpeta **processed**) y una prueba para la predicción (subcarpeta **testPred**)
- **model**: modelo entrenado en formato pkl
- **notebooks**: Carpeta que contiene los Jupyter Notebooks con el código de análisis y procesamiento.
- **prod**: Contiene los ficheros con formato *py* utilizados para realizar la productivización del proyecto en Streamlit
- **README.md**: Este archivo que proporciona una descripción general del proyecto.