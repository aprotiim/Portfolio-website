import base64
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parents[1]

def _resume_b64():
    path = ROOT / "assets" / "APROTIIM_JOARDAR_AI_ML_Engineer_final.pdf"
    if path.exists():
        return base64.b64encode(path.read_bytes()).decode()
    return None


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


# ── Hero + Right panel ─────────────────────────────────────────────────────────
col1, col2 = st.columns([2.8, 1.6], gap="large")

with col1:
    st.markdown(
        """
        <div class='hero-card' style='height:100%;box-sizing:border-box;display:flex;flex-direction:column;justify-content:space-between;'>
            <div>
                <h1 class='hero-title' style='font-size:3rem;margin-bottom:0.5rem;'>Hi, I'm <span>Aprotiim Joardar</span></h1>
                <div class='eyebrow' style='font-size:1.1rem;margin-bottom:0.6rem;text-transform:none;letter-spacing:normal;'>AI Engineer building production-grade LLM systems and scalable AI products.</div>
                <p style='font-size:1.0rem;font-weight:600;color:#e5eefb;margin:0 0 0.8rem 0;letter-spacing:0.03em;'>Ex-KPMG &nbsp;·&nbsp; University of Florida</p>
                <p style='font-size:1.0rem;color:#e5eefb;line-height:1.7;margin:0 0 0.8rem 0;'>
                I design systems that combine data engineering, machine learning, and GenAI — built for reliability and real-world scale, not just notebooks.
                </p>
                <div class='available-badge'>
                    <span class='available-dot'></span>
                    🚀 Open to AI Engineer / ML Engineer / Data Scientist roles
                </div>
            </div>
            <div class='cta-buttons' style='margin-top:1.2rem;'>
                <a class='cta-btn cta-btn-primary' href='https://github.com/aprotiim' target='_blank'>View AI Projects ↗</a>
                <a class='cta-btn cta-btn-secondary' href='/Contact'>Connect with me ↗</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    resume_b64 = _resume_b64()
    resume_btn = (
        f"<a class='cta-btn cta-btn-primary' "
        f"href='data:application/pdf;base64,{resume_b64}' "
        f"target='_blank' "
        f"style='background:linear-gradient(90deg,#0e7490,#6d28d9);color:#ffffff!important;font-weight:700;font-size:0.9rem;letter-spacing:0.04em;border:none;border-radius:12px;box-shadow:0 4px 20px rgba(110,231,249,0.25);width:100%;text-align:center;display:block;padding:0.65rem 1rem;'>📄 Resume ↗</a>"
        if resume_b64 else ""
    )
    photo_path = ROOT / "assets" / "photo.jpeg"
    photo_b64 = base64.b64encode(photo_path.read_bytes()).decode() if photo_path.exists() else None
    photo_tag = (
        f"<img src='data:image/jpeg;base64,{photo_b64}' class='hero-photo'>"
        if photo_b64 else ""
    )
    st.markdown(
        f"""
        <div class='hero-card side-panel'>
            <div class='side-photo-wrap'>
                {photo_tag}
                <div style='text-align:center;margin-top:0.6rem;font-size:0.78rem;font-weight:600;color:#94a9c9;letter-spacing:0.04em;'>
                    AI Engineer &nbsp;·&nbsp; ML Engineer &nbsp;·&nbsp; Data Scientist
                </div>
            </div>
            <div class='side-metrics'>
                <div class='metric-card'><div class='metric-value'>5+</div><div class='metric-label'>Experience</div><div class='metric-caption'>Years</div></div>
                <div class='metric-card'><div class='metric-value'>3.91</div><div class='metric-label'>GPA</div><div class='metric-caption'>Graduate</div></div>
                <div class='metric-card'><div class='metric-value'>20TB+</div><div class='metric-label'>Data Scale</div><div class='metric-caption'>at KPMG</div></div>
            </div>
            <div class='side-ctas'>
                {resume_btn}
                <a class='cta-btn cta-btn-secondary' href='https://www.linkedin.com/in/aprotiim-joardar-595074118/' target='_blank' style='width:100%;text-align:center;display:block;border-radius:12px;font-size:0.9rem;letter-spacing:0.04em;'>💼 LinkedIn ↗</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ── Featured Projects (full width) ─────────────────────────────────────────────
st.markdown("### Featured Projects")

_TAG = (
    "display:inline-block;padding:0.25rem 0.65rem;border-radius:999px;"
    "background:rgba(110,231,249,0.12);border:1px solid rgba(110,231,249,0.18);"
    "color:#6ee7f9;font-size:0.75rem;font-weight:600;margin-bottom:0.6rem;"
)

featured = [
    {
        "title": "AI Agent Blog Planner & Writer",
        "tag": "Agentic AI",
        "desc": "Multi-agent workflow that plans, researches, and writes full blog posts end-to-end with citations and images.",
        "repo": "https://github.com/aprotiim/AI-Agent_Blog-planner-and-writer",
        "thumb": "thumb_blog.png",
        "img_pos": "center center",
    },
    {
        "title": "Self-RAG: Self-Reflective Retrieval",
        "tag": "Agentic RAG",
        "desc": "LLM that evaluates its own retrieval decisions, filters relevance, verifies grounding, and rewrites until quality thresholds are met.",
        "repo": "https://github.com/aprotiim/Self_RAG",
        "thumb": "thumb_selfrag.png",
        "img_pos": "center top",
    },
    {
        "title": "Corrective RAG Knowledge System",
        "tag": "RAG / Evaluation",
        "desc": "Corrective RAG that scores retrieval confidence and falls back to web search when local context is weak — reducing hallucinations by 40%.",
        "repo": "https://github.com/aprotiim/C-RAG-Knowledge-System",
        "thumb": "thumb_crag.png",
        "img_pos": "center center",
    },
]

proj_cols = st.columns(3, gap="large")
for col, p in zip(proj_cols, featured):
    thumb_path = ROOT / "assets" / p["thumb"]
    b64 = base64.b64encode(thumb_path.read_bytes()).decode() if thumb_path.exists() else None
    img_pos = p.get("img_pos", "center center")
    img_html = (
        f"<img src='data:image/png;base64,{b64}' "
        f"style='width:100%;height:auto;display:block;'>"
    ) if b64 else ""
    with col:
        st.markdown(
            f"""
            <div style='background:linear-gradient(135deg,rgba(21,38,72,0.82),rgba(14,26,54,0.90));
                        border:1px solid rgba(148,163,184,0.16);border-radius:18px;
                        box-shadow:0 8px 24px rgba(0,0,0,0.22);overflow:hidden;
                        display:flex;flex-direction:column;margin-bottom:0.5rem;'>
                {img_html}
                <div style='padding:1.1rem 1.3rem 1.3rem 1.3rem;'>
                    <div style='{_TAG}'>{p["tag"]}</div>
                    <h4 style='margin:0.3rem 0 0.6rem 0;color:#e5eefb;font-size:1rem;line-height:1.4;'>{p["title"]}</h4>
                    <p style='font-size:0.85rem;color:#94a9c9;line-height:1.6;margin:0 0 0.8rem 0;'>{p["desc"]}</p>
                    <a href='{p["repo"]}' target='_blank'
                       style='font-size:0.83rem;font-weight:600;color:#6ee7f9;'>View repo ↗</a>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ── My Story (full width) ──────────────────────────────────────────────────────
st.markdown(
    """
    <div class='section-card'>
        <h3>My Story</h3>
        <p>I began by solving hard data problems in enterprise systems — where things don't break quietly and scale is never optional.</p>
        <ul>
            <li><strong>KPMG</strong> → built large-scale pipelines and analytics systems on complex ERP data</li>
            <li><strong>University of Florida</strong> → focused on machine learning, forecasting, and AI systems</li>
            <li><strong>Now</strong> → building LLM-powered applications and production-grade AI systems</li>
        </ul>
        <p style='margin-bottom:0.3rem;'><strong>What makes me different:</strong></p>
        <p style='margin:0;'>I don't just prototype AI — I build systems that work outside notebooks, in real-world, messy environments.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── What recruiters should know ────────────────────────────────────────────────
st.markdown("### What I bring")
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
st.caption("Built with Streamlit · AI/ML Engineer portfolio · aprotiim@gmail.com")
