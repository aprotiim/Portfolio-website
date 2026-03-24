import base64
from pathlib import Path

import streamlit as st

# ── Inline style constants (bypass Streamlit CSS override) ────────────────────
_TAG = (
    "display:inline-block;padding:0.3rem 0.7rem;border-radius:999px;"
    "background:rgba(110,231,249,0.12);border:1px solid rgba(110,231,249,0.18);"
    "color:#6ee7f9;font-size:0.8rem;font-weight:600;margin-bottom:0.6rem;"
)
_TECH = (
    "display:inline-block;padding:0.18rem 0.6rem;border-radius:999px;"
    "background:rgba(110,231,249,0.10);border:1px solid rgba(110,231,249,0.20);"
    "color:#93e8f7;font-size:0.72rem;font-weight:500;margin:2px 3px 2px 0;"
)


def _tech_pills(items):
    spans = " ".join(f"<span style='{_TECH}'>{t}</span>" for t in items)
    return f"<p style='margin:0 0 0.7rem 0;line-height:2;'>{spans}</p>"


# ── Thumbnail loader ───────────────────────────────────────────────────────────
# Place individual images in assets/ named: thumb_blog.png, thumb_crag.png,
# thumb_chatbot.png, thumb_recommender.png, thumb_sentiment.png, thumb_selfrag.png

_ASSETS = Path(__file__).resolve().parents[1] / "assets"
_THUMBS: dict = {}


def _load_thumbs():
    if _THUMBS:
        return
    for key in ("blog", "crag", "chatbot", "recommender", "sentiment", "selfrag"):
        path = _ASSETS / f"thumb_{key}.png"
        if path.exists():
            _THUMBS[key] = base64.b64encode(path.read_bytes()).decode()


_load_thumbs()

# ── Projects data ──────────────────────────────────────────────────────────────
projects = [
    {
        "key": "blog",
        "title": "AI Agent Blog Planner and Writer",
        "repo": "https://github.com/aprotiim/AI-Agent_Blog-planner-and-writer",
        "tag": "Agentic AI",
        "tech": ["LangGraph", "LangChain", "Multi-Agent", "Tavily", "DALL·E", "Python"],
        "summary": "A multi-agent content workflow that plans tasks, decides when web research is required, parallelizes subtasks, adds citations and images, and generates blog output end-to-end.",
        "highlights": [
            "Demonstrates planning-before-execution instead of single-shot prompting",
            "Shows multi-agent orchestration and parallel worker design — improved content generation latency by ~35%",
            "Reflects strong product thinking around content generation pipelines",
        ],
    },
    {
        "key": "crag",
        "title": "Corrective RAG Knowledge System",
        "repo": "https://github.com/aprotiim/C-RAG-Knowledge-System",
        "tag": "RAG / Evaluation",
        "tech": ["LangGraph", "LangChain", "FAISS", "Tavily", "OpenAI", "Python"],
        "summary": "A corrective RAG system using LangGraph and LangChain with retrieval evaluation, query rewriting, and web-search augmentation when local context is weak or irrelevant.",
        "highlights": [
            "Solves a real weakness in standard RAG: trusting retrieval too easily",
            "Reduced hallucination rate by 40% through retrieval confidence scoring and adaptive web augmentation",
            "Strong signal for LLM systems engineering roles",
        ],
    },
    {
        "key": "chatbot",
        "title": "Chatbot using LangGraph",
        "repo": "https://github.com/aprotiim/Chatbot-using-Langgraph",
        "tag": "Production Chatbot",
        "tech": ["LangGraph", "RAG", "MCP", "HITL", "Streamlit", "FastAPI", "Python"],
        "summary": "A Streamlit-based chatbot built with LangGraph supporting tool calling, MCP integration, RAG as a tool, persistent memory, PDF upload, and document indexing.",
        "highlights": [
            "Closer to real product architecture than a basic demo chatbot",
            "Reduced average response latency by ~25% via caching and async inference routing",
            "Highlights production-oriented UX and system integration thinking",
        ],
    },
    {
        "key": "sentiment",
        "title": "YouTube Comments Analysis",
        "repo": "https://github.com/aprotiim/Youtube-Comments-Analysis",
        "tag": "NLP / Analytics",
        "tech": ["XGBoost", "Logistic Regression", "Random Forest", "FastAPI", "NLTK", "Python"],
        "summary": "A sentiment analysis system for YouTube comments with analytics charts, common-word extraction, trend tracking, and REST API exposure for downstream applications.",
        "highlights": [
            "Built NLP sentiment classifier on 100K+ YouTube comments with preprocessing and feature engineering",
            "Improved macro-F1 by ~13% through model selection and hyperparameter tuning",
            "Shows end-to-end NLP workflow beyond notebook-only analysis with REST API layer",
        ],
    },
    {
        "key": "selfrag",
        "title": "Self-RAG: Self-Reflective Retrieval System",
        "repo": "https://github.com/aprotiim/Self_RAG",
        "tag": "Agentic RAG",
        "tech": ["LangGraph", "LangChain", "FAISS", "Self-Reflection", "OpenAI", "Python"],
        "summary": "A self-reflective RAG system where the LLM actively evaluates its own retrieval decisions, document relevance, answer grounding, and response usefulness — rather than blindly accepting retrieved content.",
        "highlights": [
            "Implements four decision modules: retrieve gating, relevance filtering, grounding verification, and usefulness scoring",
            "Iterative feedback loop with query rewriting and answer revision until quality thresholds are met",
            "Addresses core RAG failures (blind trust, hallucination, incomplete responses) that standard pipelines ignore",
        ],
    },
    {
        "key": "recommender",
        "title": "Spotify Recommendation System",
        "repo": "https://github.com/aprotiim/Spotify-Recommendation-System",
        "tag": "Recommender Systems",
        "tech": ["Collaborative Filtering", "Content-Based", "Cosine Similarity", "Streamlit", "Python"],
        "summary": "A hybrid recommender that combines content-based filtering and collaborative filtering, normalizes scores, handles cold start, and exposes a simple Streamlit UI.",
        "highlights": [
            "Demonstrates core recommendation-system concepts cleanly",
            "Improved Recall@10 by ~18% through model tuning and similarity weighting",
            "Useful recruiter signal for ranking and personalization roles",
        ],
    },
]

# ── Render ─────────────────────────────────────────────────────────────────────
st.title("Projects")
st.caption("A selection of recruiter-facing projects that show how I think about architecture, AI workflows, and practical impact.")

for i in range(0, len(projects), 2):
    cols = st.columns(2, gap="large")
    for col, project in zip(cols, projects[i:i+2]):
        with col:
            tech_row = _tech_pills(project["tech"])
            tag_html = f"<div style='{_TAG}'>{project['tag']}</div>"
            b64 = _THUMBS.get(project["key"])

            if b64:
                img_html = (
                    f"<img src='data:image/png;base64,{b64}' "
                    "style='width:100%;height:auto;display:block;'>"
                )
                card = f"""
                <div style='
                    background:linear-gradient(135deg,rgba(21,38,72,0.82),rgba(14,26,54,0.90));
                    border:1px solid rgba(148,163,184,0.16);
                    border-radius:22px;
                    box-shadow:0 12px 32px rgba(0,0,0,0.28);
                    margin-bottom:1rem;
                    overflow:hidden;
                    display:flex;
                    flex-direction:column;
                    min-height:460px;
                    transition:transform 0.2s ease,box-shadow 0.2s ease;
                '>
                    {img_html}
                    <div style='padding:1.2rem 1.4rem 1.4rem 1.4rem;display:flex;flex-direction:column;flex:1;'>
                        {tag_html}
                        <h3 style='margin-top:0.3rem;color:#e5eefb;'>{project['title']}</h3>
                        {tech_row}
                        <p style='margin-bottom:1rem;'>{project['summary']}</p>
                        <p style='margin-top:auto;margin-bottom:0;'><a href='{project['repo']}' target='_blank'>View repository ↗</a></p>
                    </div>
                </div>
                """
            else:
                card = f"""
                <div class='project-card'>
                    {tag_html}
                    <h3 style='margin-top:0;color:#e5eefb;'>{project['title']}</h3>
                    {tech_row}
                    <p style='margin-bottom:1rem;'>{project['summary']}</p>
                    <p style='margin-top:auto;margin-bottom:0;'><a href='{project['repo']}' target='_blank'>View repository ↗</a></p>
                </div>
                """

            st.markdown(card, unsafe_allow_html=True)

st.subheader("What these projects communicate to recruiters")
col1, col2, col3 = st.columns(3, gap="large")
with col1:
    st.markdown("<div class='info-card'><h4>Depth</h4><p>These are not generic tutorials. They show architectural thinking and a clear understanding of modern AI system patterns.</p></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='info-card'><h4>Range</h4><p>The portfolio spans LLMs, retrieval, recommender systems, NLP, agentic AI, and production-oriented app building.</p></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='info-card'><h4>Relevance</h4><p>The stack maps well to AI engineer, ML engineer, applied scientist, and LLM application roles.</p></div>", unsafe_allow_html=True)
