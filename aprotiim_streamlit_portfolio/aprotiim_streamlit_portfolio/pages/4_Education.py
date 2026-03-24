import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Education | Aprotiim Joardar", page_icon="🎓", layout="wide")
ROOT = Path(__file__).resolve().parents[1]
css = (ROOT / "assets" / "styles.css").read_text(encoding="utf-8")
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

st.title("Education")

left, right = st.columns([1.3, 1], gap="large")

with left:
    st.markdown(
        """
        <div class='section-card'>
            <h3>University of Florida</h3>
            <p><strong>M.S. in Information Systems & Operations Management</strong><br/>Data Science Concentration</p>
            <p><strong>Period:</strong> August 2023 – May 2025</p>
            <p><strong>GPA:</strong> 3.91</p>
            <p><strong>Relevant coursework:</strong> Machine Learning, Causal Inference, Statistics, Database Design</p>
            <p><strong>Honors:</strong> Exxon Mobil Scholarship, 3-time Director’s Choice Academic Excellence award</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='section-card'>
            <h3>How my education shows up in my work</h3>
            <ul>
                <li>Stronger grounding in statistical reasoning and model validation</li>
                <li>More rigorous approach to forecasting and ML experimentation</li>
                <li>Better ability to connect business decisions with quantitative evidence</li>
                <li>Confidence working across both traditional ML and modern AI systems</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        """
        <div class='info-card'>
            <h4>Academic focus areas</h4>
            <p>Machine Learning</p>
            <p>Statistical Modelling</p>
            <p>Forecasting</p>
            <p>Database Design</p>
            <p>Causal Inference</p>
            <p>Applied Data Science</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='info-card'>
            <h4>Why this matters</h4>
            <p>
            Recruiters often see either strong academics without real engineering depth, or strong engineering without recent quantitative training.
            My profile combines both.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
