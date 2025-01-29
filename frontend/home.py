import streamlit as st
import os

logo_path = "images/logo.png"  # App Logo

def home_page():
    # Layout for logo and title
    col1, col2 = st.columns([1, 4]) 

    with col1:
        # Display the logo
        if os.path.exists(logo_path):
            st.image(logo_path, width=100)  
        else:
            st.error("Logo image not found.")

    with col2:
        st.title("PCOS Care")

    # Welcome Message
    st.markdown(
        "<h2 style='text-align: center; color: #6a0dad;'>Empowering Women’s Health with AI-Driven Insights!</h2>", 
        unsafe_allow_html=True
    )

    # Introduction
    st.markdown("""
        ### Welcome to PCOS Care  
        Our AI-driven **PCOS Risk Assessment tool** helps women understand their health better through data-driven insights.  
        This tool **does not provide a medical diagnosis**, but it serves as an informative resource.  
        
        💡 **Early detection and awareness are key to managing PCOS effectively.**  
        📌 **Use this platform to assess your risk, gain knowledge, and take informed actions.**  
        
        _Always consult a healthcare professional for medical advice._  
    """)

    # Call to Action
    st.markdown(
        "<h3 style='text-align: center;'>Start your journey towards better health!</h3>", 
        unsafe_allow_html=True
    )

    # Navigation Buttons
    col1, col2 = st.columns(2)

    # with col1:
    #     if st.button("📚 Learn More About PCOS"):
    #         st.switch_page("PCOS_Info") 

    # with col2:
    #     if st.button("⚠️ Take the Risk Assessment"):
    #         st.switch_page("simple_risk_assessment_page")  

    # Engaging Visuals - Hero Section
    st.image("images/logo.png", use_column_width=True, caption="Take Control of Your Health")  # Replace with an actual image

    # Section Breaker
    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)  

    # Features Overview Section
    st.subheader("🔎 Overview of the Features")

    # Create columns for feature highlights
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image(logo_path, caption="PCOS Information", use_column_width=True)
        with st.expander("📚 PCOS Information"):
            st.markdown("Learn about PCOS, its symptoms, causes, and management strategies.")

    with col2:
        st.image(logo_path, caption="Simple Risk Assessment", use_column_width=True)
        with st.expander("⚠️ Simple Risk Assessment"):
            st.markdown("Quickly assess your risk based on key symptoms.")

    with col3:
        st.image(logo_path, caption="Enhanced Risk Assessment", use_column_width=True)
        with st.expander("🔍 Enhanced Risk Assessment"):
            st.markdown("Provide more detailed health data for an in-depth risk evaluation.")

    with col4:
        st.image(logo_path, caption="Results Visualization", use_column_width=True)
        with st.expander("📊 Results Visualization"):
            st.markdown("View your risk level with intuitive graphs and visualizations.")
