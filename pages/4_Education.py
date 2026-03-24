import base64
from pathlib import Path

import streamlit as st

st.title("Education")

_ASSETS = Path(__file__).resolve().parents[1] / "assets"

def _img_tag(filename, size=52):
    path = _ASSETS / filename
    if not path.exists():
        return ""
    b64 = base64.b64encode(path.read_bytes()).decode()
    ext = path.suffix.lstrip(".")
    mime = "svg+xml" if ext == "svg" else ext
    return (
        f"<img src='data:image/{mime};base64,{b64}' "
        f"style='width:{size}px;height:{size}px;object-fit:contain;"
        f"border-radius:10px;background:#fff;padding:4px;flex-shrink:0;'>"
    )

_LOGO_UF = _img_tag("uf_logo.png")

left, right = st.columns([1.3, 1], gap="large")

with left:
    st.markdown(
        f"""
        <div class='section-card'>
            <div class='experience-header-left' style='margin-bottom:0.85rem;'>
                {_LOGO_UF}
                <div>
                    <div style='font-size:1.12rem;font-weight:700;color:#e5eefb;line-height:1.3;margin:0;padding:0;'>University of Florida</div>
                    <div style='font-size:0.88rem;color:#94a9c9;margin:0;padding:0;line-height:1.4;'>Gainesville, Florida · Aug 2023 – May 2025</div>
                </div>
            </div>
            <p><strong>M.S. in Information Systems &amp; Operations Management</strong> — Data Science Concentration</p>
            <p><strong>GPA:</strong> 3.91 &nbsp;|&nbsp; <strong>Coursework:</strong> Machine Learning, Causal Inference, Statistics, Database Design</p>
            <p><strong>Honors:</strong> Exxon Mobil Scholarship · 3-time Director's Choice Academic Excellence Award</p>
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
            <p style='margin:0.5rem 0 0 0;line-height:2.2;'>
                <span style='display:inline-block;padding:0.22rem 0.72rem;border-radius:999px;background:rgba(167,139,250,0.18);border:1px solid rgba(167,139,250,0.32);color:#c4b5fd;font-size:0.78rem;font-weight:500;margin:2px 3px 2px 0;'>Machine Learning</span>
                <span style='display:inline-block;padding:0.22rem 0.72rem;border-radius:999px;background:rgba(167,139,250,0.18);border:1px solid rgba(167,139,250,0.32);color:#c4b5fd;font-size:0.78rem;font-weight:500;margin:2px 3px 2px 0;'>Statistical Modelling</span>
                <span style='display:inline-block;padding:0.22rem 0.72rem;border-radius:999px;background:rgba(167,139,250,0.18);border:1px solid rgba(167,139,250,0.32);color:#c4b5fd;font-size:0.78rem;font-weight:500;margin:2px 3px 2px 0;'>Forecasting</span>
                <span style='display:inline-block;padding:0.22rem 0.72rem;border-radius:999px;background:rgba(167,139,250,0.18);border:1px solid rgba(167,139,250,0.32);color:#c4b5fd;font-size:0.78rem;font-weight:500;margin:2px 3px 2px 0;'>Database Design</span>
                <span style='display:inline-block;padding:0.22rem 0.72rem;border-radius:999px;background:rgba(167,139,250,0.18);border:1px solid rgba(167,139,250,0.32);color:#c4b5fd;font-size:0.78rem;font-weight:500;margin:2px 3px 2px 0;'>Causal Inference</span>
                <span style='display:inline-block;padding:0.22rem 0.72rem;border-radius:999px;background:rgba(167,139,250,0.18);border:1px solid rgba(167,139,250,0.32);color:#c4b5fd;font-size:0.78rem;font-weight:500;margin:2px 3px 2px 0;'>Applied Data Science</span>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='info-card'>
            <h4>Why this matters to recruiters</h4>
            <p>
            Recruiters often see either strong academics without real engineering depth, or strong engineering without recent quantitative training.
            My profile combines both — enterprise-scale execution and rigorous academic grounding.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
