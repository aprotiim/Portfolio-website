import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Projects | Aprotiim Joardar", page_icon="🧠", layout="wide")
ROOT = Path(__file__).resolve().parents[1]
css = (ROOT / "assets" / "styles.css").read_text(encoding="utf-8")
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

st.title("Projects")
st.caption("A selection of recruiter-facing projects that show how I think about architecture, AI workflows, and practical impact.")

projects = [
    {
        "title": "AI Agent Blog Planner and Writer",
        "repo": "https://github.com/aprotiim/AI-Agent_Blog-planner-and-writer",
        "tag": "Agentic AI",
        "summary": "A multi-agent content workflow that plans tasks, decides when web research is required, parallelizes subtasks, adds citations and images, and generates blog output end-to-end.",
        "highlights": [
            "Demonstrates planning-before-execution instead of single-shot prompting",
            "Shows multi-agent orchestration and parallel worker design",
            "Reflects strong product thinking around content generation pipelines",
        ],
    },
    {
        "title": "Corrective RAG Knowledge System",
        "repo": "https://github.com/aprotiim/C-RAG-Knowledge-System",
        "tag": "RAG / Evaluation",
        "summary": "A corrective RAG system using LangGraph and LangChain with retrieval evaluation, query rewriting, and web-search augmentation when local context is weak or irrelevant.",
        "highlights": [
            "Solves a real weakness in standard RAG: trusting retrieval too easily",
            "Includes corrective actions based on retrieval quality",
            "Strong signal for LLM systems engineering roles",
        ],
    },
    {
        "title": "Chatbot using LangGraph",
        "repo": "https://github.com/aprotiim/Chatbot-using-Langgraph",
        "tag": "Production Chatbot",
        "summary": "A Streamlit-based chatbot built with LangGraph supporting tool calling, MCP integration, RAG as a tool, persistent memory, PDF upload, and document indexing.",
        "highlights": [
            "Closer to real product architecture than a basic demo chatbot",
            "Combines orchestration, retrieval, UI, and tool execution status",
            "Highlights production-oriented UX and system integration thinking",
        ],
    },
    {
        "title": "YouTube Comments Analysis",
        "repo": "https://github.com/aprotiim/Youtube-Comments-Analysis",
        "tag": "NLP / Analytics",
        "summary": "A sentiment analysis system for YouTube comments with analytics charts, common-word extraction, trend tracking, and REST API exposure for downstream applications.",
        "highlights": [
            "Shows end-to-end NLP workflow beyond notebook-only analysis",
            "Good mix of ML, API design, and user-facing utility",
            "Demonstrates practical thinking about analytics products",
        ],
    },
    {
        "title": "Spotify Recommendation System",
        "repo": "https://github.com/aprotiim/Spotify-Recommendation-System",
        "tag": "Recommender Systems",
        "summary": "A hybrid recommender that combines content-based filtering and collaborative filtering, normalizes scores, handles cold start, and exposes a simple Streamlit UI.",
        "highlights": [
            "Demonstrates core recommendation-system concepts cleanly",
            "Balances modeling logic with user experience",
            "Useful recruiter signal for ranking and personalization roles",
        ],
    },
]

for i in range(0, len(projects), 2):
    cols = st.columns(2, gap="large")
    for col, project in zip(cols, projects[i:i+2]):
        with col:
            bullets = "".join([f"<li>{item}</li>" for item in project["highlights"]])
            st.markdown(
                f"""
                <div class='project-card'>
                    <div class='project-tag'>{project['tag']}</div>
                    <h3>{project['title']}</h3>
                    <p>{project['summary']}</p>
                    <ul>{bullets}</ul>
                    <p><a href='{project['repo']}' target='_blank'>View repository ↗</a></p>
                </div>
                """,
                unsafe_allow_html=True,
            )

st.subheader("What these projects communicate to recruiters")
col1, col2, col3 = st.columns(3, gap="large")
with col1:
    st.markdown("<div class='info-card'><h4>Depth</h4><p>These are not generic tutorials. They show architectural thinking and a clear understanding of modern AI system patterns.</p></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='info-card'><h4>Range</h4><p>The portfolio spans LLMs, retrieval, recommender systems, NLP, deployment, and UX-oriented app building.</p></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='info-card'><h4>Relevance</h4><p>The stack maps well to AI engineer, ML engineer, applied scientist, and LLM application roles.</p></div>", unsafe_allow_html=True)
