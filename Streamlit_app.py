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
# SESSION STATE
# ======================
if "page" not in st.session_state:
    st.session_state.page = "home"

if "plan" not in st.session_state:
    st.session_state.plan = None

if "paid" not in st.session_state:
    st.session_state.paid = False


# ======================
# SIDEBAR GLOBAL (VISIBLE PARTOUT)
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

    st.title("🚀 DescAI Pro")
    st.markdown("### Choose your plan")

    col1, col2, col3 = st.columns(3)

    def select_plan(plan):
        st.session_state.plan = plan
        st.session_state.page = "payment"
        st.rerun()

    with col1:
        st.markdown("## 🟢 Basic")
        if st.button("Select Basic", use_container_width=True):
            select_plan("Basic")

    with col2:
        st.markdown("## 🔵 Premium")
        if st.button("Select Premium", use_container_width=True):
            select_plan("Premium")

    with col3:
        st.markdown("## 🟣 Ultra")
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
        return f"{product} is a simple product."

    elif level == "Premium":
        return f"{product} delivers strong performance and value."

    else:
        return f"{product} is built for maximum impact and results."


# ======================
# APP PAGE
# ======================
def app():

    # LOCK ACCESS
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
