import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Tennis Predict ML",
    page_icon="🎾",
)

st.title("Tennis Predict" )
st.subheader("Un modelo predictivo sobre el mundo del tenis 🎾")

st.sidebar.info("Selecciona una de las páginas para navegar.")

image = Image.open("src/prod/img/tennis.jpeg")
st.image(image)

st.write("### 🔗 Origen de los datos")

text="Los datos se han extraído de kaggle (https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)"
st.markdown(text,unsafe_allow_html=True)

st.write("### 🔗 Repositorio en Github")
text="https://github.com/jmayordomom/ML_TennisPredict"
st.markdown(text,unsafe_allow_html=True)

st.sidebar.markdown('---')

st.sidebar.markdown('App creada por Jaime Mayordomo')