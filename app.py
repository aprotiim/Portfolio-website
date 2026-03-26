import json
import streamlit as st
import streamlit.components.v1 as components
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

# ── Chat Popup ─────────────────────────────────────────────────────────────────
# Injected directly into the Streamlit DOM via st.markdown so that
# position:fixed is relative to the screen viewport (not an iframe viewport).
# JavaScript is executed via the <img onerror> trick because React strips
# <script> tags from dangerouslySetInnerHTML.
_API_KEY = st.secrets.get("ANTHROPIC_API_KEY", "")

_SYSTEM = (
    "You are an AI assistant representing Aprotiim Joardar's professional portfolio. "
    "Answer recruiter and hiring manager questions concisely and professionally. "
    "Keep answers under 120 words. Use plain text only, no markdown formatting, "
    "no asterisks, no bullet symbols.\n\n"
    "ABOUT: AI Engineer, 5+ years experience. Ex-KPMG. University of Florida MS GPA 3.91. "
    "Florida USA, open to relocation. Contact: aprotiim@gmail.com\n\n"
    "TARGET ROLES: AI Engineer, ML Engineer, Data Scientist, Applied LLM roles.\n\n"
    "EDUCATION: M.S. Information Systems and Operations Management (Data Science Concentration), "
    "University of Florida, GPA 3.91, Aug 2023 to May 2025. "
    "Honors: Exxon Mobil Scholarship, 3x Directors Choice Academic Excellence Award.\n\n"
    "EXPERIENCE: KPMG Data Engineer, built 20TB+ ERP data pipelines and enterprise analytics, "
    "translated business problems into scalable technical solutions.\n\n"
    "SKILLS: Python, SQL, PySpark, PyTorch, TensorFlow, LangChain, LlamaIndex, RAG, Agentic AI, "
    "Prompt Engineering, Apache Spark, Airflow, dbt, ETL, PostgreSQL, Snowflake, BigQuery, "
    "AWS, GCP, MLflow, Docker.\n\n"
    "KEY PROJECTS: "
    "1. AI Agent Blog Planner and Writer: multi-agent LangGraph workflow, end-to-end blog creation. "
    "2. Self-RAG: self-reflective retrieval LLM that evaluates its own retrieval quality. "
    "3. Corrective RAG Knowledge System: confidence-scored RAG with web fallback, "
    "40 percent fewer hallucinations."
)

_STARTERS = [
    "What's your strongest technical skill?",
    "Tell me about your AI projects",
    "What was your role at KPMG?",
    "What roles are you open to?",
    "What makes you stand out?",
    "Walk me through your best project",
]

_starters_html = "".join(
    f'<button class="cw-s" data-q="{s}">{s}</button>'
    for s in _STARTERS
)

st.markdown(f"""
<style>
#cw-fab{{position:fixed;top:95px;right:20px;z-index:2147483647;display:inline-flex;align-items:center;gap:8px;padding:10px 16px 10px 12px;background:linear-gradient(135deg,#0e7490,#6d28d9);color:#fff;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;font-weight:700;font-size:.82rem;letter-spacing:.02em;border-radius:50px;border:none;cursor:pointer;white-space:nowrap;box-shadow:0 4px 24px rgba(110,231,249,.45);animation:cwp 2.5s infinite;transition:transform .15s;}}
#cw-fab:hover{{transform:scale(1.04);}}
@keyframes cwp{{0%,100%{{box-shadow:0 4px 24px rgba(110,231,249,.45),0 0 0 0 rgba(110,231,249,.4);}}70%{{box-shadow:0 4px 24px rgba(110,231,249,.45),0 0 0 12px rgba(110,231,249,0);}}}}
#cw-panel{{position:fixed;top:148px;right:20px;z-index:2147483647;width:340px;max-width:calc(100vw - 40px);flex-direction:column;background:#0f172a;border:1px solid rgba(148,163,184,.2);border-radius:16px;overflow:hidden;box-shadow:0 16px 48px rgba(0,0,0,.55);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;}}
#cw-hdr{{display:flex;align-items:center;justify-content:space-between;padding:11px 13px;flex-shrink:0;border-bottom:1px solid rgba(148,163,184,.15);background:linear-gradient(90deg,rgba(14,116,144,.25),rgba(109,40,217,.25));}}
#cw-hdr span{{color:#e5eefb;font-weight:700;font-size:.84rem;}}
.cw-hb{{background:none;border:1px solid rgba(148,163,184,.2);color:#94a9c9;cursor:pointer;font-size:.7rem;padding:3px 7px;border-radius:6px;margin-left:4px;font-family:inherit;transition:background .15s;}}
.cw-hb:hover{{background:rgba(148,163,184,.15);}}
#cw-close{{border:none;font-size:.95rem;}}
#cw-msgs{{flex:1;overflow-y:auto;padding:11px;display:flex;flex-direction:column;gap:7px;min-height:50px;max-height:220px;}}
.cw-b{{max-width:85%;padding:7px 11px;border-radius:11px;font-size:.81rem;line-height:1.55;word-wrap:break-word;}}
.cw-b-u{{background:linear-gradient(135deg,#0e7490,#6d28d9);color:#fff;align-self:flex-end;border-bottom-right-radius:3px;}}
.cw-b-a{{background:rgba(30,41,59,.95);color:#e5eefb;border:1px solid rgba(148,163,184,.12);align-self:flex-start;border-bottom-left-radius:3px;}}
#cw-starters{{padding:7px 9px 5px;display:flex;flex-wrap:wrap;gap:5px;flex-shrink:0;border-bottom:1px solid rgba(148,163,184,.1);}}
.cw-s{{background:rgba(14,116,144,.15);border:1px solid rgba(110,231,249,.22);color:#6ee7f9;font-size:.73rem;padding:4px 9px;border-radius:999px;cursor:pointer;white-space:nowrap;font-family:inherit;transition:background .15s;}}
.cw-s:hover{{background:rgba(14,116,144,.32);}}
#cw-inp-row{{display:flex;align-items:center;gap:5px;padding:9px;flex-shrink:0;border-top:1px solid rgba(148,163,184,.12);background:rgba(15,23,42,.85);}}
#cw-inp{{flex:1;background:rgba(30,41,59,.85);border:1px solid rgba(148,163,184,.22);border-radius:7px;padding:6px 9px;color:#e5eefb;font-size:.81rem;font-family:inherit;outline:none;}}
#cw-inp:focus{{border-color:rgba(110,231,249,.55);}}
#cw-inp::placeholder{{color:#4a5568;}}
#cw-snd{{background:linear-gradient(135deg,#0e7490,#6d28d9);border:none;border-radius:7px;color:#fff;cursor:pointer;padding:6px 11px;font-size:.81rem;flex-shrink:0;transition:opacity .15s;}}
#cw-snd:hover{{opacity:.85;}}
#cw-snd:disabled{{opacity:.35;cursor:not-allowed;}}
.cw-d{{display:inline-block;width:6px;height:6px;background:#6ee7f9;border-radius:50%;margin:0 2px;animation:cwbd 1.2s infinite;}}
.cw-d:nth-child(2){{animation-delay:.2s;}}
.cw-d:nth-child(3){{animation-delay:.4s;}}
@keyframes cwbd{{0%,60%,100%{{transform:translateY(0);}}30%{{transform:translateY(-5px);}}}}
</style>

<button id="cw-fab">🤖 Talk to Aprotiim's AI Clone</button>
<div id="cw-panel" style="display:none">
  <div id="cw-hdr">
    <span>🤖 Aprotiim's AI Profile</span>
    <div>
      <button class="cw-hb" id="cw-clr">New Chat</button>
      <button class="cw-hb" id="cw-close">✕</button>
    </div>
  </div>
  <div id="cw-msgs"></div>
  <div id="cw-starters">{_starters_html}</div>
  <div id="cw-inp-row">
    <input id="cw-inp" type="text" placeholder="Ask about experience, projects…">
    <button id="cw-snd">Send ➤</button>
  </div>
</div>
""", unsafe_allow_html=True)

# Inject JS via components.html (same-origin iframe) so it reliably executes.
# window.parent.document gives access to the main Streamlit page DOM.
components.html(f"""<script>
(function(){{
  var K={json.dumps(_API_KEY)},Sys={json.dumps(_SYSTEM)};
  function init(){{
    var pdoc=window.parent.document;
    var fab=pdoc.getElementById('cw-fab');
    if(!fab){{setTimeout(init,50);return;}}
    var panel=pdoc.getElementById('cw-panel'),
        md=pdoc.getElementById('cw-msgs'),
        stDiv=pdoc.getElementById('cw-starters'),
        inp=pdoc.getElementById('cw-inp'),
        snd=pdoc.getElementById('cw-snd'),
        msgs=window.parent.__cwMsgs||[];
    fab.onclick=function(){{panel.style.display=panel.style.display==='flex'?'none':'flex';}};
    pdoc.getElementById('cw-close').onclick=function(){{panel.style.display='none';}};
    pdoc.getElementById('cw-clr').onclick=function(){{msgs=[];window.parent.__cwMsgs=[];md.innerHTML='';stDiv.style.display='flex';}};
    Array.prototype.forEach.call(pdoc.querySelectorAll('.cw-s'),function(b){{
      b.onclick=function(){{stDiv.style.display='none';doSend(b.dataset.q);}};
    }});
    inp.onkeydown=function(e){{if(e.key==='Enter'&&!e.shiftKey){{e.preventDefault();doSend(null);}}}};
    snd.onclick=function(){{doSend(null);}};
    function bub(r,t){{
      var b=pdoc.createElement('div');b.className='cw-b cw-b-'+r;b.textContent=t;
      md.appendChild(b);md.scrollTop=md.scrollHeight;
    }}
    function doSend(t){{
      var m=t||inp.value.trim();if(!m)return;
      inp.value='';msgs.push({{role:'user',content:m}});window.parent.__cwMsgs=msgs;bub('u',m);
      var ty=pdoc.createElement('div');ty.id='cw-ty';ty.className='cw-b cw-b-a';
      ty.innerHTML='<span class="cw-d"></span><span class="cw-d"></span><span class="cw-d"></span>';
      md.appendChild(ty);md.scrollTop=md.scrollHeight;
      inp.disabled=snd.disabled=true;
      fetch('https://api.anthropic.com/v1/messages',{{
        method:'POST',
        headers:{{'Content-Type':'application/json','x-api-key':K,'anthropic-version':'2023-06-01','anthropic-dangerous-direct-browser-access':'true'}},
        body:JSON.stringify({{model:'claude-haiku-4-5',max_tokens:350,system:Sys,messages:msgs}})
      }}).then(function(r){{return r.json();}}).then(function(d){{
        var ty=pdoc.getElementById('cw-ty');if(ty)ty.remove();
        var rep=(d.content&&d.content[0]&&d.content[0].text)?d.content[0].text:'Sorry, try again.';
        msgs.push({{role:'assistant',content:rep}});window.parent.__cwMsgs=msgs;bub('a',rep);
      }}).catch(function(){{
        var ty=pdoc.getElementById('cw-ty');if(ty)ty.remove();
        bub('a','Connection error. Please try again.');
      }}).finally(function(){{inp.disabled=snd.disabled=false;inp.focus();}});
    }}
  }}
  init();
}})();
</script>""", height=0, scrolling=False)
