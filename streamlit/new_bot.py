import streamlit as st
import pandas as pd

st.title("AllergenNix")
st.write("""Your beautytool """)
st.image('skin-jumbo-v2.gif')

st.sidebar.title("Info")
st.sidebar.info(
    """
    This app is Open Source dashboard.
    """
)
st.sidebar.info("#Тест "
                "Тест")
# Загружаем новые оптимизированные данные
DATA = ('products_new_df.csv')
@st.cache # для оптимизации работы приложения

# Создадим функцию для загрузки данных
def load_data():
    df = pd.read_csv(DATA)
    return df   

# Применим функцию 
df = load_data()
st.write (df)

