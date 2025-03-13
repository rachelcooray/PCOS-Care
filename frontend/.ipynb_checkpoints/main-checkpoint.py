import streamlit as st
from home import home_page
from pcos_info import pcos_info_page
from simple_risk_assessment import simple_risk_assessment_page
from enhanced_risk_assessment import enhanced_risk_assessment_page
from results import results_page
from contact_help import contact_help_page

hide_st_style = “”"

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

“”"
st.markdown(hide_st_style, unsafe_allow_html=True)

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
    
    selected_page = st.sidebar.radio("Go to", list(pages.keys()), index=list(pages.keys()).index(st.session_state.page))
    st.session_state.page = selected_page

    # Run the selected page function
    pages[selected_page]()

if __name__ == "__main__":
    main()