import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="MedSuite Hub", page_icon="🏥", layout="centered")

# 2. Clean UI Styling (Hiding Streamlit junk)
st.markdown("""
    <style>
    header, footer, .stDeployButton, [data-testid="stToolbar"] {display:none !important;}
    .stApp {background-color:#0E1117; color:white; font-family:sans-serif;}
    
    /* Button Styling */
    .med-card {
        background-color: #161B22;
        border: 2px solid #30363D;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        margin-bottom: 15px;
        transition: 0.3s;
        cursor: pointer;
    }
    .med-card:hover {
        border-color: #58a6ff;
        background-color: #1C2128;
    }
    a {text-decoration: none !important;}
    </style>
    """, unsafe_allow_html=True)

# 3. Header
st.title("🏥 MedSuite")
st.write("Clinical Decision Support Ecosystem")
st.divider()

# 4. The Hub Grid
# Module 1: NIHSS
st.markdown(f"""
    <a href="https://nihss-stroke-severity-scoring.streamlit.app" target="_top">
        <div class="med-card">
            <h2 style="margin:0; color:#58a6ff;">🧠 NIHSS</h2>
            <p style="color:#8b949e; margin:10px 0 0 0;">Stroke Severity Scoring & Assessment</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

# Module 2: Cardio
st.markdown(f"""
    <a href="https://chads-bled-web.streamlit.app" target="_top">
        <div class="med-card">
            <h2 style="margin:0; color:#3fb950;">🫀 Cardio Risk</h2>
            <p style="color:#8b949e; margin:10px 0 0 0;">CHA₂DS₂-VASc & HAS-BLED Calculators</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

# 5. Footer Disclaimer
st.caption("⚠️ For clinical educational use only. Verify all scores with institutional protocols.")
