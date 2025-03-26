import streamlit as st
from streamlit_option_menu import option_menu
from home import home_page
from pcos_info import pcos_info_page
from simple_risk_assessment import simple_risk_assessment_page
from enhanced_risk_assessment import enhanced_risk_assessment_page
from results import results_page
from contact_help import contact_help_page

# Function to hide default Streamlit UI components
hide_st_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {visibility: hidden !important;}
        
        /* Custom responsive layout */
        .block-container {
            max-width: 100% !important;  /* Set width to 100% */
            padding-left: 2rem !important;
            padding-right: 2rem !important;
        }

        /* Adjust the layout for mobile and tablet screens */
        .main {
            max-width: 100% !important;
            padding: 0 !important;
        }

        /* Sidebar responsiveness */
        .css-1d391kg {
            max-width: 300px;  /* You can adjust this for more space on desktop */
        }

        /* Responsive Navbar */
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

        /* Hamburger Menu Styling */
        .navbar-toggler {
            display: none;
        }

        /* Media Queries for different screen sizes */
        @media (max-width: 768px) {
            .block-container {
                padding-left: 1rem !important;
                padding-right: 1rem !important;
            }

            /* Mobile: Stack items vertically */
            .navbar {
                flex-direction: column;
                align-items: center;
                padding: 15px;
            }

            .navbar .navbar-nav {
                display: flex;
                flex-direction: column;
                align-items: center;
                width: 100%;
                display: none;  /* Initially hide the menu on small screens */
            }

            .navbar .navbar-nav.active {
                display: block;  /* Show the menu when it's toggled */
            }

            .navbar a {
                margin-bottom: 10px;
                font-size: 18px;
            }

            /* Hamburger icon */
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
            .block-container {
                padding-left: 0.5rem !important;
                padding-right: 0.5rem !important;
            }

            /* Mobile: Adjust menu item font size for small screens */
            .navbar a {
                font-size: 16px;
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
