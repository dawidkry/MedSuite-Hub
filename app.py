import streamlit as st

# 1. Config
st.set_page_config(page_title="MedSuite Hub", page_icon="🏥", layout="centered")

# 2. Force the "Card" style onto the Native Buttons
st.markdown("""
    <style>
    header, footer, .stDeployButton, [data-testid="stToolbar"] {display:none !important;}
    .stApp {background-color:#0E1117; color:white; font-family:sans-serif;}
    
    /* This targets the actual Streamlit Link Button and makes it look like your card */
    .stLinkButton a {
        background-color: #161B22 !important;
        border: 2px solid #30363D !important;
        border-radius: 20px !important;
        padding: 30px !important;
        height: auto !important;
        text-align: center !important;
        display: block !important;
        transition: 0.3s !important;
    }
    
    .stLinkButton a:hover {
        border-color: #58a6ff !important;
        background-color: #1C2128 !important;
    }

    /* Adjusting the text inside the button to match your h2/p style */
    .stLinkButton div p {
        font-size: 24px !important;
        font-weight: bold !important;
        margin: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header
st.title("🏥 MedSuite")
st.write("Clinical Decision Support Ecosystem")
st.divider()

# 4. The Buttons (Functionally identical to cards now)
st.link_button("🧠 NIHSS\n\nStroke Severity Scoring", 
               "https://nihss-stroke-severity-scoring.streamlit.app", 
               use_container_width=True)

st.write("") # Spacer

st.link_button("🫀 Cardio Risk\n\nCHA₂DS₂-VASc & HAS-BLED", 
               "https://chads-bled-web.streamlit.app", 
               use_container_width=True)

# 5. Disclaimer
st.divider()
st.caption("⚠️ For clinical educational use only. Verify all scores with institutional protocols.")
