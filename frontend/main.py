import streamlit as st
from streamlit_navigation_bar import st_navbar
from home import home_page
from pcos_info import pcos_info_page
from simple_risk_assessment import simple_risk_assessment_page
from enhanced_risk_assessment import enhanced_risk_assessment_page
from results import results_page
from contact_help import contact_help_page

hide_st_style = """
    <style>
        /* Hide default Streamlit UI components */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {visibility: hidden !important;}

        /* Apply Poppins font globally */
        * {
            font-family: "Poppins", sans-serif !important;
        }

        /* Custom landscape layout */
        .block-container {
            max-width: 90% !important;  /* Set width to 90% */
            padding-left: 2rem !important;
            padding-right: 2rem !important;
        }

        /* Adjust width for the entire app */
        .main {
            max-width: 100% !important;
            padding: 0 !important;
            margin-top: 0;  /* Reset any previous margins */
        }
    </style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)

# Define pages and custom styles for the navbar
pages = ["Home", "PCOS Information", "Simple Risk Assessment", "Enhanced Risk Assessment", "Your Results", "Help & Contact"]

styles = {
    "nav": {
        "background-color": "rgb(170, 124, 207)",  # Purple background for the navbar
        "height": "75px",
    },
    "div": {
        "max-width": "32rem",  # Adjust the width if needed
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(97, 59, 156)",  # Purple text color for the navbar links
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(170, 124, 207, 0.6)",  # Lighter purple background when active
        "color": "white",  # White text when active
    },
    "hover": {
        "background-color": "rgba(170, 124, 207, 0.4)",  # Light purple background when hovered
        "color": "white",
    },
}

# Create the navigation bar
page = st_navbar(pages, styles=styles)

# Display the selected page based on the navbar
if page == "Home":
    home_page()
elif page == "PCOS Information":
    pcos_info_page()
elif page == "Simple Risk Assessment":
    simple_risk_assessment_page()
elif page == "Enhanced Risk Assessment":
    enhanced_risk_assessment_page()
elif page == "Your Results":
    results_page()
elif page == "Help & Contact":
    contact_help_page()








