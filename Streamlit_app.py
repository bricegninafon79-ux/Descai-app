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
# SIDEBAR GLOBAL
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
# HOME PAGE (PLANS WITH FULL DESCRIPTION)
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
        st.markdown("Simple & fast product descriptions")
        st.markdown("✔ Clean structure")
        st.markdown("✔ Good for testing products")
        st.markdown("❌ No marketing optimization")
        st.markdown("💰 Free")
        if st.button("Select Basic", use_container_width=True):
            select_plan("Basic")

    with col2:
        st.markdown("## 🔵 Premium")
        st.markdown("High converting Shopify descriptions")
        st.markdown("✔ Persuasive copywriting")
        st.markdown("✔ Marketing optimized")
        st.markdown("✔ Better conversion rate")
        st.markdown("💰 $9.99 / month")
        if st.button("Select Premium", use_container_width=True):
            select_plan("Premium")

    with col3:
        st.markdown("## 🟣 Ultra")
        st.markdown("Elite sales copywriting engine")
        st.markdown("✔ Emotional marketing")
        st.markdown("✔ Scarcity & urgency")
        st.markdown("✔ Maximum conversion focus")
        st.markdown("💰 $19.99 / month")
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
