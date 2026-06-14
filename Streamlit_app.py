import streamlit as st

# Page config
st.set_page_config(
    page_title="DescAI Pro",
    page_icon="🚀",
    layout="wide"
)

# ======================
# SIDEBAR (MENU PRO)
# ======================
st.sidebar.title("⚙️ Settings")

market = st.sidebar.selectbox(
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

languages = ["English", "French", "Spanish", "German", "Italian", "Dutch"]

default_language = "English"

if market in ["France 🇫🇷", "Benin 🇧🇯", "Senegal 🇸🇳", "Ivory Coast 🇨🇮", "Morocco 🇲🇦"]:
    default_language = "French"
elif market == "Germany 🇩🇪":
    default_language = "German"
elif market == "Spain 🇪🇸":
    default_language = "Spanish"
elif market == "Italy 🇮🇹":
    default_language = "Italian"
elif market == "Netherlands 🇳🇱":
    default_language = "Dutch"

default_index = 0
if default_language in languages:
    default_index = languages.index(default_language)

language = st.sidebar.selectbox(
    "Language",
    languages,
    index=default_index
)

tone = st.sidebar.selectbox(
    "Writing Tone",
    ["Professional", "Luxury", "Friendly", "Persuasive", "Minimalist"]
)

# ======================
# MAIN INTERFACE
# ======================
st.title("🚀 DescAI Pro")
st.markdown("### AI-powered Shopify descriptions that convert buyers")
st.divider()

col1, col2 = st.columns(2)

with col1:
    product = st.text_input("Product Name", placeholder="Wireless Earbuds, Smart Watch")
    brand = st.text_input("Brand Name", placeholder="TechPro")
    price = st.text_input("Price", placeholder="$49.99")

with col2:
    audience = st.text_input("Target Audience", placeholder="Students, athletes, professionals...")
    benefit = st.text_area("Main Benefit", placeholder="8-hour battery life, waterproof, noise cancelling")

st.subheader("Features")
feature1 = st.text_input("Feature 1", placeholder="Waterproof")
feature2 = st.text_input("Feature 2", placeholder="10-hour battery life")
feature3 = st.text_input("Feature 3", placeholder="Fast charging")

# ======================
# GENERATION
# ======================
if st.button("🚀 GENERATE PRO DESCRIPTION", type="primary", use_container_width=True):

    if product.strip() and benefit.strip():

        if tone == "Professional":
            intro = f"Introducing {product}, a reliable solution designed for modern users."
        elif tone == "Luxury":
            intro = f"Experience premium excellence with {product}, crafted for those who demand the very best."
        elif tone == "Friendly":
            intro = f"Meet {product}, the simple way to make everyday life easier."
        elif tone == "Persuasive":
            intro = f"Stop settling for average. {product} gives you the performance you deserve."
        else:
            intro = f"{product}. Smart. Efficient. Reliable."

        # TEXT OUTPUT
        if language == "French":
            description = f"""
# {product}

🏷️ Marque : {brand}
🎯 Marché : {market}

{intro}

🎯 Pour : {audience}

🔥 Avantage : {benefit}

📌 Caractéristiques:
• {feature1}
• {feature2}
• {feature3}

💰 Prix : {price if price else '49,99 €'}

⚡ Stock limité
"""
        else:
            description = f"""
# {product}

🏷️ Brand: {brand}
🎯 Market: {market}

{intro}

🎯 For: {audience}

🔥 Benefit: {benefit}

📌 Features:
• {feature1}
• {feature2}
• {feature3}

💰 Price: {price if price else '$49.99'}

⚡ Limited stock
"""

        st.success("✅ Description generated successfully")
        st.text_area("Result", value=description, height=300)

    else:
        st.warning("⚠️ Please fill Product Name and Main Benefit")

st.sidebar.divider()
st.sidebar.caption("DescAI Pro | SaaS UI version 🚀")
