import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
from PIL import Image
import base64

st.set_page_config(
    page_title='Green Impact Pro',
    page_icon='🌍',
    layout='centered',
    initial_sidebar_state='collapsed'
)

st.markdown("""
<style>
.main { max-width: 360px !important; padding: 1rem; }
.stApp { background-color: #f6f9f6; }
.header, .footer { background-color: #1e5631; color: white; padding: 12px; border-radius: 12px; text-align: center; }
.section { background-color: white; padding: 14px; border-radius: 12px; margin-bottom: 15px; border: 1px solid #d8e5da; }
.section h3 { font-size: 16px; margin-bottom: 8px; color: #2e8b57; }
.section p { font-size: 13px; margin: 4px 0; }
.impact-box { background-color: #f0f5f0; border-radius: 10px; padding: 8px; margin: 4px 0; font-size: 12px; }
.chart-center { display: flex; justify-content: center; margin: 10px 0; }
</style>
""", unsafe_allow_html=True)

def create_donut_chart(percentage):
    fig, ax = plt.subplots(figsize=(2, 2))
    ax.pie([percentage, 100 - percentage], colors=['#2e8b57', '#e0e0e0'], startangle=90, wedgeprops={'width': 0.3})
    centre_circle = plt.Circle((0, 0), 0.35, fc='white')
    ax.add_artist(centre_circle)
    ax.axis('equal')
    buffer = BytesIO()
    plt.savefig(buffer, format='png', transparent=True)
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()
    return f'data:image/png;base64,{image_base64}'

st.markdown('<div class="header"><h2>🌍 Green Impact Pro</h2><p>Invest. Impact. Inspire.</p></div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="section"><h3>👤 Your Profile</h3>', unsafe_allow_html=True)
    st.markdown('<p><strong>Name:</strong> Alex Taylor</p>', unsafe_allow_html=True)
    st.markdown('<p><strong>Eco Level:</strong> 🌿 Green Leader</p>', unsafe_allow_html=True)
    st.markdown('<p><strong>Joined:</strong> Jan 2024</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="section"><h3>💰 Balance & Growth</h3>', unsafe_allow_html=True)
    st.markdown('<p><strong>Current Balance:</strong> £3,210.45</p>', unsafe_allow_html=True)
    st.markdown('<p><strong>Growth:</strong> +£120.34 this month</p>', unsafe_allow_html=True)
    st.markdown('<p><strong>APY:</strong> 3.5%</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="section"><h3>🌱 Impact Summary</h3>', unsafe_allow_html=True)
    donut = create_donut_chart(82)
    st.markdown(f'<div class="chart-center"><img src="{donut}" width="120"></div>', unsafe_allow_html=True)
    st.markdown('<div class="impact-box">🌳 Trees Planted: 58</div>', unsafe_allow_html=True)
    st.markdown('<div class="impact-box">🔋 Clean Energy Generated: 890 kWh</div>', unsafe_allow_html=True)
    st.markdown('<div class="impact-box">💧 Water Saved: 1,200L</div>', unsafe_allow_html=True)
    st.markdown('<div class="impact-box">🏞️ Carbon Offset: 210kg CO2</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="section"><h3>📈 Projects Invested In</h3>', unsafe_allow_html=True)
    projects = [
        {'name': 'Reforest Africa', 'impact': 'Planted 200K trees', 'return': '+4.1%'},
        {'name': 'Solar Grid Kenya', 'impact': 'Powered 300 homes', 'return': '+3.8%'},
        {'name': 'Wind Hub Wales', 'impact': 'Reduced 500 tons CO2', 'return': '+3.2%'}
    ]
    for p in projects:
        st.markdown(f'''
            <div class="impact-box">
                <strong>{p['name']}</strong><br>
                🌿 {p['impact']}<br>
                📈 Return: {p['return']}
            </div>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="section"><h3>🤝 Community Impact</h3>', unsafe_allow_html=True)
    highlights = [
        '✔️ 75 local businesses supported',
        '✔️ 500 students reached with eco-education',
        '✔️ 10,000 kg plastic waste removed'
    ]
    st.markdown('<ul style="font-size: 13px;">', unsafe_allow_html=True)
    for h in highlights:
        st.markdown(f'<li>{h}</li>', unsafe_allow_html=True)
    st.markdown('</ul></div>', unsafe_allow_html=True)

st.markdown('<div class="footer">🌿 Thank you for supporting a greener future 🌿</div>', unsafe_allow_html=True)
