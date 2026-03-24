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


load_css()

# ── Persistent sidebar (shows on every page) ──────────────────────────────────
st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    <div style='padding:0.2rem 0 0.5rem 0;'>

      <a href='mailto:aprotiim@gmail.com' style='text-decoration:none;'>
        <div style='display:flex;align-items:center;gap:0.65rem;padding:0.55rem 0.6rem;border-radius:10px;margin-bottom:4px;transition:background 0.2s;'>
          <div style='width:34px;height:34px;border-radius:8px;background:rgba(110,231,249,0.12);border:1px solid rgba(110,231,249,0.22);display:flex;align-items:center;justify-content:center;font-size:1rem;flex-shrink:0;'>✉️</div>
          <div>
            <div style='font-size:0.68rem;font-weight:700;color:#94a9c9;text-transform:uppercase;letter-spacing:0.07em;'>Email</div>
            <div style='font-size:0.82rem;color:#6ee7f9;'>aprotiim@gmail.com</div>
          </div>
        </div>
      </a>

      <div style='display:flex;align-items:center;gap:0.65rem;padding:0.55rem 0.6rem;border-radius:10px;margin-bottom:4px;'>
        <div style='width:34px;height:34px;border-radius:8px;background:rgba(110,231,249,0.12);border:1px solid rgba(110,231,249,0.22);display:flex;align-items:center;justify-content:center;font-size:1rem;flex-shrink:0;'>📞</div>
        <div>
          <div style='font-size:0.68rem;font-weight:700;color:#94a9c9;text-transform:uppercase;letter-spacing:0.07em;'>Phone</div>
          <div style='font-size:0.82rem;color:#e5eefb;'>+1 352-709-5368</div>
        </div>
      </div>

      <a href='https://www.linkedin.com/in/aprotiim-joardar-595074118/' target='_blank' style='text-decoration:none;'>
        <div style='display:flex;align-items:center;gap:0.65rem;padding:0.55rem 0.6rem;border-radius:10px;margin-bottom:4px;'>
          <div style='width:34px;height:34px;border-radius:8px;background:rgba(10,102,194,0.20);border:1px solid rgba(10,102,194,0.35);display:flex;align-items:center;justify-content:center;font-size:1rem;flex-shrink:0;'>💼</div>
          <div>
            <div style='font-size:0.68rem;font-weight:700;color:#94a9c9;text-transform:uppercase;letter-spacing:0.07em;'>LinkedIn</div>
            <div style='font-size:0.82rem;color:#6ee7f9;'>aprotiim-joardar ↗</div>
          </div>
        </div>
      </a>

      <a href='https://github.com/aprotiim' target='_blank' style='text-decoration:none;'>
        <div style='display:flex;align-items:center;gap:0.65rem;padding:0.55rem 0.6rem;border-radius:10px;margin-bottom:4px;'>
          <div style='width:34px;height:34px;border-radius:8px;background:rgba(167,139,250,0.15);border:1px solid rgba(167,139,250,0.28);display:flex;align-items:center;justify-content:center;font-size:1rem;flex-shrink:0;'>⚡</div>
          <div>
            <div style='font-size:0.68rem;font-weight:700;color:#94a9c9;text-transform:uppercase;letter-spacing:0.07em;'>GitHub</div>
            <div style='font-size:0.82rem;color:#6ee7f9;'>github.com/aprotiim ↗</div>
          </div>
        </div>
      </a>

    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown("---")

resume_path = ROOT / "assets" / "APROTIIM_JOARDAR_AI_ML_Engineer_final.pdf"
if resume_path.exists():
    with open(resume_path, "rb") as f:
        st.sidebar.download_button(
            label="📄 Download Resume",
            data=f,
            file_name="Aprotiim_Joardar_AI_Engineer.pdf",
            mime="application/pdf",
            use_container_width=True,
        )

# ── Navigation ────────────────────────────────────────────────────────────────
pg = st.navigation([
    st.Page("pages/0_Home.py",             title="Home",            icon="🏠"),
    st.Page("pages/1_About.py",            title="About",           icon="👋"),
    st.Page("pages/2_Projects.py",         title="Projects",        icon="🧠"),
    st.Page("pages/3_Work_Experience.py",  title="Work Experience", icon="💼"),
    st.Page("pages/4_Education.py",        title="Education",       icon="🎓"),
    st.Page("pages/5_Contact.py",          title="Contact",         icon="📬"),
])

pg.run()
