import streamlit as st
import os

logo_path = "images/logo.png" # App Logo

def home_page():
    col1, col2 = st.columns([1, 4]) 

    with col1:
        # Display the logo
        if os.path.exists(logo_path):
            st.image(logo_path, width=100)  
        else:
            st.error("Logo image not found.")

    with col2:
        st.title("PCOS Care")

    # Description and introductory text
    st.markdown("""
        Do you think you might have symptoms of **PCOS**?  
        Is your diagnosis taking longer than expected?  
        Are you looking for answers or guidance?  
        
        With **PCOS Care's Risk Assessment Tool**, you can get a quick prediction based on your health data and symptoms.  
        
        Understand your results, learn more about PCOS, and take the first step towards better health and informed decisions.  
        
        We're here to help you understand your health and wellness, so you can take action and seek the care you deserve.
        """)


    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True) # Section breaker

    # Features Overview Section
    st.subheader("Overview of the features")
    
    # Create columns for horizontal layout
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.image(logo_path, caption="PCOS Information", use_column_width=True)
        with st.expander("📚 PCOS Information"):
            st.markdown("""
            Learn about PCOS, its symptoms, causes, and management strategies.
            """)
    
    with col2:
        st.image(logo_path, caption="Simple Risk Assessment", use_column_width=True)
        with st.expander("⚠️ Simple Risk Assessment"):
            st.markdown("""
            Quickly assess your risk based on key symptoms.
            """)
    
    with col3:
        st.image(logo_path, caption="Enhanced Risk Assessment", use_column_width=True)
        with st.expander("🔍 Enhanced Risk Assessment"):
            st.markdown("""
            Provide more detailed health data for an in-depth risk evaluation.
            """)
    
    with col4:
        st.image(logo_path, caption="Results Visualization", use_column_width=True)
        with st.expander("📊 Results Visualization"):
            st.markdown("""
            View your risk level with intuitive graphs and visualizations.
            """)