import streamlit as st

st.subheader('Future Works')
st.write(
    """
    This tool is a work in progress and will continue to be developed moving forward. Adding other blockchains,
    more KPIs and metrics, optimizing the code in general, enhancing the UI/UX of the tool, and more importantly,
    improving the data pipeline by utilizing [**Flipside ShroomDK**](https://sdk.flipsidecrypto.xyz/shroomdk) are
    among the top priorities for the development of this app. Feel free to share your feedback, suggestions, and
    also critics with me.
    """
)

c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Data Analyst: [@AlisaK](https://www.linkedin.com/in/alisa-kaliagina/)**', icon="💡")
with c2:
    st.info('**GitHub: [@AlisaKaligina](https://github.com/AlisaKaliagina)**', icon="💻")
with c3:
    st.info('**Data: [Cosmetics datasets](https://www.kaggle.com/datasets/kingabzpro/cosmetics-datasets)**', icon="🧠")