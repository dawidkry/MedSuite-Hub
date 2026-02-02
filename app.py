import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="MedSuite Hub", page_icon="🏥", layout="centered")

# 2. Card Styling (Applied to Native Link Buttons)
st.markdown("""
    <style>
    /* Hide Streamlit elements */
    header, footer, .stDeployButton, [data-testid="stToolbar"] {display:none !important;}
    .stApp {background-color:#0E1117; color:white; font-family:sans-serif;}
    
    /* Transforming the standard link button into your "Med-Card" */
    .stLinkButton a {
        background-color: #161B22 !important;
        border: 2px solid #30363D !important;
        border-radius: 20px !important;
        padding: 30px 20px !important;
        height: auto !important;
        text-align: center !important;
        display: block !important;
        transition: 0.3s !important;
        text-decoration: none !important;
    }
    
    .stLinkButton a:hover {
        border-color: #58a6ff !important;
        background-color: #1C2128 !important;
    }

    /* Styling the text inside the buttons */
    .stLinkButton div p {
        font-size: 22px !important;
        font-weight: 700 !important;
        margin: 0 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header
st.title("🏥 MedSuite")
st.write("Clinical Decision Support Ecosystem")
st.divider()

# 4. The Hub Grid

# Module 1: NIHSS
st.link_button("🧠 NIHSS Stroke Scale", 
               "https://nihss-stroke-severity-scoring.streamlit.app", 
               use_container_width=True)

st.write("") # Space between cards

# Module 2: CHADS-BLED (Updated Label)
st.link_button("🫀 CHADS-BLED Benefit Calculator", 
               "https://chads-bled-web.streamlit.app", 
               use_container_width=True)

# 5. Footer Disclaimer
st.divider()
st.caption("⚠️ For clinical educational use only. Verify all scores with institutional protocols.")
