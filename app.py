import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="MedSuite Hub", page_icon="🏥", layout="centered")

# 2. Card Styling
st.markdown("""
    <style>
    header, footer, .stDeployButton, [data-testid="stToolbar"] {display:none !important;}
    .stApp {background-color:#0E1117; color:white; font-family:sans-serif;}
    
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
        margin-bottom: 15px !important;
    }
    
    .stLinkButton a:hover {
        border-color: #58a6ff !important;
        background-color: #1C2128 !important;
    }

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

# 4. The Modules (All external links)

# DVLA Guidelines (External Link)
st.link_button(" 🩺 AMU Ultrasound Locator", 
               "https://ultrasoundlocator.streamlit.app/", 
               use_container_width=True)

# NIHSS
st.link_button("🧠 NIHSS Stroke Scale", 
               "https://nihss-stroke-severity-scoring.streamlit.app", 
               use_container_width=True)

# CHADS-BLED
st.link_button("❤️ CHADS-BLED Benefit Calculator", 
               "https://chads-bled-web.streamlit.app", 
               use_container_width=True)

# CHADS-ORBIT Benefit Calculator (External Link)
st.link_button("❤️ CHADS-ORBIT Benefit Calculator", 
               "https://chads-orbit-benefit-calculator.streamlit.app", 
               use_container_width=True)

# REFEEDING SYNDROME (External Link)
st.link_button("🧪 Adult Refeeding Syndrome", 
               "https://adult-refeeding-syndrome.streamlit.app", 
               use_container_width=True)

# DVLA Guidelines (External Link)
st.link_button(" 🩺 DVLA Clinical Standards Dashboard", 
               "https://dvla-guidelines-search-tool.streamlit.app/", 
               use_container_width=True)


# 5. Footer
st.divider()
st.caption("⚠️ For clinical educational use only. v1.2")
