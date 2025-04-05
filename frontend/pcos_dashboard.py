import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance
import base64

# Update paths to be relative to the current file location
current_directory = os.path.dirname(__file__)
logo_path = os.path.join(current_directory, "images/logo.png")
pcos_image_path = os.path.join(current_directory, "images/pcos.jpg")
visuals_directory = os.path.join(current_directory, "../pcos_visuals")

def get_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# # Image details with filenames, captions, and explanations
# image_details = [
#     ("undiagnosed_pcos_distribution.png", "Undiagnosed PCOS Cases Distribution", 
#      "This chart shows the percentage of people who have PCOS but remain undiagnosed, highlighting the need for better awareness and screening."),
    
#     ("pcos_distribution_donut_chart.png", "PCOS Prevalence Donut Chart", 
#      "A donut chart representing the proportion of diagnosed versus undiagnosed PCOS cases among the surveyed population."),
    
#     ("pcos_symptoms_percentage.png", "Common PCOS Symptoms Breakdown", 
#      "This visualization presents the most frequently reported symptoms of PCOS, helping identify key health concerns."),
    
#     ("exercise_vs_pcos_symptoms.png", "Impact of Exercise on PCOS Symptoms", 
#      "A comparative analysis of how different levels of physical activity influence the severity of PCOS symptoms."),
    
#     ("fast_food_vs_pcos_symptoms.png", "Fast Food Consumption & PCOS Symptoms", 
#      "This graph explores the relationship between frequent fast-food consumption and the occurrence of PCOS symptoms.")
# ]

# Function to display the images and their explanations 
def display_image_and_explanation(image_filename, caption, explanation):
    image_path = os.path.join(visuals_directory, image_filename)
    if os.path.exists(image_path):
        # HTML to center the image
        st.markdown(f"""
            <div style="display: flex; justify-content: center;">
                <img src="data:image/png;base64,{get_base64(image_path)}" width="700" alt="{caption}">
            </div>
        """, unsafe_allow_html=True)
        
        # Caption and explanation
        st.markdown(f"<p style='text-align: center; font-weight: bold;'>{caption}</p>", unsafe_allow_html=True)
        
        # Explanation within an expander
        with st.expander(f"More details about {caption}"):
            st.markdown(f"""
                <div style='background-color: #D6C2EA; padding: 15px; border-radius: 10px; margin-bottom: 15px;'>
                    <p style='color: #333; font-size: 14px; line-height: 1.6;'>{explanation}</p>
                </div>
            """, unsafe_allow_html=True)


# Function to display images with larger size and enhanced quality
def display_image_and_explanation_large(image_filename, caption, explanation):
    image_path = os.path.join(visuals_directory, image_filename)
    
    # Open and enhance image for quality (sharpness adjustment)
    img = Image.open(image_path)
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(2.0)  # Increase sharpness by a factor of 2.0 (adjust as needed)
    
    # Display the enhanced image in Streamlit
    st.image(img, caption=caption, use_column_width=True)  # Using column width to scale appropriately
    
    with st.expander(f"More deatils about {caption}"):
        st.markdown(f"""
                <div style='background-color: #D6C2EA; padding: 15px; border-radius: 10px; margin-bottom: 15px;'>
                    <p style='color: #333; font-size: 14px; line-height: 1.6;'>{explanation}</p>
                </div>
            """, unsafe_allow_html=True)


# PCOS Dashboard Page with Storytelling Approach
def pcos_dashboard_page():
    # Logo and Title
    st.markdown(
        f"""
        <div style='text-align: center;'>
            <img src='data:image/png;base64,{get_base64(logo_path)}' width='100'/> 
            <h1>PCOS Care</h1>
        </div>
        """,unsafe_allow_html=True)
    
    # Introductory Overview of PCOS
    st.markdown("""
        <div style='background-color: #E5D9F2; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
            <h1 style='color: #947bd6; text-align: center;'>Welcome to the Insights Dashboard</h1>
            <p>In this section, you will be taken through the impact of Polycystic Ovary Syndrome (PCOS), how it affects millions of people, and the ways you can manage it effectively. You will have a deeper understanding of how you can shape your life, along with practical insights on symptoms and the role of exercise.</p>
        </div>
    """, unsafe_allow_html=True)

    # 1: The Growing Challenge - PCOS Prevalence
    st.markdown("""
        <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; margin-bottom: 20px; border: 2px solid #CDC1FF;'>
            <h2 style='color: #9C89FB;'>Insight 1: The Growing Challenge - PCOS Prevalence</h2>
            <p>PCOS affects millions of people around the world, but many don’t even know they have it. This is because PCOS is often not diagnosed, and many people overlook the symptoms. Understanding how common PCOS is is the first step toward managing it better. This section highlights an alarming number of people with undiagnosed PCOS, which is a major issue.</p>
        </div>
    """, unsafe_allow_html=True)

    # Display the first graph: Undiagnosed PCOS Cases Distribution
    display_image_and_explanation(
        "undiagnosed_pcos_distribution.png", 
        "Undiagnosed PCOS Cases Distribution", 
        "This chart shows the percentage of people who have PCOS but remain undiagnosed as 70%, highlighting the need for better awareness and screening. This insight was gathered from the research <a href='https://doi.org/10.1109/ICABME53305.2021.9604905' target='_blank'>Automated Detection of Polycystic Ovary Syndrome Using Machine Learning Techniques</a>."

    )


    # 2: The Impact of PCOS - Prevalence Breakdown
    st.markdown("""
        <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; margin-bottom: 20px; border: 2px solid #CDC1FF;'>
            <h2 style='color: #9C89FB;'>Insight 2: The Impact of PCOS - Prevalence Breakdown</h2>
            <p>PCOS is a common condition that affects many individuals worldwide, but many people are still undiagnosed. Its symptoms can often be easy to overlook, making it challenging for people to seek the help they need. In this section, we highlight how widespread PCOS is in the population and why it's so important to raise awareness. Understanding how common it is helps spread the word about PCOS and encourages early diagnosis and treatment, leading to better care and management.</p>
        </div>
    """, unsafe_allow_html=True)

    # Display the second graph: PCOS Prevalence Donut Chart
    display_image_and_explanation(
        "pcos_distribution_donut_chart.png", 
        "PCOS Prevalence Donut Chart", 
        "This donut chart shows the percentage of people in the survey who have PCOS compared to those who don't. About 33% of the people in the survey were found to have PCOS. This highlights how important it is to be aware of the condition and get checked early."
    )
    

    # 3: The Faces of PCOS - Symptoms Breakdown (contd.)
    st.markdown("""
        <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; margin-bottom: 20px; border: 2px solid #CDC1FF;'>
            <h2 style='color: #9C89FB;'>Insight 3: The Faces of PCOS - Common Symptoms Breakdown</h2>
            <p>PCOS can cause a variety of symptoms that affect a person’s daily life. Some of the most common symptoms include pimples, weight gain, skin darkening, hair loss, and extra hair growth. It’s important to recognize these signs, as they can help people seek the right treatment. Lifestyle changes can help manage these symptoms and improve overall well-being.</p>
        </div>
    """, unsafe_allow_html=True)

    # Display the third graph: Common PCOS Symptoms Breakdown
    display_image_and_explanation(
        "pcos_symptoms_percentage.png", 
        "Common PCOS Symptoms Breakdown", 
        "This chart shows the most commonly reported symptoms in people diagnosed with PCOS. Each bar represents the percentage of individuals with PCOS who experience that symptom. The symptoms are arranged from top to bottom based on how strongly they are linked to PCOS - so those at the top are the most impactful and worth paying closer attention to."
    )

    # 4: Managing PCOS - The Role of Exercise
    st.markdown("""
        <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; margin-bottom: 20px; border: 2px solid #CDC1FF;'>
            <h2 style='color: #9C89FB;'>Insight 4: Managing PCOS - The Role of Exercise</h2>
            <p>Physical activity is one of the most powerful tools in managing PCOS. In this we see how different levels of exercise can positively impact the severity of symptoms.</p>
        </div>
    """, unsafe_allow_html=True)

    # Display the fourth graph: Impact of Exercise on PCOS Symptoms
    display_image_and_explanation_large(
        "exercise_vs_pcos_symptoms.png", 
        "Impact of Exercise on PCOS Symptoms", 
        "A comparative analysis of how different levels of physical activity influence the severity of PCOS and its symptoms."
    )

    # Chapter 5: The Impact of Diet - Fast Food and PCOS Symptoms
    st.markdown("""
        <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; margin-bottom: 20px; border: 2px solid #CDC1FF;'>
            <h2 style='color: #9C89FB;'>Insight 5: The Impact of Diet - Fast Food and PCOS Symptoms</h2>
            <p>Diet plays a key role in managing PCOS. In this we can see how a diet rich in fast food may contribute to the worsening of PCOS symptoms.</p>
        </div>
    """, unsafe_allow_html=True)

    # Display the fifth graph: Fast Food Consumption & PCOS Symptoms
    display_image_and_explanation_large(
        "fast_food_vs_pcos_symptoms.png", 
        "Fast Food Consumption & PCOS Symptoms", 
        "This graph explores the relationship between frequent fast-food consumption and the occurrence of PCOS and its symptoms."
    )

    # Disclaimer Section
    st.markdown("""
        <div style='background-color: #EAE0F5; padding: 20px; border-radius: 10px; border: 2px solid #CDC1FF;'>
            <h3 style='text-align: center; color: #b179d9;'>Disclaimer</h3>
            <p style='text-align: center; font-weight: bold;'>This tool is for informational purposes only and does not provide a medical diagnosis.</p>
            <ul style='list-style-type: disc; padding-left: 20px;'>
                <li>Predictions are generated based on data from a specific patient dataset. <a href="https://www.kaggle.com/datasets/prasoonkottarathil/polycystic-ovary-syndrome-pcos" target="_blank">Access the dataset here</a></li>
                <li>The assessment is not a substitute for a professional medical evaluation or diagnosis. Always consult a doctor or qualified healthcare provider for diagnosis and treatment.</li>
                <li>The predictions provided are based on the available dataset and may have limitations in accuracy and scope. Results should be interpreted with caution and may not reflect individual circumstances.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)