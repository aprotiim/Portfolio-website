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
    <div class="topnav-links">
        <a href="/home">🏠 Home</a>
        <a href="/about">👋 About</a>
        <a href="/projects">🧠 Projects</a>
        <a href="/work-experience">💼 Experience</a>
        <a href="/education">🎓 Education</a>
        <a href="/contact">📬 Contact</a>
    </div>
    <button class="ham-btn" id="hamBtn" aria-label="Menu">
        <span></span><span></span><span></span>
    </button>
    <div class="ham-menu" id="hamMenu">
        <a href="/home">🏠 Home</a>
        <a href="/about">👋 About</a>
        <a href="/projects">🧠 Projects</a>
        <a href="/work-experience">💼 Experience</a>
        <a href="/education">🎓 Education</a>
        <a href="/contact">📬 Contact</a>
    </div>
</nav>
<script>
(function() {
    var btn = document.getElementById('hamBtn');
    var menu = document.getElementById('hamMenu');
    if (btn) {
        btn.addEventListener('click', function() {
            btn.classList.toggle('active');
            menu.classList.toggle('open');
        });
    }
    // Highlight current page
    var path = window.location.pathname;
    document.querySelectorAll('.topnav-links a, .ham-menu a').forEach(function(a) {
        if (a.getAttribute('href') === path || (path === '/' && a.getAttribute('href') === '/home')) {
            a.classList.add('active');
        }
    });
})();
</script>
""", unsafe_allow_html=True)

pg.run()
