
import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="Green Impact", layout="wide")

# Sample data
account_balance = 12578.45
savings_goal = 15000
interest_rate = 3.5
co2_saved = 487
trees_planted = 32
water_saved = 14752
renewable_energy = 658

# Recent transactions
transactions = [
    {"Date": "Apr 7", "Description": "Deposit", "Amount": 500, "Category": "Income"},
    {"Date": "Apr 5", "Description": "Solar Panel Project", "Amount": -200, "Category": "Investment"},
    {"Date": "Apr 2", "Description": "Interest Payment", "Amount": 36.45, "Category": "Interest"},
    {"Date": "Mar 28", "Description": "Reforestation Fund", "Amount": -150, "Category": "Investment"}
]
transactions_df = pd.DataFrame(transactions)

# Sidebar Navigation
tab = st.sidebar.radio("Navigate", ["Home", "Impact", "Invest", "Account"])

st.title("🌱 Green Impact")

if tab == "Home":
    st.header("💰 Account Summary")
    st.metric("Savings Balance", f"${account_balance:,.2f}")
    st.progress(account_balance / savings_goal)
    st.write(f"**Goal:** ${savings_goal:,.2f}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Interest Rate", f"{interest_rate}%")
    col2.metric("YTD Earnings", "$328.45")
    col3.metric("APY", "3.6%")

    st.divider()
    st.header("🌍 Environmental Impact")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Trees Planted", trees_planted)
    col2.metric("Water Saved (L)", f"{water_saved:,}")
    col3.metric("Renewable Energy (kWh)", renewable_energy)
    col4.metric("CO₂ Reduced (kg)", co2_saved)

    st.divider()
    st.header("📄 Recent Transactions")
    st.dataframe(transactions_df, use_container_width=True)

    st.divider()
    st.header("🚀 Active Impact Projects")
    st.write("**Solar Farm Initiative**")
    st.progress(0.60)
    st.write("Funding solar panel installations in rural communities. ($45,342 of $75,000)")

    st.write("**Amazon Reforestation**")
    st.progress(0.85)
    st.write("Planting native trees in deforested areas. ($128,450 of $150,000)")

elif tab == "Impact":
    st.header("📊 Impact Dashboard")
    st.info("Detailed environmental impact metrics will be available soon.")

elif tab == "Invest":
    st.header("💸 Investment Options")
    st.info("Green investment opportunities and tools coming soon.")

elif tab == "Account":
    st.header("👤 Account Settings")
    st.info("Manage your profile and preferences.")
