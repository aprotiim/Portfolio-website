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

# ── Floating Chat Widget ───────────────────────────────────────────────────────
try:
    _API_KEY = st.secrets.get("ANTHROPIC_API_KEY", "")
except Exception:
    _API_KEY = ""

_SYSTEM = (
    "You are an AI assistant representing Aprotiim Joardar's professional portfolio. "
    "Answer recruiter and hiring manager questions concisely and professionally. "
    "Keep answers under 120 words unless a detailed answer is clearly needed.\n\n"
    "ABOUT APROTIIM:\n"
    "- AI Engineer, 5+ years experience. Ex-KPMG. University of Florida MS (GPA 3.91).\n"
    "- Location: Florida, USA — open to relocation.\n"
    "- Contact: aprotiim@gmail.com | github.com/aprotiim | linkedin.com/in/aprotiim-joardar-595074118/\n\n"
    "TARGET ROLES: AI Engineer, ML Engineer, Data Scientist, Applied LLM roles.\n\n"
    "EDUCATION: M.S. Computer Science / AI-ML — University of Florida, GPA 3.91.\n\n"
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
    "Builds AI that works in production, not just notebooks. Strong business and technical fluency.\n\n"
    "AVAILABILITY: Open to full-time roles. Open to relocation."
)

_CSS = (
    "#cw-root{position:fixed;top:80px;right:24px;z-index:2147483647;"
    "font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;}"

    "#cw-btn{width:56px;height:56px;border-radius:50%;"
    "background:linear-gradient(135deg,#0e7490,#6d28d9);border:none;cursor:pointer;"
    "box-shadow:0 4px 24px rgba(110,231,249,.4);transition:transform .2s,box-shadow .2s;"
    "display:flex;align-items:center;justify-content:center;font-size:22px;color:#fff;"
    "margin-left:auto;}"
    "#cw-btn:hover{transform:scale(1.09);box-shadow:0 6px 32px rgba(110,231,249,.55);}"

    "#cw-panel{position:absolute;top:68px;right:0;width:340px;height:490px;"
    "background:rgba(8,14,36,.97);border:1px solid rgba(148,163,184,.18);border-radius:18px;"
    "box-shadow:0 20px 64px rgba(0,0,0,.65);display:flex;flex-direction:column;overflow:hidden;"
    "transform:scale(.88) translateY(-14px);opacity:0;pointer-events:none;"
    "transition:transform .28s cubic-bezier(.34,1.56,.64,1),opacity .2s;"
    "transform-origin:top right;}"
    "#cw-panel.open{transform:scale(1) translateY(0);opacity:1;pointer-events:all;}"

    "#cw-header{padding:13px 14px;"
    "background:linear-gradient(135deg,rgba(14,116,144,.22),rgba(109,40,217,.22));"
    "border-bottom:1px solid rgba(148,163,184,.11);display:flex;align-items:center;"
    "gap:10px;flex-shrink:0;}"
    ".cw-av{width:34px;height:34px;border-radius:50%;"
    "background:linear-gradient(135deg,#0e7490,#6d28d9);"
    "display:flex;align-items:center;justify-content:center;font-size:15px;flex-shrink:0;}"
    ".cw-ti{flex:1;}"
    ".cw-ti strong{display:block;color:#e5eefb;font-size:.85rem;font-weight:600;}"
    ".cw-ti span{color:#6ee7f9;font-size:.7rem;}"
    "#cw-x{background:none;border:none;color:#94a9c9;cursor:pointer;font-size:17px;"
    "padding:3px 7px;border-radius:6px;line-height:1;transition:background .15s,color .15s;}"
    "#cw-x:hover{background:rgba(148,163,184,.12);color:#e5eefb;}"

    "#cw-msgs{flex:1;overflow-y:auto;padding:12px 10px;display:flex;flex-direction:column;"
    "gap:8px;scrollbar-width:thin;scrollbar-color:rgba(148,163,184,.15) transparent;}"
    "#cw-msgs::-webkit-scrollbar{width:4px;}"
    "#cw-msgs::-webkit-scrollbar-thumb{background:rgba(148,163,184,.15);border-radius:4px;}"

    ".cw-m{max-width:85%;padding:8px 11px;border-radius:12px;font-size:.81rem;"
    "line-height:1.55;word-wrap:break-word;white-space:pre-wrap;}"
    ".cw-u{background:linear-gradient(135deg,rgba(14,116,144,.65),rgba(109,40,217,.55));"
    "color:#e5eefb;align-self:flex-end;border-bottom-right-radius:3px;}"
    ".cw-a{background:rgba(22,34,64,.9);color:#c8d8f0;"
    "border:1px solid rgba(148,163,184,.1);align-self:flex-start;border-bottom-left-radius:3px;}"
    ".cw-welcome{background:rgba(110,231,249,.05);border:1px solid rgba(110,231,249,.12);"
    "color:#7a99bb;align-self:center;text-align:center;font-size:.77rem;"
    "max-width:95%;border-radius:10px;}"

    ".cw-typing{display:flex;gap:5px;align-items:center;padding:10px 14px !important;}"
    ".cw-typing span{width:7px;height:7px;border-radius:50%;background:#6ee7f9;"
    "animation:cwBounce 1.3s infinite;opacity:.55;}"
    ".cw-typing span:nth-child(2){animation-delay:.2s;}"
    ".cw-typing span:nth-child(3){animation-delay:.4s;}"
    "@keyframes cwBounce{0%,60%,100%{transform:translateY(0);opacity:.55;}"
    "30%{transform:translateY(-5px);opacity:1;}}"

    "#cw-foot{padding:9px 10px;border-top:1px solid rgba(148,163,184,.1);"
    "display:flex;gap:7px;align-items:center;background:rgba(5,10,28,.5);flex-shrink:0;}"
    "#cw-inp{flex:1;background:rgba(22,34,64,.7);border:1px solid rgba(148,163,184,.18);"
    "border-radius:10px;padding:8px 11px;color:#e5eefb;font-size:.81rem;outline:none;"
    "transition:border-color .2s;}"
    "#cw-inp::placeholder{color:#4a6280;}"
    "#cw-inp:focus{border-color:rgba(110,231,249,.38);background:rgba(22,34,64,.95);}"
    "#cw-snd{width:34px;height:34px;border-radius:9px;"
    "background:linear-gradient(135deg,#0e7490,#6d28d9);border:none;color:#fff;"
    "cursor:pointer;font-size:16px;display:flex;align-items:center;justify-content:center;"
    "flex-shrink:0;transition:opacity .2s,transform .15s;}"
    "#cw-snd:hover{opacity:.85;transform:scale(1.06);}"
    "#cw-snd:disabled{opacity:.35;cursor:not-allowed;transform:none;}"

    "@media(max-width:420px){"
    "#cw-panel{width:calc(100vw - 32px);right:-4px;height:430px;top:68px;}"
    "}"
)

_JS = f"""
(function(){{
  var par = window.parent.document;
  if(par.getElementById('cw-root')) return;

  var KEY = {json.dumps(_API_KEY)};
  var SYS = {json.dumps(_SYSTEM)};
  var CSS = {json.dumps(_CSS)};
  var hist = [];

  var s = par.createElement('style');
  s.textContent = CSS;
  par.head.appendChild(s);

  var root = par.createElement('div');
  root.id = 'cw-root';
  root.innerHTML = `
    <div id="cw-panel">
      <div id="cw-header">
        <div class="cw-av">🤖</div>
        <div class="cw-ti">
          <strong>Ask about Aprotiim</strong>
          <span>● AI Portfolio Assistant</span>
        </div>
        <button id="cw-x">✕</button>
      </div>
      <div id="cw-msgs">
        <div class="cw-m cw-welcome">
          Hi! Ask me anything about Aprotiim's experience, skills, or projects. 👋
        </div>
      </div>
      <div id="cw-foot">
        <input id="cw-inp" type="text" placeholder="Ask a question…" autocomplete="off"/>
        <button id="cw-snd">↑</button>
      </div>
    </div>
    <button id="cw-btn" title="Chat with Aprotiim's AI">💬</button>
  `;
  par.body.appendChild(root);

  par.getElementById('cw-btn').onclick = toggle;
  par.getElementById('cw-x').onclick   = toggle;
  par.getElementById('cw-snd').onclick  = doSend;
  par.getElementById('cw-inp').onkeydown = function(e){{
    if(e.key === 'Enter' && !e.shiftKey){{ e.preventDefault(); doSend(); }}
  }};

  function toggle(){{
    var panel = par.getElementById('cw-panel');
    var btn   = par.getElementById('cw-btn');
    var open  = panel.classList.toggle('open');
    btn.textContent = open ? '✕' : '💬';
    if(open) setTimeout(function(){{ par.getElementById('cw-inp').focus(); }}, 280);
  }}

  async function doSend(){{
    var inp = par.getElementById('cw-inp');
    var snd = par.getElementById('cw-snd');
    var txt = inp.value.trim();
    if(!txt || snd.disabled) return;
    inp.value = '';
    snd.disabled = true;
    addMsg('u', txt);
    hist.push({{role:'user', content:txt}});
    var typ = addTyping();
    try{{
      var res = await fetch('https://api.anthropic.com/v1/messages', {{
        method: 'POST',
        headers: {{
          'x-api-key': KEY,
          'anthropic-version': '2023-06-01',
          'anthropic-dangerous-direct-browser-access': 'true',
          'content-type': 'application/json'
        }},
        body: JSON.stringify({{
          model: 'claude-haiku-4-5',
          max_tokens: 512,
          system: SYS,
          messages: hist
        }})
      }});
      typ.remove();
      if(res.ok){{
        var d = await res.json();
        var reply = d.content[0].text;
        addMsg('a', reply);
        hist.push({{role:'assistant', content:reply}});
      }} else {{
        addMsg('a', 'Sorry, something went wrong. Please try again.');
      }}
    }} catch(e){{
      typ.remove();
      addMsg('a', 'Connection error. Please try again.');
    }}
    snd.disabled = false;
    inp.focus();
  }}

  function addMsg(role, text){{
    var c = par.getElementById('cw-msgs');
    var d = par.createElement('div');
    d.className = 'cw-m cw-' + role;
    d.textContent = text;
    c.appendChild(d);
    c.scrollTop = c.scrollHeight;
    return d;
  }}

  function addTyping(){{
    var c = par.getElementById('cw-msgs');
    var d = par.createElement('div');
    d.className = 'cw-m cw-a cw-typing';
    d.innerHTML = '<span></span><span></span><span></span>';
    c.appendChild(d);
    c.scrollTop = c.scrollHeight;
    return d;
  }}
}})();
"""

components.html(f"<script>{_JS}</script>", height=0)
