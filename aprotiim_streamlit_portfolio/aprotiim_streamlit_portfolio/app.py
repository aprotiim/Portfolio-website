import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Aprotiim Joardar | AI/ML Engineer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT = Path(__file__).parent


def load_css() -> None:
    css = (ROOT / "assets" / "styles.css").read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def metric_card(label: str, value: str, caption: str = "") -> None:
    st.markdown(
        f"""
        <div class='metric-card'>
            <div class='metric-value'>{value}</div>
            <div class='metric-label'>{label}</div>
            <div class='metric-caption'>{caption}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


load_css()

st.sidebar.markdown("## Navigation")
st.sidebar.info(
    "Use the pages in the sidebar to explore About, Projects, Work Experience, Education, and Contact."
)
st.sidebar.markdown("---")
st.sidebar.markdown("**Location**  \\nGainesville, Florida")
st.sidebar.markdown("**Email**  \\naprotiim@gmail.com")
st.sidebar.markdown("**Phone**  \\n352-709-5368")
st.sidebar.markdown("**GitHub**  \\n[github.com/aprotiim](https://github.com/aprotiim)")
st.sidebar.markdown("**LinkedIn**  \\nAdd your LinkedIn URL here")

col1, col2 = st.columns([1.4, 1], gap="large")

with col1:
    st.markdown(
        """
        <div class='hero-card'>
            <div class='eyebrow'>AI/ML Engineer • Data Scientist • Ex-KPMG</div>
            <h1 class='hero-title'>I build intelligent systems that connect <span>data engineering rigor</span> with <span>modern AI products</span>.</h1>
            <p class='hero-subtitle'>
            I'm Aprotiim Joardar — an AI/ML engineer and data scientist with a background in enterprise-scale data systems,
            machine learning, retrieval-augmented generation, and production-minded AI application design.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='section-card'>
            <h3>My story</h3>
            <p>
            I started by solving hard data problems in enterprise environments, where reliability, scale, and stakeholder trust mattered.
            At KPMG, I built distributed pipelines and analytics systems across large ERP datasets. During my master's at the University of Florida,
            I deepened that foundation with machine learning, forecasting, and AI research. Today, my work sits at the intersection of
            LLM systems, data products, and deployable ML engineering.
            </p>
            <p>
            The result is a profile that is unusual in the best way: I do not just prototype AI ideas — I think about architecture,
            evaluation, latency, robustness, and how systems behave in the real world.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    metric_card("Years of experience", "5+", "Data science, ML systems, and analytics engineering")
    metric_card("Graduate GPA", "3.91", "M.S. in Information Systems & Operations Management")
    metric_card("Forecast error reduced", "18%", "Research work on quarterly firm revenue forecasting")
    metric_card("Pipeline scale handled", "20TB+", "Enterprise data engineering at KPMG")

st.markdown("### What recruiters should know")
rec_col1, rec_col2, rec_col3 = st.columns(3, gap="large")

with rec_col1:
    st.markdown(
        """
        <div class='info-card'>
            <h4>Systems-first AI mindset</h4>
            <p>Strong foundation in ETL, PySpark, SQL, feature pipelines, model evaluation, and deployment thinking.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with rec_col2:
    st.markdown(
        """
        <div class='info-card'>
            <h4>Modern GenAI portfolio</h4>
            <p>Projects span agentic workflows, corrective RAG, production chatbots, recommender systems, and NLP analytics.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with rec_col3:
    st.markdown(
        """
        <div class='info-card'>
            <h4>Business + technical fluency</h4>
            <p>Experience translating business problems into scalable technical solutions across consulting and research settings.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")
st.caption("Built with Streamlit as a recruiter-friendly portfolio with five dedicated pages.")
