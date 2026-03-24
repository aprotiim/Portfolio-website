import base64
from pathlib import Path

import streamlit as st

st.title("Work Experience")

# ── Logo loader ────────────────────────────────────────────────────────────────
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

_LOGO_KPMG = _img_tag("kpmg_logo.png")
_LOGO_UF   = _img_tag("uf_logo.png")

experiences = [
    {
        "role": "Data Scientist",
        "logo": _LOGO_UF,
        "company": "University of Florida",
        "location": "Gainesville, Florida",
        "type_tag": "Research",
        "period": "May 2025 – Present",
        "impact": [
            "Reduced quarterly forecast error by 18% using deep neural networks integrating structured financial and macroeconomic data.",
            "Designed neural network models with regularization, early stopping, and sliding-window validation to improve forecasting reliability.",
            "Engineered 25+ lag and rolling-window features while preserving fiscal continuity.",
            "Optimized HPC-based training workflows, reducing runtime by roughly 35%.",
            "Benchmarked MLP and LSTM architectures evaluated on RMSE and MAE metrics.",
        ],
    },
    {
        "role": "Senior Engineer – Data & Analytics",
        "logo": _LOGO_KPMG,
        "company": "KPMG",
        "location": "Bengaluru, India",
        "type_tag": None,
        "period": "Jul 2018 – Jul 2023",
        "impact": [
            "Designed and maintained ETL pipelines for financial and operational datasets (10M+ rows), ensuring timely ingestion, cleansing, and transformation for downstream analytics and reporting.",
            "Automated data workflows using SQL stored procedures, Python scripts, and Alteryx, reducing manual processing time by 30% across multiple client engagements.",
            "Developed scalable data pipelines for structured and unstructured data, integrating sources like Excel, Oracle, SQL Server, and APIs into centralized reporting systems.",
            "Implemented data validation and quality checks with custom SQL/Python routines, improving data accuracy and consistency by 25%.",
            "Optimized SQL queries and stored procedures, improving query performance by up to 40% on large client datasets.",
            "Collaborated with cross-functional teams to understand business requirements and translated them into scalable data engineering solutions for tax, audit, and advisory workflows.",
            "Deployed reporting dashboards (Power BI/Tableau) connected to optimized data pipelines, enabling faster insights and self-service analytics for client teams.",
            "Mentored junior analysts on best practices in SQL optimization, ETL pipeline design, and debugging, contributing to overall team efficiency.",
        ],
    },
]

for exp in experiences:
    bullets = "".join([f"<li>{item}</li>" for item in exp["impact"]])
    type_tag_html = (
        f"<span class='research-tag'>{exp['type_tag']}</span>"
        if exp["type_tag"] else ""
    )
    location = exp.get("location", "")
    st.markdown(
        f"""
        <div class='section-card'>
            <div style='display:flex;justify-content:space-between;align-items:center;gap:1rem;margin-bottom:0.8rem;'>
                <div style='display:flex;align-items:center;gap:1rem;'>
                    {exp["logo"]}
                    <div>
                        <div style='font-size:1.12rem;font-weight:700;letter-spacing:0.01em;
                                    color:#e5eefb;line-height:1.3;margin:0;padding:0;'>{exp["role"]}{type_tag_html}</div>
                        <div style='margin:0;padding:0;line-height:1.4;'>
                            <span style='font-size:0.9rem;font-weight:700;color:#94a9c9;'>{exp["company"]}</span>
                            <span style='color:rgba(148,169,201,0.35);margin:0 0.4rem;'>|</span>
                            <span style='font-size:0.82rem;font-style:italic;color:#6ee7f9;'>📍 {location}</span>
                        </div>
                    </div>
                </div>
                <div style='font-size:0.88rem;color:#94a9c9;white-space:nowrap;flex-shrink:0;'>{exp["period"]}</div>
            </div>
            <ul style='margin:0;padding-left:1.3rem;'>{bullets}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.subheader("How this experience translates to recruiter value")
col1, col2 = st.columns(2, gap="large")
with col1:
    st.markdown(
        """
        <div class='info-card'>
            <h4>For AI/ML engineering roles</h4>
            <p>
            I bring strong fundamentals in data preparation, evaluation design, experimentation, and system thinking — all of which are essential for taking AI systems from proof of concept to reliable application.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        """
        <div class='info-card'>
            <h4>For data science roles</h4>
            <p>
            My experience combines forecasting, feature engineering, statistical thinking, and large-scale business data work, which makes me comfortable operating from problem framing through measurable impact.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
