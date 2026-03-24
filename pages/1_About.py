import streamlit as st

# Pill styles — carried entirely by inline attributes, no CSS classes
_P = (
    "display:inline-block;padding:0.22rem 0.72rem;border-radius:999px;"
    "background:rgba(167,139,250,0.18);border:1px solid rgba(167,139,250,0.32);"
    "color:#c4b5fd;font-size:0.78rem;font-weight:500;margin:2px 3px 2px 0;line-height:1.6;"
)
_R = (
    "display:inline-block;padding:0.25rem 0.8rem;border-radius:999px;"
    "background:rgba(167,139,250,0.18);border:1px solid rgba(167,139,250,0.32);"
    "color:#c4b5fd;font-size:0.8rem;font-weight:600;margin:2px 3px 2px 0;line-height:1.6;"
)
_CAT = (
    "font-size:0.72rem;font-weight:700;color:#94a9c9 !important;"
    "text-transform:uppercase;letter-spacing:0.08em;"
    "display:block;margin-top:0.85rem;margin-bottom:0.3rem;"
)


def _pills(items, s=None):
    # Use <p> as container — inline-block spans inside a <p> wrap naturally.
    # This avoids relying on flex/grid which Streamlit's CSS can override.
    style = s or _P
    spans = " ".join(f"<span style='{style}'>{i}</span>" for i in items)
    return f"<p style='margin:0 0 0.2rem 0;line-height:2.2;'>{spans}</p>"


# ── Page ───────────────────────────────────────────────────────────────────────
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
        f"""
        <div class='info-card'>
          <h4 style='margin-top:0;margin-bottom:0.6rem;color:#e5eefb;'>Core strengths</h4>

          <span style='{_CAT}'>AI &amp; LLM Systems</span>
          {_pills(["RAG","LangGraph","Multi-Agent Systems","Prompt Engineering","Vector Databases"])}

          <span style='{_CAT}'>Machine Learning</span>
          {_pills(["Regression","Classification","Deep Learning","Feature Engineering","XGBoost","Model Evaluation"])}

          <span style='{_CAT}'>Data &amp; Distributed Systems</span>
          {_pills(["PySpark","SQL","Azure Databricks","HPC","Distributed Computing","ETL/ELT Pipelines"])}

          <span style='{_CAT}'>Deployment &amp; MLOps</span>
          {_pills(["FastAPI","Docker","MLflow","DVC","CI/CD","AWS EC2","S3","IAM","SageMaker","Bedrock","CodeDeploy"])}

          <span style='{_CAT}'>Analytics &amp; Visualization</span>
          {_pills(["Tableau","Alteryx","Statistical Modelling","Business Intelligence"])}

          <span style='{_CAT}'>AI Development Tools</span>
          {_pills(["Cursor","Claude Code","GitHub Copilot","Git","GitHub"])}
        </div>
        """,
        unsafe_allow_html=True,
    )


st.subheader("Career arc")
for title, text in [
    ("Enterprise foundation",
     "Built scalable data platforms and analytics workflows in consulting environments handling large, business-critical datasets."),
    ("Graduate deepening",
     "Strengthened statistics, machine learning, forecasting, and causal reasoning through a data science-focused master's program."),
    ("Modern AI builder",
     "Focused on LLM-powered applications, agentic systems, RAG architectures, and practical ML products that recruiters can immediately understand."),
]:
    st.markdown(
        f"""
        <div class='timeline-item'>
            <div class='timeline-title'>{title}</div>
            <div class='timeline-text'>{text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
