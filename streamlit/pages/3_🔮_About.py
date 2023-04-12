import streamlit as st

st.title('Analyzing allergens in cosmetics comes with several limitations and challenges, some of which are:')

st.image('cosm_about.jpeg')

st.subheader('1. Incomplete ingredient lists 🕵🏼 :')

st.write(
    """
Some manufacturers may not disclose the complete list of ingredients on the product label, making it difficult to identify potential allergens.

    """)
st.subheader('2. Varying individual reactions 🧚‍♀️ :')
st.write(
    """
Allergic reactions are highly individual, and a substance that causes a reaction in one person may not cause the same reaction in another. This makes it challenging to determine whether a specific ingredient is an allergen for everyone.
    """
)
st.subheader('3. Complex chemical compositions 🧬 : ')

st.write(
    """
Many cosmetic products have complex chemical compositions, making it difficult to pinpoint the exact allergen responsible for an adverse reaction.
    """
)
st.subheader('4. Allergen thresholds 🧪:')

st.write(
    """
Some individuals may only experience an allergic reaction when exposed to a certain amount of an allergen. Identifying the exact threshold for each person can be challenging.
    """
)

st.subheader('5. Lack of standardized testing 🔬:')

st.write(
    """
There is no universally accepted method for testing cosmetic products for allergens, making it difficult to compare the allergenic potential of different products.
""")

st.subheader('6. Changes in product formulations 🔄 :')

st.write(
    """
Manufacturers may change product formulations over time, introducing new allergens or increasing the concentration of existing allergens. This makes it difficult to maintain up-to-date information about the allergenic potential of specific products.
""")

st.subheader(
    """
Despite these limitations, being aware of the most common allergens and carefully reading ingredient labels can help individuals with sensitive skin or a history of allergies make informed decisions when choosing cosmetic products.
    """
)

st.sidebar.title("How to use?")

with st.sidebar.beta_expander("How can I determine my skin type?"):
    st.write("[**Here**](https://www.luminskin.com/blog/556068306980/how-to-determine-your-skin-type?utm_source=google&utm_medium=cpc&utm_campaign=16950478023&utm_term=&utm_content=pmax&gclid=CjwKCAjwitShBhA6EiwAq3RqA-LiB1Bt9Hbz6BfG8X8_D1WZ_u8JFopotWKduwAdW_aKtLbtyZN1hhoC85MQAvD_BwE) you can find some information.Keep in mind that skin type can change over time due to various factors, such as age, hormones, climate, or lifestyle. It's essential to reassess your skin type periodically and adjust your skincare routine accordingly. If you're unsure about your skin type or have concerns, it's always best to consult with a dermatologist")
    st.image("type_skin.jpg")

with st.sidebar.beta_expander("How to enter the ingredients?"):
    st.write("Be sure to use a comma when entering multiple ingredients. You can also refer to the information in the 'Allergens and Ingredients' section to help you choose the right product.")
    st.image("cosm.jpeg")

with st.sidebar.beta_expander("Why are there 3 products in the output?"):
    st.write("We present you the top rated products in every price segment.")