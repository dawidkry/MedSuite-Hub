import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="MedSuite Hub", page_icon="🏥", layout="centered")

# 2. High-End Clinical UI Styling
st.markdown("""
    <style>
    /* Hide top and bottom branding */
    header, footer, .stDeployButton, [data-testid="stToolbar"] {display:none !important;}
    
    /* Background and Font */
    .stApp {background-color:#0E1117; color:white; font-family:sans-serif;}
    
    /* Style the buttons to look like clinical modules */
    div.stButton > button {
        height: 120px;
        border-radius: 20px;
        border: 2px solid #30363D;
        background-color: #161B22;
        color: white;
        font-size: 22px !important;
        font-weight: 700;
        transition: all 0.3s ease;
        margin-bottom: 10px;
    }
    
    /* Hover effects for a tactile feel */
    div.stButton > button:hover {
        border-color: #58a6ff;
        background-color: #1C2128;
        transform: translateY(-2px);
    }
    
    /* Color accents for the text within buttons */
    .blue-text { color: #58a6ff; }
    .green-text { color: #3fb950; }
    </style>
    """, unsafe_allow_html=True)

# 3. Branding
st.title("🏥 MedSuite")
st.markdown("<p style='color:#8b949e;'>Clinical Decision Support Ecosystem</p>", unsafe_allow_html=True)
st.divider()

# 4. The Modules
# Module 1: Neurology
st.link_button("🧠 NIHSS Stroke Scale", 
               "https://nihss-stroke-severity-scoring.streamlit.app", 
               use_container_width=True)

st.write("") # Spacer

# Module 2: Cardiology
st.link_button("🫀 CHADS-BLED Benefit", 
               "https://chads-bled-web.streamlit.app", 
               use_container_width=True)

# 5. Bottom Navigation / Info
st.divider()
with st.expander("ℹ️ Suite Information"):
    st.write("""
    **MedSuite v1.0**
    - Private Clinical Tools
    - Optimized for Mobile Use
    """)

st.caption("⚠️ For clinical educational use only. Verify with institutional protocols.")
