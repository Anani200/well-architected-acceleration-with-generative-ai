import streamlit as st


def inject_global_css():
    st.markdown(
        """
        <style>
        :root {
            --page-bg: linear-gradient(135deg, #0f172a 0%, #111827 50%, #0b1324 100%);
            --card-bg: rgba(255, 255, 255, 0.03);
            --card-border: rgba(255, 255, 255, 0.08);
            --text-color: #e5e7eb;
            --muted: #94a3b8;
            --accent: #22c55e;
            --accent-strong: #34d399;
        }

        .stApp {
            background: var(--page-bg);
            color: var(--text-color);
        }

        .block-container {
            padding: 2.5rem 2rem 3rem;
            max-width: 1100px;
        }

        h1, h2, h3, h4, h5, h6 {
            color: #f8fafc;
            letter-spacing: -0.02em;
        }

        p, li, span, label, .stMarkdown {
            color: var(--text-color);
        }

        .pill {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            padding: 0.35rem 0.8rem;
            background: rgba(52, 211, 153, 0.12);
            border: 1px solid rgba(52, 211, 153, 0.35);
            border-radius: 999px;
            color: #bbf7d0;
            font-weight: 600;
            font-size: 0.85rem;
        }

        .hero {
            padding: 1.5rem 1.5rem;
            background: linear-gradient(120deg, rgba(34, 197, 94, 0.12), rgba(59, 130, 246, 0.12));
            border: 1px solid var(--card-border);
            border-radius: 18px;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.35);
        }

        .hero h1 {
            margin: 0.4rem 0 0.5rem;
            font-size: 2.1rem;
        }

        .hero p {
            color: var(--muted);
            margin-bottom: 1rem;
            font-size: 1.05rem;
        }

        .glass-card {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 16px;
            padding: 1.1rem 1rem;
            box-shadow: 0 12px 26px rgba(0, 0, 0, 0.25);
        }

        .metric-card {
            display: flex;
            flex-direction: column;
            gap: 0.35rem;
        }

        .metric-title {
            color: var(--muted);
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }

        .metric-value {
            font-size: 1.6rem;
            font-weight: 700;
        }

        .card-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 1rem;
        }

        .card-grid .glass-card h3 {
            margin: 0.4rem 0 0.35rem;
        }

        .card-grid .glass-card p {
            margin: 0;
            color: var(--muted);
        }

        .action-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.4rem;
            padding: 0.55rem 1.1rem;
            border-radius: 12px;
            background: linear-gradient(135deg, #22c55e, #16a34a);
            color: #0b1324 !important;
            text-decoration: none;
            font-weight: 700;
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 8px 24px rgba(34, 197, 94, 0.35);
        }

        .secondary-btn {
            background: rgba(255, 255, 255, 0.04);
            color: #e5e7eb !important;
            border: 1px solid var(--card-border);
            box-shadow: none;
        }

        .divider {
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            margin: 1.5rem 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
