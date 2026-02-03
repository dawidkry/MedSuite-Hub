import streamlit as st

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="MedSuite Hub", page_icon="🏥", layout="wide")

# 2. CSS FOR BOTH HUB AND MODULES
st.markdown("""
    <style>
    /* Hide all Streamlit developer clutter */
    header, footer, .stDeployButton, [data-testid="stToolbar"], [data-testid="stStatusWidget"] {
        display: none !important;
        visibility: hidden;
    }
    
    /* Dark Mode Theme */
    .stApp {background-color:#0E1117; color:white;}
    
    /* Hub Button Styling */
    .stButton button {
        background-color: #161B22 !important;
        border: 2px solid #30363D !important;
        border-radius: 20px !important;
        padding: 30px 20px !important;
        width: 100% !important;
        color: white !important;
        font-size: 22px !important;
        font-weight: 700 !important;
        transition: 0.3s !important;
    }
    .stButton button:hover {
        border-color: #58a6ff !important;
        background-color: #1C2128 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. NAVIGATION LOGIC (State Management)
if 'page' not in st.session_state:
    st.session_state.page = 'hub'

def go_to_refeeding():
    st.session_state.page = 'refeeding'

def go_to_hub():
    st.session_state.page = 'hub'

# --- PAGE 1: THE HUB ---
if st.session_state.page == 'hub':
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        st.title("🏥 MedSuite")
        st.write("Clinical Decision Support Ecosystem")
        st.divider()

        # External Links (Keep these as link buttons)
        st.link_button("🧠 NIHSS Stroke Scale", "https://nihss-stroke-severity-scoring.streamlit.app", use_container_width=True)
        st.write("")
        st.link_button("❤️ CHADS-BLED Benefit Calculator", "https://chads-bled-web.streamlit.app", use_container_width=True)
        st.write("")

        # Internal Link (This opens the code below)
        st.button("🧪 Adult Refeeding Syndrome", on_click=go_to_refeeding)
        
        st.divider()
        st.caption("⚠️ For clinical educational use only.")

# --- PAGE 2: REFEEDING MODULE ---
elif st.session_state.page == 'refeeding':
    # Back Button
    if st.button("⬅️ Back to MedSuite Hub"):
        go_to_hub()
        st.rerun()

    # Integrated Refeeding Tool
    side_col, main_col = st.columns([1, 4])

    with side_col:
        st.subheader("📊 Reference Ranges")
        st.info("**K+:** 3.5–5.5\n\n**PO4:** 0.8–1.5\n\n**Mg:** 0.7–1.0\n\n**Ca:** 2.2–2.6\n\n**Na+:** 135–145")
        st.divider()
        st.caption("Taunton & Somerset NHS Trust")

    with main_col:
        st.title("Adult Refeeding Syndrome CDS")
        
        # Step 1: Risk
        st.header("Step 1: Risk Assessment")
        r_col1, r_col2 = st.columns(2)
        with r_col1:
            r1 = st.checkbox("BMI < 16 kg/m²")
            r2 = st.checkbox("Unintentional weight loss > 15%")
            r3 = st.checkbox("Little/no nutrition > 10 days")
            r4 = st.checkbox("Low baseline K+, PO4, or Mg")
        with r_col2:
            ex1 = st.checkbox("BMI < 14 kg/m²")
            ex2 = st.checkbox("Little/no nutrition > 15 days")

        # Risk Logic
        risk = "At Risk"
        if ex1 or ex2: risk = "Extremely High Risk"
        elif r1 or r2 or r3 or r4: risk = "High Risk"
        st.warning(f"Category: {risk}")

        # Step 2: Feed
        st.header("Step 2: Initial Management")
        if risk == "Extremely High Risk":
            st.error("Feed: 5 kcal/kg/day. Increase to full by Day 7.")
        elif risk == "High Risk":
            st.warning("Feed: 10 kcal/kg/day. Increase to full by Day 4-7.")

        with st.expander("💊 Vitamin Prophylaxis", expanded=True):
            st.write("Thiamine 50mg QDS | Vit B Co Strong 2 tabs TDS | Forceval 1 cap OD")

        # Step 3: Electrolytes & PN Toggle
        st.header("Step 3: Monitoring")
        m_col1, m_col2 = st.columns([2, 1])
        with m_col2:
            is_pn = st.toggle("Patient is on Parenteral Nutrition?")
            if is_pn: st.warning("⚠️ Glucose: Monitor 6-hourly (QDS)")
            else: st.info("ℹ️ Glucose: Monitor Twice Daily (BD)")
