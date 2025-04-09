
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import base64
from io import BytesIO

# Set page config
st.set_page_config(
    page_title="Revolut Green Impact",
    page_icon="🌱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS to style the app like a mobile interface
st.markdown("""
<style>
    .main {
        max-width: 340px !important;
        padding: 1rem 1rem 1rem 1rem;
    }
    .stApp {
        background-color: #f0f2f5;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    .css-1544g2n {
        padding-top: 2rem;
    }
    .revolut-header {
        background-color: #000000;
        padding: 10px;
        border-radius: 10px 10px 0 0;
        display: flex;
        align-items: center;
        color: white;
    }
    .revolut-logo {
        background-color: white;
        border-radius: 50%;
        width: 24px;
        height: 24px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 10px;
        font-weight: bold;
        color: black;
    }
    .balance-card {
        background: linear-gradient(to right, #1e5631, #2e8b57);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    .impact-summary {
        background-color: white;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 15px;
        border: 1px solid #e6e6e6;
    }
    .tab-content {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #e6e6e6;
        margin-top: 15px;
    }
    .project-card {
        background-color: white;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 10px;
        border: 1px solid #e6e6e6;
    }
    .progress-container {
        width: 100%;
        background-color: #f0f0f0;
        border-radius: 5px;
        height: 6px;
        margin-top: 5px;
    }
    .progress-bar {
        height: 6px;
        border-radius: 5px;
        background-color: #2e8b57;
    }
    .metric-box {
        background-color: #f8f9fa;
        padding: 8px;
        border-radius: 5px;
        margin: 5px 0;
    }
    .invest-button {
        background-color: #000000;
        color: white;
        border: none;
        padding: 5px 10px;
        border-radius: 15px;
        cursor: pointer;
        font-size: 12px;
    }
    .bottom-nav {
        display: flex;
        justify-content: space-around;
        background-color: white;
        padding: 10px 0;
        border-radius: 0 0 10px 10px;
        border-top: 1px solid #e6e6e6;
        position: sticky;
        bottom: 0;
    }
    .nav-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        font-size: 12px;
        color: #666;
    }
    .nav-item.active {
        color: #2e8b57;
    }
    h1, h2, h3, h4, h5, h6 {
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 10px;
    }
    p {
        font-size: 12px;
        margin: 0;
    }
    .small-text {
        font-size: 11px;
        color: #666;
    }
    .flex-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .impact-metrics {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 8px;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Create a function to generate a circular progress chart
def create_donut_chart(percentage):
    fig, ax = plt.subplots(figsize=(2, 2))
    ax.pie([percentage, 100-percentage], colors=['#2e8b57', '#f0f0f0'], startangle=90, wedgeprops=dict(width=0.3))
    circle = plt.Circle((0, 0), 0.35, fc='white')
    ax.add_patch(circle)
    ax.axis('equal')
    plt.tight_layout()
    plt.close()
    buffer = BytesIO()
    fig.savefig(buffer, format='png', transparent=True)
    buffer.seek(0)
    image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return f"data:image/png;base64,{image_data}"

# Sample data
projects = [
    {"name": "Solar Farm - Scotland", "amount": "£850", "funding": 65, "return": "+2.8% YTD"},
    {"name": "Wind Energy - Wales", "amount": "£600", "funding": 42, "return": "+3.5% YTD"}
]

new_opportunities = [
    {"name": "Ocean Cleanup", "impact": "-8 tons plastic/year"},
    {"name": "Reforestation", "impact": "+5000 trees"}
]

impact_metrics = {
    "CO2 Reduced": "120kg total",
    "Trees Planted": "24 trees",
    "Clean Energy": "450kWh",
    "Plastic Removed": "5kg"
}

community_impact = [
    "120 families access clean energy",
    "Provide clean water to 30 households",
    "Support 3 local green businesses"
]

def mobile_frame():
    st.markdown("""
    <div class="revolut-header">
        <div class="revolut-logo">R</div>
        <span>Green Impact</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="balance-card">
        <p class="small-text">Available Balance</p>
        <h1 style="font-size: 20px; margin: 5px 0;">£2,450.00</h1>
        <div class="flex-container">
            <p class="small-text">+£15.60 this month</p>
            <span style="background-color: rgba(255,255,255,0.2); padding: 2px 8px; border-radius: 10px; font-size: 11px;">3.2% APY</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="impact-summary">
        <p style="font-weight: 500; margin-bottom: 8px;">Your Environmental Impact</p>
        <div style="display: flex; justify-content: space-between;">
            <div style="display: flex; align-items: center;">
                <div style="background-color: #e6f4ea; padding: 4px; border-radius: 50%; margin-right: 5px;">💧</div>
                <span style="font-size: 11px;">450L Water</span>
            </div>
            <div style="display: flex; align-items: center;">
                <div style="background-color: #e6f4ea; padding: 4px; border-radius: 50%; margin-right: 5px;">🌬️</div>
                <span style="font-size: 11px;">23kg CO2</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

tabs = ["Projects", "Impact"]
selected_tab = st.radio("", tabs, horizontal=True, label_visibility="collapsed")

mobile_frame()

if selected_tab == "Projects":
    st.markdown("""
    <div class="tab-content">
        <div class="flex-container">
            <p style="font-weight: 500;">Your Investments</p>
            <span class="small-text" style="color: #2e8b57;">3 projects</span>
        </div>
    """, unsafe_allow_html=True)

    for project in projects:
        st.markdown(f"""
        <div class="project-card">
            <div class="flex-container">
                <p style="font-weight: 500;">{project['name']}</p>
                <span style="color: #2e8b57; font-size: 12px;">{project['amount']}</span>
            </div>
            <div class="flex-container">
                <span class="small-text">Funding: {project['funding']}%</span>
                <span class="small-text">{project['return']}</span>
            </div>
            <div class="progress-container">
                <div class="progress-bar" style="width: {project['funding']}%;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-top: 15px;" class="flex-container">
        <p style="font-weight: 500;">New Opportunities</p>
        <span class="small-text" style="color: #2e8b57;">ESG Score: A+</span>
    </div>
    """, unsafe_allow_html=True)

    for opportunity in new_opportunities:
        st.markdown(f"""
        <div class="project-card">
            <div class="flex-container">
                <div>
                    <p style="font-weight: 500;">{opportunity['name']}</p>
                    <span class="small-text">{opportunity['impact']}</span>
                </div>
                <button class="invest-button">Invest</button>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

elif selected_tab == "Impact":
    st.markdown("""
    <div class="tab-content">
        <div class="flex-container">
            <p style="font-weight: 500;">Impact Summary</p>
            <span style="color: #2e8b57;">📊</span>
        </div>
    """, unsafe_allow_html=True)

    donut_chart = create_donut_chart(75)
    st.markdown(f"""
    <div style="display: flex; justify-content: center; margin: 15px 0;">
        <img src="{donut_chart}" width="120">
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="impact-metrics">', unsafe_allow_html=True)
    for metric, value in impact_metrics.items():
        st.markdown(f"""
        <div class="metric-box">
            <span class="small-text">{metric}</span>
            <p style="font-weight: 500;">{value}</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-top: 15px;">
        <p style="font-weight: 500;">Community Impact</p>
        <p class="small-text" style="margin-bottom: 5px;">Your investments have helped:</p>
    """, unsafe_allow_html=True)

    for impact in community_impact:
        st.markdown(f"""
        <p class="small-text" style="margin-left: 10px;">• {impact}</p>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
<div class="bottom-nav">
    <div class="nav-item">
        📊
        <span>Home</span>
    </div>
    <div class="nav-item active">
        🌱
        <span>Green</span>
    </div>
    <div class="nav-item">
        📈
        <span>Stats</span>
    </div>
</div>
""", unsafe_allow_html=True)
