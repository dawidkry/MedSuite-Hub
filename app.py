import streamlit as st

# 1. PAGE CONFIG (This must be the very first Streamlit command)
st.set_page_config(page_title="MedSuite Hub", page_icon="🏥", layout="wide")

# 2. SURGICAL CSS (Removes GitHub, Star, 3-dots, and Header)
st.markdown("""
    <style>
    header, footer, .stDeployButton, [data-testid="stToolbar"], [data-testid="stStatusWidget"] {
        display: none !important;
        visibility: hidden;
    }
    .stApp {background-color:#0E1117; color:white;}
    
    /* Hub Button Styling */
    .stButton button {
        background-color: #161B22 !important;
        border: 2px solid #30363D !important;
        border-radius: 20px !important;
        padding: 25px !important;
        width: 100% !important;
        color: white !important;
        font-size: 20px !important;
        font-weight: 700 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. NAVIGATION STATE
if 'page' not in st.session_state:
    st.session_state.page = 'hub'

# 4. THE HUB PAGE
if st.session_state.page == 'hub':
    st.title("🏥 MedSuite")
    st.write("Clinical Decision Support Ecosystem")
    st.divider()

    # Integrated Module Button
    if st.button("🧪 Adult Refeeding Syndrome"):
        st.session_state.page = 'refeeding'
        st.rerun()

    st.write("")
    
    # External Links
    st.link_button("🧠 NIHSS Stroke Scale", "https://nihss-stroke-severity-scoring.streamlit.app", use_container_width=True)
    st.link_button("❤️ CHADS-BLED Calculator", "https://chads-bled-web.streamlit.app", use_container_width=True)

# 5. THE REFEEDING MODULE (Integrated)
elif st.session_state.page == 'refeeding':
    if st.button("⬅️ Back to Hub"):
        st.session_state.page = 'hub'
        st.rerun()
    
    st.divider()
    
    # Static Sidebar Column
    side_col, main_col = st.columns([1, 4])
    
    with side_col:
        st.subheader("📊 Reference")
        st.info("**K+:** 3.5–5.5\n\n**PO4:** 0.8–1.5\n\n**Mg:** 0.7–1.0")
        st.caption("Taunton & Somerset NHS")

    with main_col:
        st.title("Refeeding Syndrome Tool")
        
        # Risk Checkboxes
        st.header("Step 1: Risk Assessment")
        c1, c2 = st.columns(2)
        with c1:
            r1 = st.checkbox("BMI < 16 kg/m²")
            r2 = st.checkbox("Weight loss > 15%")
        with c2:
            ex1 = st.checkbox("BMI < 14 kg/m²")
            ex2 = st.checkbox("No nutrition > 15 days")

        # Parenteral Nutrition Toggle (Full Name)
        st.divider()
        is_pn = st.toggle("Patient is on Parenteral Nutrition?")
        if is_pn:
            st.warning("⚠️ **Glucose:** Monitor 6-hourly (QDS)")
        else:
            st.info("ℹ️ **Glucose:** Monitor Twice Daily (BD)")
