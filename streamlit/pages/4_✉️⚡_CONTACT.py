import streamlit as st

st.subheader('Future Works')
st.write(
    """
    Thank you for using AllergenNix! I'm constantly working to improve this app and provide you with the most accurate and relevant information on cosmetic products.

    If you have any questions, suggestions, or if you're interested in discussing potential collaborations, feel free to reach out to me:
    """
)

c1, c2, c3 = st.columns(3)
with c1:
    st.info('**LinkedIn: [@AlisaK](https://www.linkedin.com/in/alisa-kaliagina/)**', icon="💡")
with c2:
    st.info('**GitHub: [@AlisaKaligina](https://github.com/AlisaKaliagina)**', icon="💻")
with c3:
    st.info('**E-mail: [steiger2212@gmail.com](mailto:steiger2212@gmail.com)**', icon="✍️")