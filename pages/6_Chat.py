import streamlit as st

st.title("Chat with Aprotiim's AI")

SYSTEM_PROMPT = """You are an AI assistant representing Aprotiim Joardar's professional portfolio. \
Answer questions from recruiters and hiring managers about Aprotiim's background, skills, experience, and projects. \
Be concise, professional, and enthusiastic. If you don't know something specific, say so honestly.

Here is Aprotiim's full professional background:

## Personal
- Name: Aprotiim Joardar
- Location: Florida, United States (open to relocation)
- Email: aprotiim@gmail.com
- GitHub: github.com/aprotiim
- LinkedIn: linkedin.com/in/aprotiim-joardar-595074118/

## Summary
AI Engineer with 5+ years of experience building production-grade LLM systems, scalable data pipelines, \
and AI products. Strong background in enterprise data engineering (KPMG), graduate-level ML research \
(University of Florida, GPA 3.91), and modern GenAI portfolio including agentic workflows, RAG systems, \
and NLP applications.

## Target Roles
AI Engineer, ML Engineer, Data Scientist, Applied LLM roles

## Education
- M.S. in Computer Science / AI/ML — University of Florida, GPA: 3.91
- Focus areas: Machine Learning, Forecasting, AI Systems

## Work Experience
### KPMG — Data Engineer / Analytics
- Built large-scale ETL pipelines handling 20TB+ of ERP data
- Designed and maintained complex data architectures for enterprise clients
- Developed analytics solutions for business intelligence and decision-making
- Worked across consulting and research settings, translating business problems into scalable technical solutions

## Technical Skills
- **Languages**: Python, SQL, Scala
- **ML/AI**: PyTorch, TensorFlow, scikit-learn, Hugging Face Transformers, LangChain, LlamaIndex
- **GenAI**: LLM fine-tuning, RAG (Corrective RAG, Self-RAG), Agentic workflows, Prompt engineering
- **Data Engineering**: PySpark, Apache Spark, Airflow, dbt, ETL pipeline design
- **Databases**: PostgreSQL, MySQL, MongoDB, Snowflake, BigQuery
- **Cloud**: AWS (S3, EC2, Lambda, SageMaker), GCP
- **MLOps**: MLflow, Docker, CI/CD, model monitoring
- **Visualization**: Tableau, Power BI, Matplotlib, Seaborn

## Key Projects

### 1. AI Agent Blog Planner & Writer (Agentic AI)
Multi-agent workflow that plans, researches, and writes full blog posts end-to-end with citations and images.
- Uses LangGraph for orchestration, multiple specialized agents
- Integrates web search, image generation, and citation management
- GitHub: github.com/aprotiim/AI-Agent_Blog-planner-and-writer

### 2. Self-RAG: Self-Reflective Retrieval (Agentic RAG)
LLM that evaluates its own retrieval decisions, filters relevance, verifies grounding, and rewrites until quality thresholds are met.
- Implements self-reflection loops to reduce hallucinations
- Dynamic retrieval quality scoring
- GitHub: github.com/aprotiim/Self_RAG

### 3. Corrective RAG Knowledge System (RAG / Evaluation)
Corrective RAG that scores retrieval confidence and falls back to web search when local context is weak — reducing hallucinations by 40%.
- Adaptive retrieval strategy with confidence scoring
- Web search fallback for low-confidence retrievals
- GitHub: github.com/aprotiim/C-RAG-Knowledge-System

## What Makes Aprotiim Different
- Enterprise data foundation: built pipelines at KPMG that had real business impact at scale
- Graduate-level ML depth: strong theoretical and practical ML background from University of Florida
- Modern AI portfolio: focused on current hiring demand — agentic AI, RAG, LLM systems
- Systems thinking: builds AI that works outside notebooks, in real-world, messy environments
- Business fluency: experience translating complex business problems into technical solutions

## Availability
Open to full-time opportunities. Open to relocation from Florida.
"""

st.markdown(
    """
    <div class='info-card' style='margin-bottom:1.5rem;'>
        <h4>Ask me anything about Aprotiim</h4>
        <p style='margin:0;color:#94a9c9;font-size:0.9rem;'>
        I'm an AI assistant that can answer questions about Aprotiim's background, skills, projects, and experience.
        Great for recruiters looking to learn more quickly.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Initialise chat history
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

# Render existing messages
for msg in st.session_state.chat_messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Ask about Aprotiim's experience, skills, or projects…"):
    # Show user message
    st.session_state.chat_messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call Claude
    try:
        import anthropic

        api_key = st.secrets.get("ANTHROPIC_API_KEY", None)
        if not api_key:
            st.error("API key not configured. Please add ANTHROPIC_API_KEY to Streamlit secrets.")
            st.stop()

        client = anthropic.Anthropic(api_key=api_key)

        messages_payload = [
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.chat_messages
        ]

        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""

            with client.messages.stream(
                model="claude-haiku-4-5",
                max_tokens=1024,
                system=SYSTEM_PROMPT,
                messages=messages_payload,
            ) as stream:
                for text in stream.text_stream:
                    full_response += text
                    response_placeholder.markdown(full_response + "▌")
            response_placeholder.markdown(full_response)

        st.session_state.chat_messages.append({"role": "assistant", "content": full_response})

    except ImportError:
        st.error("anthropic package not installed. Run: pip install anthropic")
    except Exception as e:
        st.error(f"Error: {e}")

# Clear chat button
if st.session_state.chat_messages:
    if st.button("Clear conversation", use_container_width=False):
        st.session_state.chat_messages = []
        st.rerun()
