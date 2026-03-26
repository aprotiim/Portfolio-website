from pathlib import Path
import streamlit as st
import anthropic

# ── System prompts ────────────────────────────────────────────────────────────
_SYSTEM = (
    "You are an AI assistant representing Aprotiim Joardar's professional portfolio. "
    "Answer recruiter and hiring manager questions concisely and professionally. "
    "Keep answers under 120 words. Do NOT use markdown formatting like **bold** or bullet points with asterisks — use plain text only.\n\n"
    "ABOUT APROTIIM:\n"
    "- AI Engineer, 5+ years experience. Ex-KPMG. University of Florida MS (GPA 3.91).\n"
    "- Location: Florida, USA — open to relocation.\n"
    "- Contact: aprotiim@gmail.com | github.com/aprotiim\n\n"
    "TARGET ROLES: AI Engineer, ML Engineer, Data Scientist, Applied LLM roles.\n\n"
    "EDUCATION: M.S. Information Systems & Operations Management (Data Science Concentration) — University of Florida, GPA 3.91. Aug 2023–May 2025. Honors: Exxon Mobil Scholarship, 3x Director's Choice Academic Excellence Award.\n\n"
    "EXPERIENCE:\n"
    "- KPMG: Data Engineer — built 20TB+ ERP data pipelines, enterprise analytics, "
    "translated business problems into scalable technical solutions.\n\n"
    "SKILLS: Python, SQL, PySpark, PyTorch, TensorFlow, scikit-learn, Hugging Face, "
    "LangChain, LlamaIndex, LLM fine-tuning, RAG, Agentic AI, Prompt Engineering, "
    "Apache Spark, Airflow, dbt, ETL, PostgreSQL, Snowflake, BigQuery, AWS, GCP, MLflow, Docker.\n\n"
    "KEY PROJECTS:\n"
    "1. AI Agent Blog Planner & Writer — multi-agent LangGraph workflow, end-to-end blog creation.\n"
    "2. Self-RAG — self-reflective retrieval LLM that evaluates its own retrieval quality.\n"
    "3. Corrective RAG Knowledge System — confidence-scored RAG with web fallback, -40% hallucinations.\n\n"
    "STRENGTHS: Enterprise data foundation + graduate ML depth + modern GenAI portfolio. "
    "Builds AI that works in production, not just notebooks.\n\n"
    "AVAILABILITY: Open to full-time roles. Open to relocation."
)

_FOLLOWUP_SYSTEM = (
    "Based on the last exchange in a recruiter-portfolio chat, suggest exactly 3 short follow-up "
    "questions a recruiter might ask next. Each question must be under 8 words. "
    "Return only the 3 questions, one per line, no numbering, no extra text."
)

_STARTERS = [
    "What's your strongest technical skill?",
    "Tell me about your AI projects",
    "What was your role at KPMG?",
    "What roles are you open to?",
    "What makes you stand out?",
    "Walk me through your best project",
]

# ── Helpers ───────────────────────────────────────────────────────────────────
def _client() -> anthropic.Anthropic:
    return anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])


def _chat(messages: list) -> str:
    r = _client().messages.create(
        model="claude-haiku-4-5",
        max_tokens=512,
        system=_SYSTEM,
        messages=messages,
    )
    return r.content[0].text


def _follow_ups(user_msg: str, assistant_msg: str) -> list[str]:
    r = _client().messages.create(
        model="claude-haiku-4-5",
        max_tokens=80,
        system=_FOLLOWUP_SYSTEM,
        messages=[{
            "role": "user",
            "content": f"User: {user_msg}\nAssistant: {assistant_msg}",
        }],
    )
    lines = [l.strip().lstrip("•-– ") for l in r.content[0].text.strip().splitlines() if l.strip()]
    return lines[:3]


def _process(prompt: str) -> None:
    """Add user message, get reply, store follow-ups — all in session state."""
    st.session_state.msgs.append({"role": "user", "content": prompt})
    reply = _chat(st.session_state.msgs)
    st.session_state.msgs.append({"role": "assistant", "content": reply})
    st.session_state.follow_ups = _follow_ups(prompt, reply)


# ── Init session state ────────────────────────────────────────────────────────
if "msgs" not in st.session_state:
    st.session_state.msgs = []
if "follow_ups" not in st.session_state:
    st.session_state.follow_ups = []

# Process any pending button-triggered prompt BEFORE rendering
if "pending" in st.session_state:
    with st.spinner(""):
        _process(st.session_state.pop("pending"))

# ── Page header ───────────────────────────────────────────────────────────────
st.title("Talk to my AI profile")
st.caption("Ask about my projects, experience, skills, or technical decisions.")

# ── Starter buttons (only when conversation is empty) ────────────────────────
if not st.session_state.msgs:
    st.markdown("#### Quick questions to get started")
    row1 = st.columns(3)
    row2 = st.columns(3)
    for i, prompt in enumerate(_STARTERS):
        col = row1[i] if i < 3 else row2[i - 3]
        with col:
            if st.button(prompt, use_container_width=True, key=f"s{i}"):
                st.session_state.pending = prompt
                st.rerun()
    st.divider()

# ── Chat history ──────────────────────────────────────────────────────────────
if st.session_state.msgs:
    with st.container(height=420, border=False):
        for msg in st.session_state.msgs:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

# ── Follow-up suggestion buttons ─────────────────────────────────────────────
if st.session_state.follow_ups:
    st.markdown(
        "<p style='font-size:0.78rem;color:#94a9c9;margin:0.6rem 0 0.35rem 0;"
        "font-weight:600;letter-spacing:0.03em;'>SUGGESTED FOLLOW-UPS</p>",
        unsafe_allow_html=True,
    )
    fcols = st.columns(len(st.session_state.follow_ups))
    for i, q in enumerate(st.session_state.follow_ups):
        with fcols[i]:
            if st.button(q, use_container_width=True, key=f"f{i}_{len(st.session_state.msgs)}"):
                st.session_state.pending = q
                st.rerun()

# ── Chat input ────────────────────────────────────────────────────────────────
if user_input := st.chat_input("Ask about experience, projects, skills…"):
    with st.spinner(""):
        _process(user_input)
    st.rerun()

# ── Clear button ─────────────────────────────────────────────────────────────
if st.session_state.msgs:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Clear conversation", type="secondary"):
        st.session_state.msgs = []
        st.session_state.follow_ups = []
        st.rerun()
