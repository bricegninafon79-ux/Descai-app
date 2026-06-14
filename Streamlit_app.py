import streamlit as st

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="DescAI Pro",
    page_icon="🚀",
    layout="wide"
)

# ======================
# TITLE
# ======================
st.title("🚀 DescAI Pro")
st.markdown("### AI-powered Shopify descriptions that convert buyers")
st.divider()

# ======================
# PRICING CARDS
# ======================
st.subheader("💎 Choose Your Plan")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🟢 Basic")
    st.markdown("Simple & fast product descriptions")
    st.markdown("✔ Good for testing products")
    st.markdown("✔ Clean structure")
    st.markdown("❌ No marketing boost")
    st.markdown("💰 $0 / Free")
    basic = st.button("Select Basic")

with col2:
    st.markdown("### 🔵 Premium")
    st.markdown("High converting Shopify descriptions")
    st.markdown("✔ Persuasive writing")
    st.markdown("✔ Marketing optimized")
    st.markdown("✔ Better sales structure")
    st.markdown("💰 $9.99 / month")
    premium = st.button("Select Premium")

with col3:
    st.markdown("### 🟣 Ultra")
    st.markdown("Elite conversion + sales copy")
    st.markdown("✔ Emotional marketing")
    st.markdown("✔ Urgency & scarcity")
    st.markdown("✔ Maximum conversion style")
    st.markdown("💰 $19.99 / month")
    ultra = st.button("Select Ultra")

# ======================
# PLAN LOGIC
# ======================
if basic:
    level = "Basic"
    st.success("Basic plan selected")
elif premium:
    level = "Premium"
    st.success("Premium plan selected")
elif ultra:
    level = "Ultra"
    st.success("Ultra plan selected")
else:
    level = "Basic"

st.divider()

# ======================
# SIDEBAR SETTINGS
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
# INPUTS
# ======================
col1, col2 = st.columns(2)

with col1:
    product = st.text_input("Product Name", placeholder="Wireless Earbuds, Smart Watch")
    brand = st.text_input("Brand Name", placeholder="TechPro")
    price = st.text_input("Price", placeholder="$49.99")

with col2:
    audience = st.text_input("Target Audience", placeholder="Students, athletes, professionals...")
    benefit = st.text_area("Main Benefit", placeholder="8-hour battery life, waterproof, noise cancelling")

st.subheader("Features")
feature1 = st.text_input("Feature 1")
feature2 = st.text_input("Feature 2")
feature3 = st.text_input("Feature 3")

# ======================
# LEVEL SYSTEM (COPYWRITING ENGINE)
# ======================
def get_intro(level, tone, product):

    if level == "Basic":
        return f"{product} is a simple and functional product designed for everyday use."

    elif level == "Premium":
        if tone == "Luxury":
            return f"Experience refined excellence with {product}, designed for high performance and style."
        else:
            return f"{product} delivers strong performance, comfort, and reliability for daily use."

    else:  # Ultra
        if tone == "Luxury":
            return f"Step into luxury with {product} — designed to impress and dominate expectations."
        else:
            return f"Don’t settle for average. {product} is built to outperform and maximize results."

# ======================
# GENERATION
# ======================
if st.button("🚀 GENERATE PRO DESCRIPTION", type="primary", use_container_width=True):

    if product.strip() and benefit.strip():

        intro = get_intro(level, tone, product)

        if language == "French":
            description = f"""
# {product}

🏷️ Marque : {brand}
🎯 Marché : {market}
💎 Plan : {level}

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
💎 Plan: {level}

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

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Plan", level)
        with col2:
            st.metric("Status", "READY")

    else:
        st.warning("⚠️ Please fill Product Name and Main Benefit")

st.sidebar.divider()
st.sidebar.caption("DescAI Pro SaaS Version 🚀") 
