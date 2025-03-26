import streamlit as st
from streamlit_option_menu import option_menu
from home import home_page
from pcos_info import pcos_info_page
from simple_risk_assessment import simple_risk_assessment_page
from enhanced_risk_assessment import enhanced_risk_assessment_page
from results import results_page
from contact_help import contact_help_page

# Hide default Streamlit UI components and custom styling
hide_st_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {visibility: hidden !important;}

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
        }

        /* Adjust the sidebar to take more space */
        .css-1d391kg {
            max-width: 300px;  /* You can adjust this for more space */
        }

        /* Horizontal Navigation Bar */
        .navbar {
            display: flex;
            justify-content: space-between;
            background-color: #ac7ccf;
            padding: 10px;
        }

        .navbar a {
            color: white;
            text-decoration: none;
            font-size: 18px;
            margin-right: 20px;
        }

        /* Media Queries for different screen sizes */
        @media (max-width: 768px) {
            .navbar {
                flex-direction: column;
                align-items: flex-start;
            }

            .navbar a {
                padding: 10px 0;
                font-size: 16px;
            }

            /* Mobile menu toggle button */
            .navbar-toggler {
                display: block;
                background-color: #ac7ccf;
                color: white;
                border: none;
                font-size: 25px;
                padding: 10px;
                cursor: pointer;
            }
        }

        @media (max-width: 480px) {
            /* For very small screens (phones) */
            .navbar a {
                font-size: 14px;
                padding: 8px 0;
            }

            .navbar .navbar-nav {
                display: flex;
                flex-direction: column;
                align-items: center;
                width: 100%;
                display: none;
            }

            .navbar .navbar-nav.active {
                display: block;
            }
        }
    </style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)

def main():
    # Sidebar for page navigation
    pages = {
        "Home": home_page,
        "PCOS Information": pcos_info_page,
        "Simple Risk Assessment": simple_risk_assessment_page,
        "Enhanced Risk Assessment": enhanced_risk_assessment_page,
        "Your Results": results_page,
        "Help & Contact": contact_help_page,
    }

    # Initialize session state for pages
    if "page" not in st.session_state:
        st.session_state.page = "Home"

    # Horizontal menu with custom styling
    selected = option_menu(
        menu_title=None,  # No title
        options=["Home", "PCOS Information", "Simple Risk Assessment", "Enhanced Risk Assessment", "Your Results", "Help & Contact"],
        icons=["house", "book", "calculator", "bar-chart", "clipboard", "question-circle"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",  # Horizontal layout
        styles={
            "container": {
                "padding": "0!important", 
                "background-color": "#f0f0f0",  # Light background color
                "border": "none"
            },
            "icon": {
                "color": "#ac7ccf",  # Soft purple color for icons
                "font-size": "25px"
            },
            "nav-link": {
                "font-size": "18px", 
                "text-align": "left",
                "margin": "0px",
                "color": "#ac7ccf",  # Soft purple color for text
            },
            "nav-link-selected": {
                "background-color": "#ac7ccf",  # Soft purple for selected item
                "color": "white"  # Text color for selected item
            },
        }
    )

    # Update session state to the selected page
    st.session_state.page = selected

    # Call the corresponding page function based on the session state
    pages[selected]()

if __name__ == "__main__":
    main()
