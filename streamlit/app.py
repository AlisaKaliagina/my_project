import streamlit as st
import pandas as pd
import numpy as np

df=pd.read_csv('products_new_df.csv')
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

def main():
    cat = ['Moisturizer', 'Cleanser', 'Treatment', 'Face Mask', 'Eye Cream', 'Sun protect']
    type_skin = ['Dry', 'Oily', 'Normal', 'Combination', 'Sensitive']
    category = input('What kind of product are u searchig for? (Moisturizer, Cleanser, Treatment, Eye cream, Face Mask, Sun protect)').title().strip()

    while category not in cat:
        print('Please choose category of product: Moisturizer, Cleanser, Treatment, Eye cream, Face Mask, Sun protect')
        category = input().title().strip()
        break

    skin_type = input('What is your skin type? (Dry, Oily, Normal, Combination, Sensitive)').title().strip()
    
    while skin_type not in type_skin:
        print('Please choose your type of skin')
        skin_type = input().title().strip()
        break

    exclude_ingr = input('What ingredients (allergens) do you want to exclude from the product? If you wanted to enter multiple ingredients, please enter them separated by commas').title().strip()
    exclude_ingr = [a.strip() for a in exclude_ingr.split(",")]

    filtered_products = filter_products(category, skin_type, exclude_ingr)
    
    if filtered_products.empty:
        print('Sorry, no products match your criteria. Please try again.')
        filtered_products = main()

    return filtered_products

main()

# Заголовок и вступление
st.title("Консультант по уходу за кожей")
st.write("Добро пожаловать! Этот инструмент поможет вам найти подходящие продукты для ухода за кожей на основе ваших предпочтений и типа кожи.")

# Вместо использования ввода с клавиатуры используйте виджеты Streamlit для получения пользовательских данных
category = st.selectbox("Выберите категорию продукта", ['Moisturizer', 'Cleanser', 'Treatment', 'Face Mask', 'Eye Cream', 'Sun protect'])
skin_type = st.selectbox("Выберите тип кожи", ['Dry', 'Oily', 'Normal', 'Combination', 'Sensitive'])
exclude_ingr = st.text_input("Введите ингредиенты (аллергены), которые вы хотите исключить из продукта. Если вы хотите ввести несколько ингредиентов, разделите их запятыми")

# Кнопка для запуска поиска продуктов
if st.button("Найти продукты"):
    exclude_ingr_list = [a.strip() for a in exclude_ingr.split(",")]
    filtered_products = filter_products(category, skin_type, exclude_ingr_list)

    if filtered_products.empty:
        st.write("Извините, подходящих продуктов не найдено. Попробуйте изменить критерии поиска.")
    else:
        st.write(filtered_products)

