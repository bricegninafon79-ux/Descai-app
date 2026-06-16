import streamlit as st
from datetime import datetime
import calendar

# ======================
# CONFIG
# ======================
st.title("🚀 DescAI Pro")

st.markdown("### AI-powered Shopify descriptions that convert buyers")
st.markdown("DescAI Pro generates optimized product descriptions designed to increase your sales and attract more customers.")

# ======================
# CSS DESIGN SAAS
# ======================
st.markdown("""
<style>

.stApp {
    background: #0b1220;
    color: white;
}

[data-testid="stSidebar"] {
    background: #111827;
}

h1, h2, h3 {
    color: white;
}

.stButton > button {
    background: linear-gradient(135deg, #3b82f6, #8b5cf6);
    color: white;
    border-radius: 12px;
    padding: 10px;
    font-weight: bold;
    border: none;
}

.plan-card {
    background: #1e293b;
    padding: 20px;
    border-radius: 20px;
    margin-bottom: 15px;
    border: 1px solid #334155;
}

.notification {
    background: linear-gradient(135deg, #ff4b4b, #ff9800);
    padding: 20px;
    border-radius: 18px;
    color: white;
    text-align: center;
    font-weight: bold;
    margin-bottom: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
}

.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)

# ======================
# SESSION STATE
# ======================
if "page" not in st.session_state:
    st.session_state.page = "home"

if "plan" not in st.session_state:
    st.session_state.plan = None

if "paid" not in st.session_state:
    st.session_state.paid = False


# ======================
# NOTIFICATION RENOUVELLEMENT (28+)
# ======================
today = datetime.now()

if today.day >= 28:
    last_day = calendar.monthrange(today.year, today.month)[1]
    days_left = last_day - today.day

    st.markdown(f"""
    <div class="notification">
        🔔 Votre abonnement DescAI Pro arrive à expiration.<br><br>
        Renouvelez-le avant la fin du mois pour continuer à accéder à toutes les fonctionnalités<br>
        et à des descriptions optimisées pour augmenter vos ventes.<br><br>
        ⏳ Il reste {days_left} jour(s).
    </div>
    """, unsafe_allow_html=True)


# ======================
# SIDEBAR
# ======================
st.sidebar.title("⚙️ Settings")

market = st.sidebar.selectbox(
    "Target Market",
    ["United States 🇺🇸", "France 🇫🇷", "Germany 🇩🇪", "Worldwide 🌍"]
)

language = st.sidebar.selectbox(
    "Language",
    ["English", "French", "Spanish", "German"]
)

tone = st.sidebar.selectbox(
    "Writing Tone",
    ["Professional", "Luxury", "Friendly", "Persuasive"]
)

st.sidebar.divider()

st.sidebar.write("Plan:", st.session_state.plan)
st.sidebar.write("Paid:", st.session_state.paid)


# ======================
# NAVIGATION
# ======================
def go(page):
    st.session_state.page = page
    st.rerun()


# ======================
# HOME
# ======================
def home():

    st.title("🚀 DescAI Pro")
    st.markdown("### Choose your plan")

    col1, col2, col3 = st.columns(3)

    def select_plan(plan):
        st.session_state.plan = plan
        go("payment")

    with col1:
        st.markdown("## 🟢 Basic")
        st.write("Simple descriptions")
        st.write("✔ Basic structure")
        st.write("💰 $9.99 / month")
        if st.button("Select Basic"):
            select_plan("Basic")

    with col2:
        st.markdown("## 🔵 Premium")
        st.write("High converting copy")
        st.write("✔ Marketing optimized")
        st.write("💰 $15.99 / month")
        if st.button("Select Premium"):
            select_plan("Premium")

    with col3:
        st.markdown("## 🟣 Ultra")
        st.write("Elite sales copywriting")
        st.write("✔ Maximum conversion")
        st.write("💰 $22.99 / month")
        if st.button("Select Ultra"):
            select_plan("Ultra")


# ======================
# PAYMENT
# ======================
def payment():

    st.title("💳 Payment")

    st.info(f"Selected Plan: {st.session_state.plan}")

    st.warning("Complete payment to continue")

    if st.button("💳 Simulate Payment"):

        st.session_state.paid = True

        st.success("""
🎉 Merci pour votre abonnement à DescAI Pro !

Nous sommes ravis de vous accueillir dans cette aventure.

Vous avez désormais accès à des descriptions optimisées pour améliorer vos conversions et développer votre boutique.

🚀 Bienvenue dans la communauté DescAI Pro !
""")

        st.balloons()

        if st.button("🚀 Start Now"):
            go("app")

    if st.button("⬅️ Back"):
        go("home")


# ======================
# APP GENERATOR
# ======================
def app():

    if not st.session_state.paid:
        go("payment")

    st.title("🚀 DescAI Generator")

    st.success(f"Active Plan: {st.session_state.plan}")

    product = st.text_input("Product Name")
    brand = st.text_input("Brand")
    audience = st.text_input("Audience")
    price = st.text_input("Price")
    benefit = st.text_area("Main Benefit")

    if st.button("Generate"):

        if product and benefit:

            intro = f"{product} is built for performance."

            result = f"""
# {product}

Brand: {brand}
Plan: {st.session_state.plan}

{intro}

Benefit: {benefit}

Price: {price}
"""

            st.text_area("Output", result, height=250)

        else:
            st.warning("Fill required fields")


# ======================
# MY ACCOUNT
# ======================
def account():

    st.title("👤 My Account")

    st.write("Plan:", st.session_state.plan)
    st.write("Paid:", st.session_state.paid)

    if today.day >= 28:
        st.warning("⚠️ Renewal period active - please renew your subscription")

    if st.button("🔙 Back"):
        go("app")


# ======================
# ROUTER
# ======================
if st.session_state.page == "home":
    home()
elif st.session_state.page == "payment":
    payment()
elif st.session_state.page == "app":
    app()
elif st.session_state.page == "account":
    account()


# ======================
# FOOTER
# ======================
st.markdown("""
<div class="footer">
Created by kēllønę 🔗💨
</div>
""", unsafe_allow_html=True)
