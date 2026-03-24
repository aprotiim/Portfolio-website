import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Work Experience | Aprotiim Joardar", page_icon="💼", layout="wide")
ROOT = Path(__file__).resolve().parents[1]
css = (ROOT / "assets" / "styles.css").read_text(encoding="utf-8")
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

st.title("Work Experience")

experiences = [
    {
        "role": "Data Scientist (Research Assistant)",
        "company": "University of Florida",
        "period": "May 2025 – Present",
        "impact": [
            "Reduced quarterly forecast error by 18% using deep neural networks that integrated structured financial and macroeconomic data.",
            "Designed neural network models with regularization, early stopping, and sliding-window validation to improve forecasting reliability.",
            "Engineered 25+ lag and rolling-window features while preserving fiscal continuity.",
            "Optimized HPC-based training workflows, reducing runtime by roughly 35%.",
        ],
    },
    {
        "role": "Senior Data Engineer",
        "company": "KPMG",
        "period": "July 2020 – July 2023",
        "impact": [
            "Led development of enterprise analytics platforms supporting ML-driven audit analytics and anomaly detection.",
            "Designed PySpark pipelines over 20TB+ of ERP data across SAP, Oracle, and Workday ecosystems.",
            "Improved distributed pipeline performance by about 30% via partition tuning and query optimization.",
            "Served as a techno-functional lead for a team of 5 associates across analytics initiatives.",
        ],
    },
    {
        "role": "Data Engineer & Analytics Lead",
        "company": "KPMG",
        "period": "July 2018 – June 2020",
        "impact": [
            "Automated large-scale preprocessing workflows, reducing manual effort by around 30%.",
            "Translated 50+ business rules into KPI frameworks that supported predictive modeling use cases.",
            "Supported anomaly detection and financial risk analytics across 15+ audit engagements.",
            "Delivered scalable BI dashboards that improved stakeholder visibility into risk metrics.",
        ],
    },
]

for exp in experiences:
    bullets = "".join([f"<li>{item}</li>" for item in exp["impact"]])
    st.markdown(
        f"""
        <div class='section-card'>
            <div class='experience-header'>
                <div>
                    <h3>{exp['role']}</h3>
                    <div class='experience-company'>{exp['company']}</div>
                </div>
                <div class='experience-period'>{exp['period']}</div>
            </div>
            <ul>{bullets}</ul>
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
