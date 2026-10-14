import streamlit as st

from theme import inject_global_css

st.set_page_config(
    page_title="WAFR Accelerator | Architecture",
    page_icon="🧭",
    layout="wide",
)

if 'authenticated' not in st.session_state or not st.session_state['authenticated']:
    st.warning('You are not logged in. Please log in to access this page.')
    st.switch_page("pages/1_Login.py")

inject_global_css()


def architecture():
    st.markdown(
        """
        <div class="hero">
            <div class="pill">Architecture Overview</div>
            <h1>Secure, observable, and AI-powered by design</h1>
            <p>Explore how the accelerator ties together Streamlit, AWS services, and Amazon Bedrock to deliver guided Well-Architected reviews.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.image("sys-arch.png", use_container_width=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.subheader("Key components")
    st.markdown(
        """
        <div class="card-grid">
            <div class="glass-card">
                <h3>🎨 Frontend</h3>
                <p>Streamlit UI with modern theming, intuitive navigation, and contextual actions for reviews and architecture insights.</p>
            </div>
            <div class="glass-card">
                <h3>🧠 Bedrock + OpenSearch</h3>
                <p>Context-aware prompts use a secure Amazon OpenSearch Serverless knowledge base to ground Amazon Bedrock generations.</p>
            </div>
            <div class="glass-card">
                <h3>📦 Backend services</h3>
                <p>Python-based services coordinate WAFR flows, integrate AWS Well-Architected Tool APIs, and orchestrate data retrieval.</p>
            </div>
            <div class="glass-card">
                <h3>🔒 Identity & governance</h3>
                <p>Amazon Cognito enables user management while AWS IAM policies constrain access to review data and knowledge sources.</p>
            </div>
            <div class="glass-card">
                <h3>🗂️ Data layer</h3>
                <p>Amazon DynamoDB stores review artifacts and operational metadata with serverless scale, high availability, and low latency.</p>
            </div>
            <div class="glass-card">
                <h3>📈 Observability</h3>
                <p>CloudWatch metrics, structured logs, and distributed tracing enable fast root-cause analysis and operational excellence.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div class="glass-card metric-card">
                <span class="metric-title">Resilience posture</span>
                <span class="metric-value">Multi-AZ, serverless-first</span>
                <p>Critical components avoid single points of failure and lean on managed services for durability.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class="glass-card metric-card">
                <span class="metric-title">Security stance</span>
                <span class="metric-value">Least privilege</span>
                <p>Scoped IAM roles, encrypted data stores, and Cognito-managed identities keep workloads isolated.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.markdown(
        """
        ### Operational guidance
        - Prioritize automated checks for missing configuration (env vars, API tokens, knowledge base identifiers).
        - Capture structured audit logs around user actions (review creation, knowledge base queries, and recommendations).
        - Use feature flags or configuration profiles to keep optional integrations discoverable and maintainable.
        - Continuously validate event payloads and fall back gracefully when upstream services are slow or unavailable.
        """
    )


if __name__ == "__main__":
    architecture()


# Logout function
def logout():
    st.session_state['authenticated'] = False
    st.session_state.pop('username', None)
    st.rerun()

# Add logout button in sidebar
if st.sidebar.button('Logout'):
    logout()
