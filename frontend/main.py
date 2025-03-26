# import streamlit as st
# from home import home_page
# from pcos_info import pcos_info_page
# from simple_risk_assessment import simple_risk_assessment_page
# from enhanced_risk_assessment import enhanced_risk_assessment_page
# from results import results_page
# from contact_help import contact_help_page

# hide_st_style = """
#     <style>
#         #MainMenu {visibility: hidden;}
#         footer {visibility: hidden;}
#         header {visibility: hidden;}
#         .stDeployButton {visibility: hidden !important;}
#     </style>
# """

# st.markdown(hide_st_style, unsafe_allow_html=True)

# def change_page(page):
#     st.session_state.page = page

# def navbar():
#     # Navbar with links that change the current page
#     st.markdown("""
#     <style>
#         /* Full-width navbar */
#         .navbar {
#             display: flex;
#             justify-content: space-around;
#             align-items: center;
#             background-color: #af84cf;  /* Updated color */
#             padding: 14px 0;
#             position: sticky;
#             top: 0;
#             width: 100%;
#             z-index: 10;
#             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#         }
#         .navbar a {
#             color: white;
#             text-decoration: none;
#             padding: 12px 16px;
#             font-size: 18px;
#             font-weight: bold;
#             border-radius: 4px;
#             transition: background-color 0.3s;
#         }
#         .navbar a:hover {
#             background-color: #9e66a3;  /* Slightly darker shade on hover */
#         }
#         .navbar a.active {
#             background-color: #9e66a3;  /* Active state color */
#         }
#     </style>
#     <div class="navbar">
#         <a href="#" onClick="change_page('Home')">Home</a>
#         <a href="#" onClick="change_page('PCOS Information')">PCOS Information</a>
#         <a href="#" onClick="change_page('Simple Risk Assessment')">Risk Assessment</a>
#         <a href="#" onClick="change_page('Enhanced Risk Assessment')">Enhanced Risk Assessment</a>
#         <a href="#" onClick="change_page('Your Results')">Your Results</a>
#         <a href="#" onClick="change_page('Help & Contact')">Help & Contact</a>
#     </div>
#     """, unsafe_allow_html=True)

# def main():
#     st.sidebar.title("Navigation")
#     pages = {
#         "Home": home_page,
#         "PCOS Information": pcos_info_page,
#         "Simple Risk Assessment": simple_risk_assessment_page,
#         "Enhanced Risk Assessment": enhanced_risk_assessment_page,
#         "Your Results": results_page,
#         "Help & Contact": contact_help_page,
#     }
    
#     if "page" not in st.session_state:
#         st.session_state.page = "Home"

#     navbar()
    
#     selected_page = st.sidebar.radio("Go to", list(pages.keys()), index=list(pages.keys()).index(st.session_state.page))
#     st.session_state.page = selected_page

#     # Run the selected page function
#     pages[selected_page]()

# if __name__ == "__main__":
#     main()

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

        /* Custom landscape layout */
        .block-container {
            max-width: 90% !important;  /* Set width to 100% */
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
