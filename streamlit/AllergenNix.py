import streamlit as st
import pandas as pd

st.title("AllergenNix")

st.markdown("""**:blue[Free your skin from allergens with AllergenNix - your reliable tool for safe and healthy skin!]**""")

st.image('skin-jumbo-v2.gif')

st.sidebar.title("How to use?")

with st.sidebar.beta_expander("How can I determine my skin type?"):
    st.write("[**Here**](https://www.luminskin.com/blog/556068306980/how-to-determine-your-skin-type?utm_source=google&utm_medium=cpc&utm_campaign=16950478023&utm_term=&utm_content=pmax&gclid=CjwKCAjwitShBhA6EiwAq3RqA-LiB1Bt9Hbz6BfG8X8_D1WZ_u8JFopotWKduwAdW_aKtLbtyZN1hhoC85MQAvD_BwE) you can find some information.Keep in mind that skin type can change over time due to various factors, such as age, hormones, climate, or lifestyle. It's essential to reassess your skin type periodically and adjust your skincare routine accordingly. If you're unsure about your skin type or have concerns, it's always best to consult with a dermatologist")
    st.image("type_skin.jpg")

with st.sidebar.beta_expander("How to enter the ingredients?"):
    st.write("Be sure to use a comma when entering multiple ingredients. You can also refer to the information in the 'Allergens and Ingredients' section to help you choose the right product.")
    st.image("commas.jpg")

with st.sidebar.beta_expander("Why are there 3 products in the output?"):
    st.write("We present you the top rated products in every price segment.")

with st.sidebar.beta_expander("How do I perform an allergy test before using a new cosmetic product?"):
    st.write("For an allergy test, apply a small amount of the product to a patch of skin and wait 24-48 hours.")
    st.image('patch.webp')
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
exclude_ingr = st.text_input('What ingredients (allergens) do you want to exclude from the product?❌❓ (❗If you want to enter multiple ingredients, please enter them separated by commas❗)')

if st.button('Find Products'):
    exclude_ingr_list = [a.strip() for a in exclude_ingr.split(",")]
    filtered_products = filter_products(selected_category, selected_skin_type, exclude_ingr_list)

    if filtered_products.empty:
        st.write('Sorry, no products match your criteria. Please try again.')
    else:
        st.write(filtered_products.to_html(index=False, border=0, justify="center"), unsafe_allow_html=True)


