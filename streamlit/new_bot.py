import streamlit as st
import pandas as pd


st.markdown(
    """
<style>
body {
    background-color: #98FB98;
}
</style>
""",
    unsafe_allow_html=True,
)

st.title("AllergenNix")
st.write("""Your beautytool """)
st.image('skin-jumbo-v2.gif')

st.sidebar.title("Find your product")
st.sidebar.info(
    """
    Allergens and ingredients.
    """
)
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

