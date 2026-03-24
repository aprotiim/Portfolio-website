import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Contact | Aprotiim Joardar", page_icon="📬", layout="wide")
ROOT = Path(__file__).resolve().parents[1]
css = (ROOT / "assets" / "styles.css").read_text(encoding="utf-8")
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

st.title("Contact")

col1, col2 = st.columns([1.2, 1], gap="large")

with col1:
    st.markdown(
        """
        <div class='hero-card'>
            <div class='eyebrow'>Let's connect</div>
            <h2 class='hero-title'>I’m looking for opportunities where I can build high-impact AI and data products.</h2>
            <p class='hero-subtitle'>
            I’m especially interested in AI engineer, ML engineer, data scientist, and applied LLM roles where strong systems thinking and practical execution matter.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='section-card'>
            <h3>Best ways to reach me</h3>
            <p><strong>Email:</strong> <a href='mailto:aprotiim@gmail.com'>aprotiim@gmail.com</a></p>
            <p><strong>Phone:</strong> 352-709-5368</p>
            <p><strong>GitHub:</strong> <a href='https://github.com/aprotiim' target='_blank'>github.com/aprotiim</a></p>
            <p><strong>LinkedIn:</strong> Add your LinkedIn URL here</p>
            <p><strong>Location:</strong> Gainesville, Florida</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class='info-card'>
            <h4>Recruiter quick note</h4>
            <p>
            This portfolio is intentionally built to make my story easy to remember:
            enterprise data foundation, graduate-level ML depth, and a modern AI portfolio aligned with current hiring demand.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("contact_form"):
        st.text_input("Name")
        st.text_input("Email")
        st.text_area("Message", height=180)
        st.form_submit_button("Send")

st.info("Tip: replace the LinkedIn placeholder with your live profile URL before deploying.")
