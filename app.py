import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Aprotiim Joardar | AI/ML Engineer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent


def load_css() -> None:
    css = (ROOT / "assets" / "styles.css").read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


load_css()

# ── Navigation must be registered before st.page_link ─────────────────────────
pg = st.navigation([
    st.Page("pages/0_Home.py",             title="Home",            icon="🏠"),
    st.Page("pages/1_About.py",            title="About",           icon="👋"),
    st.Page("pages/2_Projects.py",         title="Projects",        icon="🧠"),
    st.Page("pages/3_Work_Experience.py",  title="Work Experience", icon="💼"),
    st.Page("pages/4_Education.py",        title="Education",       icon="🎓"),
    st.Page("pages/5_Contact.py",          title="Contact",         icon="📬"),
])

# ── Navigation bar (desktop tabs + mobile hamburger) ──────────────────────────
st.markdown("""
<nav class="topnav">
    <input type="checkbox" id="nav-toggle" class="nav-toggle">
    <div class="topnav-links">
        <a href="/home">🏠 Home</a>
        <a href="/about">👋 About</a>
        <a href="/projects">🧠 Projects</a>
        <a href="/work-experience">💼 Experience</a>
        <a href="/education">🎓 Education</a>
        <a href="/contact">📬 Contact</a>
    </div>
    <label for="nav-toggle" class="ham-btn" aria-label="Menu">
        <span></span><span></span><span></span>
    </label>
    <div class="ham-menu">
        <a href="/home">🏠 Home</a>
        <a href="/about">👋 About</a>
        <a href="/projects">🧠 Projects</a>
        <a href="/work-experience">💼 Experience</a>
        <a href="/education">🎓 Education</a>
        <a href="/contact">📬 Contact</a>
    </div>
</nav>
""", unsafe_allow_html=True)

pg.run()
