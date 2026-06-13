import streamlit as st

# Page configuration
st.set_page_config(
    page_title="DescAI - Generator",
    page_icon="🚀",
    layout="centered"
)

# Title
st.title("🚀 DescAI")
st.markdown("### Generate high-converting Shopify product descriptions in seconds")

st.divider()

# Target Market
market = st.selectbox(
    "Target Market",
    [
        "United States 🇺🇸",
        "United Kingdom 🇬🇧",
        "Canada 🇨🇦",
        "Australia 🇦🇺",
        "France 🇫🇷",
        "Germany 🇩🇪",
        "Spain 🇪🇸",
        "Italy 🇮🇹",
        "Netherlands 🇳🇱",
        "South Africa 🇿🇦",
        "Nigeria 🇳🇬",
        "Kenya 🇰🇪",
        "Ghana 🇬🇭",
        "Benin 🇧🇯",
        "Senegal 🇸🇳",
        "Ivory Coast 🇨🇮",
        "Morocco 🇲🇦",
        "Worldwide 🌍"
    ]
)

# Input fields
col1, col2 = st.columns(2)

with col1:
    product = st.text_input(
        "Product Name",
        placeholder="Example: Wireless Headphones, Nike Shoes..."
    )

with col2:
    price = st.text_input(
        "Price",
        placeholder="Example: $29.99"
    )

benefit = st.text_area(
    "Main Benefit",
    placeholder="Example: Noise cancellation, all-day comfort..."
)

# Generate button
if st.button("🚀 GENERATE DESCRIPTION"):

    if product and benefit:

        description = f"""
✨ **{product}**

🎯 Target Market: {market}

Discover the {product}, designed to provide {benefit}.

✅ Premium quality and durability
✅ Fast shipping
✅ Satisfaction guarantee
✅ Secure payment

💰 Price: {price if price else 'Contact us'}

Order yours today and upgrade your lifestyle!
"""

        st.success("✅ Description generated successfully!")

        st.text_area(
            "Copy this description to Shopify",
            value=description,
            height=250
        )

    else:
        st.error("⚠️ Please enter the product name and main benefit.")

st.divider()

st.caption("DescAI V1 - Built by kēllønę 🔗💨")
