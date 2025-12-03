import streamlit as st

from theme import inject_global_css

st.set_page_config(
    page_title="WAFR Accelerator | Home",
    page_icon="⚡",
    layout="wide",
)

if 'authenticated' not in st.session_state or not st.session_state['authenticated']:
    st.warning('You are not logged in. Please log in to access this page.')
    st.switch_page("pages/1_Login.py")

inject_global_css()

# Main content for the home page
st.markdown(
    """
    <div class="hero">
        <div class="pill">AWS Well-Architected · GenAI</div>
        <h1>Accelerate reviews with modern, guided workflows</h1>
        <p>
            This accelerator blends the AWS Well-Architected Framework with Generative AI to help you ship
            secure, resilient, and cost-optimized workloads faster.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(
        """
        <div class="glass-card metric-card">
            <span class="metric-title">Guided lenses</span>
            <span class="metric-value">5 pillars</span>
            <span class="metric-title">Security · Reliability · Cost · Performance · Ops</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        """
        <div class="glass-card metric-card">
            <span class="metric-title">AI assistance</span>
            <span class="metric-value">Context-aware</span>
            <span class="metric-title">Recommendations tuned to your inputs</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col3:
    st.markdown(
        """
        <div class="glass-card metric-card">
            <span class="metric-title">Collaboration</span>
            <span class="metric-value">Team-ready</span>
            <span class="metric-title">Share insights and iterate quickly</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

st.subheader("What you can do")
st.markdown(
    """
    <div class="card-grid">
        <div class="glass-card">
            <h3>✨ Launch new reviews</h3>
            <p>Kick off a Well-Architected review with pre-built prompts, guardrails, and example artifacts.</p>
        </div>
        <div class="glass-card">
            <h3>🔍 Explore prior sessions</h3>
            <p>Surface existing WAFR work, reuse findings, and keep team members aligned on action items.</p>
        </div>
        <div class="glass-card">
            <h3>📊 Visualize architecture</h3>
            <p>Understand the end-to-end accelerator design and how each component strengthens your stack.</p>
        </div>
        <div class="glass-card">
            <h3>🛡️ Operationalize controls</h3>
            <p>Apply recommendations for resilience, observability, and security as code.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

cta_col1, cta_col2 = st.columns([1.2, 1])
with cta_col1:
    st.markdown("### Ready to dive in?")
    st.write(
        "Use the navigation to start a new Well-Architected review or explore the accelerator architecture for a clear mental model.")

with cta_col2:
    if st.button("View the architecture", type="primary", use_container_width=True):
        st.switch_page("pages/3_System_Architecture.py")
    st.button("Return to login", use_container_width=True, on_click=lambda: st.switch_page("pages/1_Login.py"))


# Logout function
def logout():
    st.session_state['authenticated'] = False
    st.session_state.pop('username', None)
    st.rerun()

# Add logout button in sidebar
if st.sidebar.button('Logout'):
    logout()
