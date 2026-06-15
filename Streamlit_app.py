import streamlit as st

# ======================
# CONFIG
# ======================
st.set_page_config(
    page_title="DescAI Pro",
    page_icon="🚀",
    layout="wide"
)

# ======================
# CSS SaaS DESIGN
# ======================
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
    background: linear-gradient(90deg, #7C3AED, #3B82F6);
    color: white;
}

.stTextInput input,
.stTextArea textarea {
    border-radius: 12px !important;
    background-color: #111;
    color: white;
}

/* BADGES */
.badges {
    text-align: center;
    margin-bottom: 20px;
    color: #aaa;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='badges'>
⚡ No Signup &nbsp;&nbsp; 🚀 Instant Results &nbsp;&nbsp; 💰 SaaS Ready
</div>
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
st.sidebar.write(f"Plan: {st.session_state.plan}")
st.sidebar.write(f"Paid: {st.session_state.paid}")


# ======================
# HOME PAGE
# ======================
def home():

    st.markdown("<h1 style='text-align:center;'>Turn Features Into Money</h1>", unsafe_allow_html=True)

    st.markdown("<p style='text-align:center;color:gray;'>AI Product Descriptions in 6 Seconds</p>", unsafe_allow_html=True)

    st.markdown("### Choose your plan")

    col1, col2, col3 = st.columns(3)

    def select_plan(plan):
        st.session_state.plan = plan
        st.session_state.page = "payment"
        st.rerun()

    with col1:
        st.markdown("## 🟢 Basic")
        st.markdown("💰 $9.99 / month")
        if st.button("Select Basic", use_container_width=True):
            select_plan("Basic")

    with col2:
        st.markdown("## 🔵 Premium")
        st.markdown("💰 $15.99 / month")
        if st.button("Select Premium", use_container_width=True):
            select_plan("Premium")

    with col3:
        st.markdown("## 🟣 Ultra")
        st.markdown("💰 $22.99 / month")
        if st.button("Select Ultra", use_container_width=True):
            select_plan("Ultra")

    st.divider()
    st.caption("Built with passion by kēllønę 🔗💨")


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

    st.caption("DescAI Pro system by kēllønę 🔗💨")


# ======================
# INTRO ENGINE
# ======================
def get_intro(level, tone, product):

    if level == "Basic":
        return f"{product} is a simple and functional product."

    elif level == "Premium":
        if tone == "Luxury":
            return f"Experience premium quality with {product}."
        elif tone == "Persuasive":
            return f"{product} is designed to boost your results instantly."
        else:
            return f"{product} delivers strong performance and value."

    else:
        if tone == "Luxury":
            return f"Step into luxury with {product} — premium design and performance."
        elif tone == "Persuasive":
            return f"Stop losing sales. {product} is built to dominate."
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
    st.caption("Created by kēllønę 🔗💨")

    st.success(f"Access granted — {st.session_state.plan} Plan")

    st.divider()

    product = st.text_input("Product Name")
    brand = st.text_input("Brand")
    audience = st.text_input("Target Audience")
    price = st.text_input("Price")
    benefit = st.text_area("Main Benefit")

    feature1 = st.text_input("Feature 1")
    feature2 = st.text_input("Feature 2")
    feature3 = st.text_input("Feature 3")

    if st.button("🚀 GENERATE SALES-READY COPY", use_container_width=True):

        if product and benefit:

            intro = get_intro(st.session_state.plan, tone, product)

            with st.spinner("AI is crafting your description..."):

                result = f"""
# {product}

🏷️ Brand: {brand}
💎 Plan: {st.session_state.plan}

{intro}

🎯 Target: {audience}

🔥 Main Benefit:
{benefit}

📌 Features:
• {feature1}
• {feature2}
• {feature3}

💰 Price: {price if price else "Not set"}
"""

            st.success("Generated successfully")

            st.text_area("📋 Your Shopify Description", value=result, height=350)

            st.info(f"🔥 Plan: {st.session_state.plan} | Tone: {tone}")

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

st.divider()
st.caption("DescAI Pro © 2026 | Built by kēllønę 🔗💨 | SaaS AI Generator")
