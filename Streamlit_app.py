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

# Automatic language selection
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

language = st.selectbox(
    "Language",
    ["English", "French", "Spanish", "German", "Italian", "Dutch"],
    index=["English", "French", "Spanish", "German", "Italian", "Dutch"].index(default_language)
)

# Writing Tone
tone = st.selectbox(
    "Writing Tone",
    ["Professional", "Luxury", "Friendly", "Persuasive", "Minimalist"]
)

# Inputs
product = st.text_input("Product Name", placeholder="Wireless Earbuds, Smart Watch")
brand = st.text_input("Brand Name", placeholder="TechPro")
audience = st.text_input("Target Audience", placeholder="Students, athletes, professionals...")
price = st.text_input("Price", placeholder="$49.99")
benefit = st.text_area("Main Benefit", placeholder="8-hour battery life, waterproof, noise cancelling")
feature1 = st.text_input("Feature 1", placeholder="Waterproof")
feature2 = st.text_input("Feature 2", placeholder="10-hour battery life")
feature3 = st.text_input("Feature 3", placeholder="Fast charging")

# Generate button
if st.button("🚀 GENERATE PRO DESCRIPTION", type="primary", use_container_width=True):

    if product and benefit:

        # Tone intro
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

        # Language output
        if language == "French":
            description = f"""
# {product}

🏷️ Marque : {brand}
🎯 Marché cible : {market}

{intro}

Conçu pour : {audience}

✅ Avantage principal : {benefit}

Caractéristiques :
• {feature1}
• {feature2}
• {feature3}

💰 Prix : {price if price else '49,99 €'}

⚡ Stock limité

Commandez dès aujourd'hui.
"""

        elif language == "Spanish":
            description = f"""
# {product}

🏷️ Marca: {brand}
🎯 Mercado objetivo: {market}

{intro}

Diseñado para: {audience}

✅ Beneficio principal: {benefit}

Características:
• {feature1}
• {feature2}
• {feature3}

💰 Precio: {price if price else '49,99 €'}

⚡ Stock limitado

Pide el tuyo hoy.
"""

        elif language == "German":
            description = f"""
# {product}

🏷️ Marke: {brand}
🎯 Zielmarkt: {market}

{intro}

Entwickelt für: {audience}

✅ Hauptvorteil: {benefit}

Merkmale:
• {feature1}
• {feature2}
• {feature3}

💰 Preis: {price if price else '49,99 €'}

⚡ Begrenzter Vorrat

Jetzt bestellen.
"""

        elif language == "Italian":
            description = f"""
# {product}

🏷️ Marca: {brand}
🎯 Mercato di riferimento: {market}

{intro}

Progettato per: {audience}

✅ Vantaggio principale: {benefit}

Caratteristiche:
• {feature1}
• {feature2}
• {feature3}

💰 Prezzo: {price if price else '49,99 €'}

⚡ Disponibilità limitata

Ordina oggi stesso.
"""

        elif language == "Dutch":
            description = f"""
# {product}

🏷️ Merk: {brand}
🎯 Doelmarkt: {market}

{intro}

Ontworpen voor: {audience}

✅ Belangrijkste voordeel: {benefit}

Kenmerken:
• {feature1}
• {feature2}
• {feature3}

💰 Prijs: {price if price else '49,99 €'}

⚡ Beperkte voorraad

Bestel vandaag nog.
"""

        else:
            description = f"""
# {product}

🏷️ Brand: {brand}
🎯 Target Market: {market}

{intro}

Designed for: {audience}

✅ Main Benefit: {benefit}

Features:
• {feature1}
• {feature2}
• {feature3}

💰 Price: {price if price else '$49.99'}

⚡ Limited stock available

Order yours today and upgrade your lifestyle.
"""

        st.success("✅ Description Ready")
        st.text_area("Copy and paste this description into Shopify", value=description, height=350)

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Status", "Ready")
        with col2:
            st.metric("Quality", "PRO")

    else:
        st.warning("⚠️ Please enter at least the product name and main benefit.")

st.divider()
st.caption("DescAI Pro V5 | Built by kēllønę 🔗💨")
