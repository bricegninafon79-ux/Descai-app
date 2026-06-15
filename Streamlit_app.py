import streamlit as st

# ======================
# CONFIG
# ======================
st.set_page_config(
    page_title="DescAI Pro",
    page_icon="🚀",
    layout="wide"
)
st.markdown("""
<style>
.stApp {
    background: #0A0A0A;
    color: white;
}

h1 {
    font-weight: 800 !important;
}

.stButton > button {
    border-radius: 12px !important;
    font-weight: bold !important;
}

.stTextInput input,
.stTextArea textarea {
    border-radius: 12px !important;
}
</style>
""", unsafe_allow_html=True)

# ======================
# SESSION STATE
# ======================
if "page" not in st.session_state:
    st.session_state.page = "home"

if "plan" not in st.session_state:
    st. session_state . plan = None

si  « payé »  n'est pas  dans st. session_state :
    st.session_state.payé = Faux​​​


# ======================
# BARRE LATÉRALE GLOBALE
# ======================
st. sidebar . title ( "⚙️ Paramètres" )

marché = st. barre latérale . selectbox (
    « Marché cible »
    [ "États-Unis 🇺🇸" , "France 🇫🇷" , "Allemagne 🇩🇪" , "Monde entier 🌍" ]
)

langue = st. barre latérale . selectbox (
    "Langue" ,
    [ "Anglais" , "Français" , "Espagnol" , "Allemand" ]
)

ton = st. barre latérale . selectbox (
    « Ton de l'écriture » ,
    [ "Professionnel" , "Luxe" , "Convivial" , "Persuasif" ]
)

st. barre latérale . séparateur ( )
st.sidebar.write ( f " Plan : { st.session_state.plan } " )​​​
st.sidebar.write ( f " Payé : { st.session_state.paid } " )​​​


# ======================
# PAGE D'ACCUEIL (PLUS DE PLANS AVEC DESCRIPTION COMPLÈTE)
# ======================
def  home ( ) :

    st.markdown(
    "<h1 style='text-align:center;'>Turn Features Into Money</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;color:gray;'>AI Product Descriptions in 6 Seconds</p>",
    unsafe_allow_html=True
)

    col1, col2, col3 = st. colonnes ( 3 )

    def  select_plan ( plan ) :
        st. session_state . plan = plan
        st. session_state . page = "paiement"
        st. rediffusion ( )

    avec col1 :
        st.markdown ( "## 🟢 Basique " )
        st.markdown ( « Descriptions de produits simples et rapides » )
        st.markdown ( "✔ Structure propre " )
        st.markdown ( "✔ Idéal pour tester des produits " )
        st.markdown ( "❌ Aucune optimisation marketing " )
        st. markdown ( "💰 9,99 $ / mois" )
        si st.button ( "Sélectionner basique" , use_container_width = True ) :
            sélectionner_plan ( "Basique" )

    avec col2 :
        st.markdown ( " ## 🔵 Premium" )
        st.markdown ( « Descriptions Shopify à fort taux de conversion » )
        st.markdown ( "✔ Rédaction publicitaire persuasive " )
        st.markdown ( "✔ Optimisé pour le marketing " )
        st.markdown ( "✔ Meilleur taux de conversion " )
        st.markdown("💰 $15.99 / month")
        if st.button("Select Premium", use_container_width=True):
            select_plan("Premium")

    with col3:
        st.markdown("## 🟣 Ultra")
        st.markdown("Elite sales copywriting engine")
        st.markdown("✔ Emotional marketing")
        st.markdown("✔ Scarcity & urgency")
        st.markdown("✔ Maximum conversion focus")
        st.markdown("💰 $22.99 / month")
        if st.button("Select Ultra", use_container_width=True):
            select_plan("Ultra")


# ======================
# PAYMENT PAGE
# ======================
def payment():

    st.title("💳 Payment Required")

    st.info(f"Plan: {st.session_state.plan}")

    st.warning("You must complete payment before access")

    if st.session_state.plan == "Basic":
        st.success("Free plan")

        if st.button("Continue"):
            st.session_state.paid = True
            st.session_state.page = "app"
            st.rerun()

    else:
        if st.button("💳 Simulate Payment Success"):
            st.session_state.paid = True
            st.session_state.page = "app"
            st.rerun()

        if st.button("⬅️ Back"):
            st.session_state.page = "home"
            st.rerun()


# ======================
# INTRO ENGINE
# ======================
def get_intro(level, tone, product):

    if level == "Basic":
        return f"{product} is a simple and functional product."

    elif level == "Premium":
        if tone == "Luxury":
            return f"Experience premium quality with {product}."
        else:
            return f"{product} delivers strong performance and value."

    else:
        if tone == "Luxury":
            return f"Step into luxury with {product} — premium design and performance."
        else:
            return f"Don’t settle for average. {product} is built to dominate."


# ======================
# APP PAGE
# ======================
def app():

    if not st.session_state.paid:
        st.session_state.page = "payment"
        st.rerun()

    st.title("🚀 DescAI Pro Generator")

    st.success(f"Access granted - Plan: {st.session_state.plan}")

    st.divider()

    product = st.text_input("Product Name")
    brand = st.text_input("Brand")
    audience = st.text_input("Target Audience")
    price = st.text_input("Price")
    benefit = st.text_area("Main Benefit")

    feature1 = st.text_input("Feature 1")
    feature2 = st.text_input("Feature 2")
    feature3 = st.text_input("Feature 3")

    if st.button("🚀 GENERATE", use_container_width=True):

        if product and benefit:

            intro = get_intro(st.session_state.plan, tone, product)

            result = f"""
# {product}

🏷️ Brand: {brand}
💎 Plan: {st.session_state.plan}

{intro}

🎯 For: {audience}

🔥 Benefit: {benefit}

📌 Features:
• {feature1}
• {feature2}
• {feature3}

💰 Price: {price}
"""

            st.success("Generated successfully")
            st.text_area("Result", value=result, height=300)

        else:
            st.warning("Fill required fields")


# ======================
# ROUTER
# ======================
if st.session_state.page == "home":
    home()
elif st.session_state.page == "payment":
    payment()
else:
    app()
