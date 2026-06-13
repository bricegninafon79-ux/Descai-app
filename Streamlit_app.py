```python
‎import streamlit as st
‎
‎st.set_page_config(page_title="DescAI - Generator", page_icon="🔗", layout="centered")
‎
‎st.title("🔗 DescAI")
‎st.markdown("**Generate Shopify descriptions that sell in 3 seconds**")
‎st.divider()
‎
‎col1, col2 = st.columns(2)
‎with col1:
‎    product = st.text_input("Product name:", placeholder="Ex: Wireless Headphones, Nike Shoes")
‎with col2:
‎    price = st.text_input("Price:", placeholder="Ex: $29.99")
‎
‎benefit = st.text_area("Main benefit:", placeholder="Ex: Noise canceling, All-day comfort")
‎
‎if st.button("🚀 GENERATE DESCRIPTION - $9.99", type="primary", use_container_width=True):
‎    if product and benefit:
‎        st.success("### ✅ Shopify Description Ready to Copy:")
‎        description = f"""**{product}** - {benefit}.
‎
‎Premium quality guaranteed. Durable materials tested.
‎Fast shipping across the USA. 30-day money-back guarantee.
‎Secure payment at checkout.
‎
‎Price: {price if price else 'Contact us'}
‎Order now and upgrade your lifestyle today!"""
‎        
‎        st.text_area("Copy this to Shopify:", description, height=150)
‎        st.info("💰 PRO Version with ChatGPT AI + Stripe Payment = $9.99 per description. Contact for activation.")
‎    else:
‎        st.error("⚠️ Fill 'Product name' + 'Main benefit' Boss")
‎
‎st.divider()
‎st.caption("DescAI V1 - Built by kēllønę 🔗 | Targeting USA Market")
‎```
