import streamlit as st

# Page configuration
st.set_page_config(
    page_title="DescAI Pro",
    page_icon="🚀",
    layout="centered"
)

# Header
st.title("🚀 DescAI Pro")
st.markdown("### AI-powered Shopify descriptions that convert buyers")
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

# Inputs
product = st.text_input(
    "Product Name",
    placeholder="Wireless Earbuds, Smart Watch"
)

price = st.text_input(
    "Price",
    placeholder="$49.99"
)

benefit = st.text_area(
    "Main Benefit",
    placeholder="8-hour battery life, waterproof, noise cancelling"
)

# Generate button
if st.button(
    "🚀 GENERATE PRO DESCRIPTION",
    type="primary",
    use_container_width=True
):
    if product and benefit:

        description = f"""
# {product}

🎯 Target Market: {market}

Stop settling for less. Experience premium quality that actually delivers.

## Why customers choose {product}

✅ {benefit}

✅ Premium materials built to last

✅ Fast and reliable shipping

✅ 30-day money-back guarantee

💰 Price: {price if price else '$49.99'}

⚡ Limited stock available

Upgrade your lifestyle today and order yours now.
"""

        st.success("✅ Description Ready")

        st.text_area(
            "Copy and paste this description into Shopify",
            value=description,
            height=300
        )

        st.info("🚀 Your description is ready to use.")

    else:
        st.warning(
            "⚠️ Please enter a product name and main benefit."
        )

st.divider()

st.caption(
    "DescAI Pro V2 | Built by kēllønę 🔗💨"
)
