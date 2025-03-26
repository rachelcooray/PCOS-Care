import streamlit as st
from home import home_page
from pcos_info import pcos_info_page
from simple_risk_assessment import simple_risk_assessment_page
from enhanced_risk_assessment import enhanced_risk_assessment_page
from results import results_page
from contact_help import contact_help_page

hide_st_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {visibility: hidden !important;}
    </style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)

def navbar():
    # Navbar with links that change the current page
    st.markdown("""
    <style>
        /* Full-width navbar */
        .navbar {
            display: flex;
            justify-content: space-around;
            align-items: center;
            background-color: #af84cf;  /* Updated color */
            padding: 14px 0;
            position: sticky;
            top: 0;
            width: 100%;
            z-index: 10;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .navbar a {
            color: white;
            text-decoration: none;
            padding: 12px 16px;
            font-size: 18px;
            font-weight: bold;
            border-radius: 4px;
            transition: background-color 0.3s;
        }
        .navbar a:hover {
            background-color: #9e66a3;  /* Slightly darker shade on hover */
        }
        .navbar a.active {
            background-color: #9e66a3;  /* Active state color */
        }
    </style>
    <div class="navbar">
        <a href="#" onclick="window.location.href = '/';">Home</a>
        <a href="#" onclick="window.location.href = '/pcos_info';">PCOS Information</a>
        <a href="#" onclick="window.location.href = '/simple_risk_assessment';">Risk Assessment</a>
        <a href="#" onclick="window.location.href = '/enhanced_risk_assessment';">Enhanced Risk Assessment</a>
        <a href="#" onclick="window.location.href = '/results';">Your Results</a>
        <a href="#" onclick="window.location.href = '/contact';">Help & Contact</a>
    </div>
    """, unsafe_allow_html=True)

def main():
    st.sidebar.title("Navigation")
    pages = {
        "Home": home_page,
        "PCOS Information": pcos_info_page,
        "Simple Risk Assessment": simple_risk_assessment_page,
        "Enhanced Risk Assessment": enhanced_risk_assessment_page,
        "Your Results": results_page,
        "Help & Contact": contact_help_page,
    }
    
    if "page" not in st.session_state:
        st.session_state.page = "Home"

    navbar()
    
    selected_page = st.sidebar.radio("Go to", list(pages.keys()), index=list(pages.keys()).index(st.session_state.page))
    st.session_state.page = selected_page

    # Run the selected page function
    pages[selected_page]()

if __name__ == "__main__":
    main()