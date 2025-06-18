import streamlit as st



st.set_page_config(page_title='BANK APP', layout='wide')



st.markdown("<h1 style='text-align: center; color: #1f4e79;'>Welcome to Vesting Finance</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Finance Power At your Finger Tips</h4>", unsafe_allow_html=True)


# st.image("your_logo.png", width=100)



st.markdown("---")


with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### 👋 Hello, Daniella West!")
        st.write("Here’s your personalized dashboard. Manage your account and view key banking features.")
    with col2:
        st.metric("Account Balance", "₦220,400", "₦12500 today")

st.markdown("---")

st.markdown("<h3 style='text-align: center;'>Banking Features</h3>", unsafe_allow_html=True)
fcol1, fcol2, fcol3 = st.columns(3)

with fcol1:
    st.markdown("### 📲 Mobile Banking")
    st.write("24/7 access to your funds and transactions.")

with fcol2:
    st.markdown("### 🔐 End-to-End Security")
    st.write("Industry-grade encryption protects your assets.")

with fcol3:
    st.markdown("### 💸 Instant Transfers")
    st.write("Send and receive money in real time.")

st.markdown("---")


st.markdown("<h3 style='text-align: center;'>Quick Actions</h3>", unsafe_allow_html=True)
demo_col1, demo_col2 = st.columns([1, 1])

with demo_col1:
    st.markdown("#### 💰 Check Balance")
    account = st.selectbox("Choose Account", ["Savings", "Current"], index=0)
    if st.button("Get Balance"):
        balances = { "Savings": "₦50,000", "Current": "₦200,000"}
        st.success(f"{account} Balance: {balances[account]}")

with demo_col2:
    st.markdown("#### 🔁 Make a Transfer")
    recipient = st.text_input("Recipient Name")
    amount = st.number_input("Amount (₦)", min_value=1.0, step=10.0)

    if st.button("Send Money"):
        if recipient and amount:
            st.success(f"✅ Transferred ₦{amount} to {recipient}")
        else:
            st.warning("Please fill in both recipient and amount.")

st.markdown("---")

st.markdown("""
    <div style='text-align: center; color: gray; font-size: small;'>
        © 2025 Vesting Finance. All rights reserved. | <a href='#'>Privacy Policy</a> | <a href='#'>Terms of Service</a><br>
        📧 support@vestfinanance.com | 📍 Abuja, Nigeria
    </div>
""", unsafe_allow_html=True)