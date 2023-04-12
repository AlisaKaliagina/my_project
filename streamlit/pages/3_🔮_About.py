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

st.sidebar.title("What you should know ✅:")
    
with st.sidebar.beta_expander("Can a fragrance-free product contain allergens?"):
    st.write("Fragrance-free means the absence of artificial fragrances, but the product may contain allergens.")
    #st.image("type_skin.jpg")

with st.sidebar.beta_expander("If my product contains one of the 26 allergens, does this mean that I should refuse the product?"):
    st.write("""
    If your cosmetic product contains one of the 26 allergens, it doesn't necessarily mean that you must stop using the product. 
    
    It is essential to consider your individual sensitivity or allergy history. 
    If you have experienced allergic reactions to cosmetic products in the past or suspect you might be allergic to specific ingredients, it's advisable to perform a patch test before using the product or consult a dermatologist.
    """
    )
    st.image("skin_dang.ipeg")

with st.sidebar.beta_expander("What regulatory requirements exist for allergen labeling in cosmetic products?"):
    st.write("Regulatory requirements for allergen labeling vary depending on the country.")
    st.image("cosmetics_labeling.gif")

with st.sidebar.beta_expander("Does the price of a cosmetic product depend on the amount of allergens it contains?"):
    
    st.write(
     """
The price of a cosmetic product is not necessarily dependent on the number of allergens it contains.

Other factors, such as the quality of ingredients, brand reputation, and packaging, can also affect the price of a cosmetic product. 

However, some companies may use higher-quality, hypoallergenic ingredients and charge a premium for their products as a result. Ultimately, it's important to carefully read the ingredient labels and choose products that work for your skin type and personal preferences, regardless of the price."""
)