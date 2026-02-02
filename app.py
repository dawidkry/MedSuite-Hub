import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="MedSuite Hub", page_icon="🏥", layout="centered")

# 2. Hide Streamlit Branding
st.markdown("""
    <style>
    header, footer, .stDeployButton, [data-testid="stToolbar"] {display:none !important;}
    .stApp {background-color:#0E1117; color:white;}
    /* Make the native buttons bigger and centered */
    .stButton button {
        height: 100px;
        font-size: 20px !important;
        border-radius: 15px;
        background-color: #161B22;
        border: 2px solid #30363D;
        color: #58a6ff;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏥 MedSuite")
st.write("Clinical Decision Support")
st.divider()

# 3. The Functional Buttons
st.link_button("🧠 Launch NIHSS Stroke Scale", "https://nihss-stroke-severity-scoring.streamlit.app", use_container_width=True)

st.write("") # Spacing

st.link_button("🫀 Launch Cardio Risk (CHADS/BLED)", "https://your-cardio-app.streamlit.app", use_container_width=True)

st.divider()
st.caption("⚠️ Clinical educational use only.")
