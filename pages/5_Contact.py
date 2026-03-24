from pathlib import Path

import streamlit as st

st.title("Contact")

ROOT = Path(__file__).resolve().parents[1]

col1, col2 = st.columns([1.2, 1], gap="large")

with col1:
    st.markdown(
        """
        <div class='hero-card'>
            <div class='available-badge'>
                <span class='available-dot'></span>
                Open to full-time opportunities
            </div>
            <div class='eyebrow'>Let's connect</div>
            <h2 class='hero-title'>I'm looking for opportunities where I can build high-impact AI and data products.</h2>
            <p class='hero-subtitle'>
            I'm especially interested in AI engineer, ML engineer, data scientist, and applied LLM roles where strong systems thinking and practical execution matter.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='section-card'>
            <h3>Best ways to reach me</h3>
            <p><strong>Email:</strong> <a href='mailto:aprotiim@gmail.com'>aprotiim@gmail.com</a></p>
            <p><strong>Phone:</strong> +1 352-709-5368</p>
            <p><strong>GitHub:</strong> <a href='https://github.com/aprotiim' target='_blank'>github.com/aprotiim</a></p>
            <p><strong>LinkedIn:</strong> <a href='https://www.linkedin.com/in/aprotiim-joardar-595074118/' target='_blank'>linkedin.com/in/aprotiim-joardar</a></p>
            <p><strong>Location:</strong> Florida, United States <span style='color:#94a9c9;font-size:0.88rem;'>(Open to relocation)</span></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class='info-card'>
            <h4>Recruiter quick note</h4>
            <p>
            This portfolio is intentionally built to make my story easy to remember:
            enterprise data foundation, graduate-level ML depth, and a modern AI portfolio aligned with current hiring demand.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    resume_path = ROOT / "assets" / "APROTIIM_JOARDAR_AI_ML_Engineer_final.pdf"
    if resume_path.exists():
        with open(resume_path, "rb") as f:
            st.download_button(
                label="📄 Download Resume",
                data=f,
                file_name="Aprotiim_Joardar_AI_Engineer.pdf",
                mime="application/pdf",
                use_container_width=True,
            )

    with st.form("contact_form"):
        st.text_input("Name")
        st.text_input("Email")
        st.text_area("Message", height=180)
        st.form_submit_button("Send")
