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

        /* Adjust the sidebar to take more space */
        .css-1d391kg {
            max-width: 300px;  /* Adjust sidebar width */
        }

        /* Horizontal Navigation Bar */
        .navbar {
            display: flex;
            justify-content: space-between;
            background-color: #ac7ccf;
            padding: 10px;
            position: -webkit-sticky; /* For Safari */
            position: sticky;  /* Make navbar sticky */
            top: 0;  /* Stick it to the top when scrolling */
            left: 0;
            width: 100%;
            height: 60px;  /* Set a fixed height for the navbar */
            z-index: 1000;  /* Ensure it stays above other elements */
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Add a subtle shadow */
        }

        .navbar a {
            color: white;
            text-decoration: none;
            font-size: 18px;
            margin-right: 20px;
            font-family: "Poppins", sans-serif !important;
        }

        /* Global font size for readability */
        body {
            font-size: 20px;
            line-height: 1.6;
            font-family: "Poppins", sans-serif !important;
        }

        /* Ensure navigation items have correct font */
        .nav-link, .nav-link-selected {
            font-family: "Poppins", sans-serif !important;
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
                "border": "none",
                "display": "flex",  # Ensures even spacing
                "align-items": "center"  # Aligns items properly
            },
            "icon": {
                "color": "#c19edb",  # Soft purple color for icons
                "font-size": "25px"
            },
            "nav-link": {
                "font-size": "18px", 
                "text-align": "center",
                "margin": "0px",
                "padding": "12px 24px",  # Adjust padding to ensure full height
                "border-radius": "8px",  # Rounded corners
                "color": "#ac7ccf",  # Soft purple color for text
                "display": "flex",
                "align-items": "center",
                "justify-content": "center",
                "height": "100%"  # Ensure full height coverage
            },
            "nav-link-selected": {
                "font-family": "Poppins, sans-serif",
                "background-color": "#ac7ccf",  # Soft purple for selected item
                "color": "white",  # Text color for selected item
                "border-radius": "8px",  # Rounded edges
                "padding": "12px 24px",  # Adjusted padding for full height
                "display": "flex",
                "align-items": "center",
                "justify-content": "center",
                "height": "100%",  # Ensures full coverage
                "width": "100%"  # Ensures full button width
            },
        }
    )

    # Update session state to the selected page
    st.session_state.page = selected

    # Call the corresponding page function based on the session state
    pages[selected]()

if __name__ == "__main__":
    main()
