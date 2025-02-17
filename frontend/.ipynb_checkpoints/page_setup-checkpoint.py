import streamlit as st

home_page = st.Page(
    page="pages/home.py",
    title="Home",
    icon=":material/home:",
    default=True,
)

pcos_info_page = st.Page(
    page="pages/pcos_info.py",
    title="PCOS Information",
    icon=":material/info:",
)

simple_risk_assessment_page = st.Page(
    page="pages/simple_risk_assessment.py",
    title="Simple Risk Assessment",
    icon=":material/assessment:",
)

enhanced_risk_assessment_page = st.Page(
    page="pages/enhanced_risk_assessment.py",
    title="Enhanced Risk Assessment",
    icon=":material/analytics:",
)

results_page = st.Page(
    page="pages/results.py",
    title="Results Visualization",
    icon=":material/leaderboard:",
)

contact_help_page = st.Page(
    page="pages/contact_help.py",
    title="Contact/Help",
    icon=":material/help:",
)
