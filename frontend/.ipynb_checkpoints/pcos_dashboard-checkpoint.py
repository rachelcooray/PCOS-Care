import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import base64

# Update paths to be relative to the current file location
current_directory = os.path.dirname(__file__)
logo_path = os.path.join(current_directory, "images/logo.png")
pcos_image_path = os.path.join(current_directory, "images/pcos.jpg")
visuals_directory = os.path.join(current_directory, "../pcos_visuals")

def get_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def pcos_dashboard_page():
    # Layout for logo and title
    st.markdown(
        f"""
        <div style='text-align: center;'>
            <img src='data:image/png;base64,{get_base64(logo_path)}' width='100'/>
            <h1>PCOS Care</h1>
        </div>
        """,
        unsafe_allow_html=True
    )        
    
    # **Header Section with Logo**
    st.markdown("<div class='dashboard-container'><h1 class='dashboard-title'>PCOS Dashboard</h1></div>", unsafe_allow_html=True)
        
    st.markdown("""
        <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
            <h2 style='color: #6a0dad;'>Visualizing Key Trends: Insights from Analysis of PCOS Data</h2>
        </div>
    """, unsafe_allow_html=True)

    # List of images with captions and descriptions in a box
    image_details = [
        ("undiagnosed_pcos_distribution.png", "Undiagnosed PCOS Cases Distribution", 
         "This chart shows the percentage of people who have PCOS but remain undiagnosed, highlighting the need for better awareness and screening."),
        
        ("pcos_distribution_donut_chart.png", "PCOS Prevalence Donut Chart", 
         "A donut chart representing the proportion of diagnosed versus undiagnosed PCOS cases among the surveyed population."),
        
        ("pcos_symptoms_percentage.png", "Common PCOS Symptoms Breakdown", 
         "This visualization presents the most frequently reported symptoms of PCOS, helping identify key health concerns."),
        
        ("exercise_vs_pcos_symptoms.png", "Impact of Exercise on PCOS Symptoms", 
         "A comparative analysis of how different levels of physical activity influence the severity of PCOS symptoms."),
        
        ("fast_food_vs_pcos_symptoms.png", "Fast Food Consumption & PCOS Symptoms", 
         "This graph explores the relationship between frequent fast-food consumption and the occurrence of PCOS symptoms.")
    ]
    
    # Display images with captions and descriptions inside a box
    for image_file, caption, description in image_details:
        image_path = os.path.join(visuals_directory, image_file)
        if os.path.exists(image_path):
            st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
            # Add proper centering for images by using st.columns
            col1, col2, col3 = st.columns([1, 4, 1])  # Center the image in the second column
            with col2:
                st.image(image_path, width=700, caption=caption)
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Adding a box around the description
            st.markdown(f"""
                <div style='background-color: #f1f1f1; border: 1px solid #ccc; border-radius: 5px; padding: 10px; margin-top: 5px;'>
                    <p style='text-align: center; font-size: 14px; color: #555;'>{description}</p>
                </div>
            """, unsafe_allow_html=True)  # Description in a box
            
            st.markdown("<br>", unsafe_allow_html=True)  # Adds space between images
            st.markdown("<br>", unsafe_allow_html=True) 
        else:
            st.error(f"{image_file} not found.")
    
    # Expander for deeper insights
    with st.expander("Find out the Insights gathered from the Data", expanded=False):
        st.markdown("""
            - **PCOS Prevalence Distribution** – Shows the percentage of diagnosed vs undiagnosed cases.
            - **Symptom Breakdown** – Visualizes the most commonly reported PCOS symptoms.
            - **Undiagnosed PCOS Cases** – Highlights how many individuals have PCOS but remain undiagnosed (*Alda et al., 2024*).
            - **Exercise vs PCOS Symptoms** – Demonstrates the effects of physical activity on symptom severity.
            - **Fast Food Consumption & PCOS** – Analyzes the link between fast food intake and PCOS symptoms.
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)  # Adds spacing
    
    # Disclaimer Section
    st.markdown("""
        <div style='background-color: #EAE0F5; padding: 20px; border-radius: 10px; border: 2px solid #CDC1FF;'>
            <h3 style='text-align: center; color: #b179d9;'>Disclaimer</h3>
            <p style='text-align: center; font-weight: bold;'>This tool is for informational purposes only and does not provide a medical diagnosis.</p>
            <ul style='list-style-type: disc; padding-left: 20px;'>
                <li>Predictions are based on available data from a dataset of <strong>patients in Kerala, India</strong>.</li>
                <li>The assessment is <strong>not a substitute for a professional medical evaluation or diagnosis</strong>. Always consult a doctor for diagnosis and treatment.</li>
                <li>The accuracy of predictions is <strong>limited by the dataset's scope and quality</strong>, and results may not apply to everyone.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
