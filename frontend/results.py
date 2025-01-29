import streamlit as st
import os

logo_path = "images/logo.png"

def results_page():
    col1, col2 = st.columns([1, 4]) 

    with col1:
        if os.path.exists(logo_path):
            st.image(logo_path, width=100)  
        else:
            st.error("Logo image not found.")

    with col2:
        st.title("APP NAME")
        
    st.subheader("Results")
    st.markdown("""
    View your PCOS risk assessment results here.  
    Graphs and visualizations will help you understand your health profile.
    """)

    # Display the collected data (JSON format)
    if "risk_assessment_data" in st.session_state:
        st.markdown("#### Your Submitted Data:")
        st.json(st.session_state.risk_assessment_data)

    else:
        st.error("No risk assessment data found. Please complete the assessment first.")

    # Section breaker
    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    # TO DE DONE
    # Example result visualization
    st.line_chart([1, 2, 3, 4, 5])  # Example chart for risk assessment

    st.dataframe({
        "Symptoms": ["Irregular Periods", "Excessive Hair", "Acne"],
        "Risk Level": ["High", "Low", "Moderate"]
    })