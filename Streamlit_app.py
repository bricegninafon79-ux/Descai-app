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

# ======================
# PAGE 1 - HOME (PLANS)
# ======================
def home():

    st.title("🚀 DescAI Pro")
    st.markdown("### Choose your plan to continue")
    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("## 🟢 Basic")
        st.markdown("Simple product descriptions")
        st.markdown("💰 Free")
        if st.button("Select Basic", use_container_width=True):
            st.session_state.plan = "Basic"
            st.session_state.page = "app"
            st.rerun()

    with col2:
        st.markdown("## 🔵 Premium")
        st.markdown("High converting descriptions")
        st.markdown("💰 $9.99")
        if st.button("Select Premium", use_container_width=True):
            st.session_state.plan = "Premium"
            st.session_state.page = "app"
            st.rerun()

    with col3:
        st.markdown("## 🟣 Ultra")
        st.markdown("Elite sales copywriting")
        st.markdown("💰 $19.99")
        if st.button("Select Ultra", use_container_width=True):
            st.session_state.plan = "Ultra"
            st.session_state.page = "app"
            st.rerun()


# ======================
# INTRO ENGINE
# ======================
def get_intro(level, tone, product):

    if level == "Basic":
        return f"{product} is a simple and functional product."

    elif level == "Premium":
        if tone == "Luxury":
            return f"Experience premium excellence with {product}."
        else:
            return f"{product} delivers strong performance and reliability."

    else:  # Ultra
        if tone == "Luxury":
            return f"Step into luxury with {product} — premium performance and design."
        else:
            return f"Don’t settle for average. {product} is built to dominate."


# ======================
# PAGE 2 - APP (GENERATOR)
# ======================
def app():

    st.title("🚀 DescAI Pro Generator")

    st.info(f"Selected Plan: {st.session_state.plan}")

    st.divider()

    # Sidebar
    st.sidebar.title("⚙️ Settings")

    market = st.sidebar.selectbox(
        "Target Market",
        [
            "United States 🇺🇸",
            "United Kingdom 🇬🇧",
            "Canada 🇨🇦",
            "France 🇫🇷",
            "Germany 🇩🇪",
            "Spain 🇪🇸",
            "Worldwide 🌍"
        ]
    )

    language = st.sidebar.selectbox(
        "Language",
        ["English", "French", "Spanish", "German"],
        index=0
    )

    tone = st.sidebar.selectbox(
        "Writing Tone",
        ["Professional", "Luxury", "Friendly", "Persuasive"]
    )

    # Inputs
    col1, col2 = st.columns(2)

    with col1:
        product = st.text_input("Product Name")
        brand = st.text_input("Brand")

    with col2:
        audience = st.text_input("Target Audience")
        price = st.text_input("Price")

    benefit = st.text_area("Main Benefit")

    feature1 = st.text_input("Feature 1")
    feature2 = st.text_input("Feature 2")
    feature3 = st.text_input("Feature 3")

    # Generate
    if st.button("🚀 GENERATE", use_container_width=True):

        if product and benefit:

            intro = get_intro(st.session_state.plan, tone, product)

            description = f"""
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

⚡ Limited stock
"""

            st.success("Generated successfully")
            st.text_area("Result", value=description, height=300)

        else:
            st.warning("Fill required fields")


# ======================
# ROUTER
# ======================
if st.session_state.page == "home":
    home()
else:
    app()
