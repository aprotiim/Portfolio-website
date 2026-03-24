import streamlit as st
from pathlib import Path

st.set_page_config(page_title="About | Aprotiim Joardar", page_icon="👋", layout="wide")
ROOT = Path(__file__).resolve().parents[1]
css = (ROOT / "assets" / "styles.css").read_text(encoding="utf-8")
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

st.title("About")

left, right = st.columns([1.5, 1], gap="large")

with left:
    st.markdown(
        """
        <div class='section-card'>
            <h3>Who I am</h3>
            <p>
            I'm an AI/ML engineer and data scientist who enjoys building systems that are both technically strong and practically useful.
            My background combines enterprise data engineering, machine learning research, and hands-on GenAI development.
            </p>
            <p>
            Over time, my work has evolved from analytics pipelines and reporting systems to intelligent applications powered by
            RAG, agentic workflows, neural networks, and production APIs. What ties everything together is a consistent focus on
            solving real problems with thoughtful engineering.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='section-card'>
            <h3>What makes my profile different</h3>
            <ul>
                <li>I can move across the full AI lifecycle: data pipelines, feature engineering, modeling, evaluation, and application design.</li>
                <li>I bring enterprise discipline from KPMG and experimentation depth from graduate research.</li>
                <li>I care about robustness — not just demos. That means validation strategy, latency, system fallback logic, and monitoring mindset.</li>
                <li>I enjoy building portfolio projects that reflect modern hiring demand: agentic AI, RAG, deployed chatbots, forecasting, and recommenders.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        """
        <div class='info-card'>
            <h4>Core strengths</h4>
            <p><strong>AI & LLM Systems:</strong> RAG, Corrective RAG, LangChain, LangGraph, multi-agent workflows, vector databases</p>
            <p><strong>ML:</strong> regression, classification, deep learning, feature engineering, model evaluation, cross-validation</p>
            <p><strong>Data Engineering:</strong> PySpark, SQL, ETL/ELT, Azure Databricks, distributed computing, HPC</p>
            <p><strong>Deployment:</strong> FastAPI, Docker, CI/CD, MLflow, DVC, model serving</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='info-card'>
            <h4>Ideal roles</h4>
            <p>AI Engineer</p>
            <p>ML Engineer</p>
            <p>LLM Application Engineer</p>
            <p>Data Scientist</p>
            <p>Applied AI / Agentic AI Engineer</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.subheader("Career arc")
for item in [
    ("Enterprise foundation", "Built scalable data platforms and analytics workflows in consulting environments handling large, business-critical datasets."),
    ("Graduate deepening", "Strengthened statistics, machine learning, forecasting, and causal reasoning through a data science-focused master's program."),
    ("Modern AI builder", "Focused on LLM-powered applications, agentic systems, RAG architectures, and practical ML products that recruiters can immediately understand."),
]:
    st.markdown(
        f"""
        <div class='timeline-item'>
            <div class='timeline-title'>{item[0]}</div>
            <div class='timeline-text'>{item[1]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
