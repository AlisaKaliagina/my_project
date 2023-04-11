import streamlit as st
import pandas as pd

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
    st.title("Product Recommendation App")
    
    cat = ['Moisturizer', 'Cleanser', 'Treatment', 'Face Mask', 'Eye Cream', 'Sun protect']
    type_skin = ['Dry', 'Oily', 'Normal', 'Combination', 'Sensitive']

    category = st.selectbox("What kind of product are you searching for?", cat)
    skin_type = st.selectbox("What is your skin type?", type_skin)
    exclude_ingr = st.text_input("What ingredients (allergens) do you want to exclude from the product? If you wanted to enter multiple ingredients, please enter them separated by commas")

    if st.button("Find Products"):
        exclude_ingr = [a.strip() for a in exclude_ingr.split(",")]
        filtered_products = filter_products(category, skin_type, exclude_ingr)

        if filtered_products.empty:
            st.write("Sorry, no products match your criteria. Please try again.")
        else:
            st.write(filtered_products)

