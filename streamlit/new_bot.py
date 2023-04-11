import streamlit as st
import pandas as pd

st.title("AllergenNix")
st.write("""Your beautytool """)
st.image('skin-jumbo-v2.gif')

st.sidebar.title("Find your product")
st.sidebar.info(
    """
    Allergens and ingredients.
    """
)
with st.sidebar.beta_expander("Learn more about allergens and ingredients"):
    st.write("Of course any part of the body can show an allergic reaction to cosmetic products. But, usually the more sensitive areas are those where the skin is thinner and more sensitive, such as the face, neck, décolletage and inner arms.")
    st.image("31SKIN-superJumbo.gif")

st.sidebar.info("Contact")

# Загружаем новые оптимизированные данные
DATA = ('products_new_df.csv')
@st.cache # для оптимизации работы приложения

# Создадим функцию для загрузки данных
def load_data():
    df = pd.read_csv(DATA)
    return df   

# Применим функцию 
df = load_data()

def filter_products(category, skin_type, exclude_ingr):
    filtered_df = df[df["Label"] == category]
    filtered_df = filtered_df[filtered_df[skin_type] == 1]
    for allergen in exclude_ingr:
        filtered_df = filtered_df[~filtered_df["Ingredients"].str.contains(allergen)]

    low_price = filtered_df['Price'].quantile(0.33)
    mid_price = filtered_df['Price'].quantile(0.67)

    budget_products = filtered_df[filtered_df['Price'] <= low_price].sort_values(by='Rank', ascending=False).head(1)
    normal_products = filtered_df[(filtered_df['Price'] > low_price) & (filtered_df['Price'] <= mid_price)].sort_values(by='Rank', ascending=False).head(1)
    luxury_products = filtered_df[filtered_df['Price'] > mid_price].sort_values(by='Rank', ascending=False).head(1)

    result = pd.concat([budget_products, normal_products, luxury_products])
    result=result[['Brand','Name','Price','Rank']]

    return result

categories = ['Moisturizer', 'Cleanser', 'Treatment', 'Face Mask', 'Eye Cream', 'Sun protect']
skin_types = ['Dry', 'Oily', 'Normal', 'Combination', 'Sensitive']

selected_category = st.selectbox('What kind of product are you searching for?', categories)
selected_skin_type = st.selectbox('What is your skin type?', skin_types)
exclude_ingr = st.text_input('What ingredients (allergens) do you want to exclude from the product? If you wanted to enter multiple ingredients, please enter them separated by commas')

if st.button('Find Products'):
    exclude_ingr_list = [a.strip() for a in exclude_ingr.split(",")]
    filtered_products = filter_products(selected_category, selected_skin_type, exclude_ingr_list)

    if filtered_products.empty:
        st.write('Sorry, no products match your criteria. Please try again.')
    else:
        st.write(filtered_products.to_html(index=False, border=0, justify="center"), unsafe_allow_html=True)



c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Data Analyst: [@AlisaK](https://www.linkedin.com/in/alisa-kaliagina/)**', icon="💡")
with c2:
    st.info('**GitHub: [@AlisaKaligina](https://github.com/AlisaKaliagina)**', icon="💻")
with c3:
    st.info('**Data: [Cosmetics datasets](https://www.kaggle.com/datasets/kingabzpro/cosmetics-datasets)**', icon="🧠")