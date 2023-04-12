import streamlit as st


st.title('Allergens and Ingredients in Cosmetics')
st.write(
    """
    Cosmetics contain a variety of ingredients, some of which can be potential allergens. Allergic reactions can occur when the immune system overreacts to a particular ingredient, causing symptoms such as itching, redness, and swelling.

Common allergens in cosmetics include fragrances, preservatives, and certain dyes. It's important to note that just because an ingredient is natural or organic doesn't mean it's necessarily safe for everyone.
    """)
st.subheader(
    """
❗ Some natural ingredients can also cause allergic reactions.❗
    """
)
st.image('clean_beauty.jpeg')

st.write(
    """
To prevent allergic reactions, it's important to read the labels and ingredient lists of cosmetics carefully. If you have a known allergy to a particular ingredient, avoid products that contain it. If you're unsure about a particular ingredient, do a patch test before using the product on your entire face or body.
    """)
st.subheader(
    """
🚨 If you do experience an allergic reaction to a cosmetic product, stop using it immediately and seek medical attention if the symptoms are severe or persistent.🚨
    """
)

st.title(           'Allergen Awareness'            )

st.image('allergens-TITOLO.png')

st.write(
    """
Allergic reactions are highly individual, but we strongly recommend familiarizing yourself with **[the 26 recognized allergens](https://en.ecomundo.eu/blog/allergenes-cosmetique-conformite)** to ensure the safety and well-being of your skin. These allergens, established by the European Union, are commonly found in cosmetic products and can trigger allergic reactions in sensitive individuals.

While not everyone may experience an adverse reaction to these allergens, it's crucial to be aware of them, especially if you have a history of allergies or sensitive skin. By knowing the allergens and understanding their potential effects, you can make informed decisions when choosing skincare products that are best suited for your needs.

Remember, the presence of these allergens doesn't necessarily mean a product is harmful, but rather that it may cause a reaction in susceptible individuals. Always perform a patch test before using a new product, and consult with a dermatologist if you're unsure or have concerns about specific ingredients.
    """
)
st.sidebar.title("FAQ:")

with st.sidebar.beta_expander("What are the most common allergens in cosmetic products?"):
    st.write("Common allergens: fragrances, preservatives, dyes, nickel, and some plant ingredients.")
    st.image("find_ingr.webp")

with st.sidebar.beta_expander("What symptoms might indicate an allergic reaction to a cosmetic product?"):
    st.write("Allergy symptoms to cosmetics: itching, redness, swelling, rash, or skin irritation.")
    

with st.sidebar.beta_expander("Are there hypoallergenic cosmetic products available?"):
    st.write("Hypoallergenic products exist, but they don't guarantee a complete absence of an allergic reaction.")
    st.image("cosm.jpeg")

with st.sidebar.beta_expander("Can a product labeled as 'natural' or 'organic' cause allergic reactions?"):
    st.write("Even natural and organic products can cause allergies, as some natural ingredients are allergens.🌾")
    