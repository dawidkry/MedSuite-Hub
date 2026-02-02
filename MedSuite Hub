import streamlit as st

# 1. Config & Styling
st.set_page_config(page_title="MedSuite Hub", layout="centered")

st.markdown("<style>"
"header, footer {visibility: hidden;}"
".stApp {background-color:#0E1117;color:white;font-family:sans-serif;}"
"</style>", unsafe_allow_html=True)

# 2. Header
st.title("🏥 MedSuite")
st.caption("Clinical Decision Support Tools")
st.divider()

# 3. The Grid
# We'll use Streamlit's native columns for the hub
col1, col2 = st.columns(2)

with col1:
    st.info("### Stroke\n**NIHSS** Score")
    # Link to your NIHSS app URL
    st.link_button("Launch NIHSS", "https://your-nihss-url.streamlit.app", use_container_width=True)

with col2:
    st.success("### Cardio\n**CHA₂DS₂-VASc**")
    # Link to your Cardio app URL
    st.link_button("Launch CHADS", "https://your-chads-url.streamlit.app", use_container_width=True)

st.divider()

# 4. Future Expansion
with st.expander("Add New Tool"):
    st.write("Current tools: NIHSS, CHA2DS2, HAS-BLED.")
    st.caption("More modules can be linked here.")
