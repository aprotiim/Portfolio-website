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

nav_pages = [
    ("pages/0_Home.py",            "🏠 Home"),
    ("pages/1_About.py",           "👋 About"),
    ("pages/2_Projects.py",        "🧠 Projects"),
    ("pages/3_Work_Experience.py", "💼 Experience"),
    ("pages/4_Education.py",       "🎓 Education"),
    ("pages/5_Contact.py",         "📬 Contact"),
]

pg = st.navigation([
    st.Page("pages/0_Home.py",            title="Home",            icon="🏠", default=True),
    st.Page("pages/1_About.py",           title="About",           icon="👋"),
    st.Page("pages/2_Projects.py",        title="Projects",        icon="🧠"),
    st.Page("pages/3_Work_Experience.py", title="Work Experience", icon="💼"),
    st.Page("pages/4_Education.py",       title="Education",       icon="🎓"),
    st.Page("pages/5_Contact.py",         title="Contact",         icon="📬"),
])

# ── Mobile hamburger (only visible on mobile via CSS) ─────────────────────────
with st.expander("☰  Menu", expanded=False):
    for page, label in nav_pages:
        st.page_link(page, label=label, use_container_width=True)

# ── Desktop nav (only visible on desktop via CSS) ─────────────────────────────
cols = st.columns(len(nav_pages))
for col, (page, label) in zip(cols, nav_pages):
    with col:
        st.page_link(page, label=label, use_container_width=True)

pg.run()
