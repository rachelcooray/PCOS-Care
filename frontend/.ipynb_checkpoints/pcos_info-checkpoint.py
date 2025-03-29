import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Update paths to be relative to the current file location
current_directory = os.path.dirname(__file__)
logo_path = os.path.join(current_directory, "images/logo.png")
pcos_image_path = os.path.join(current_directory, "images/pcos.jpg")
visuals_directory = os.path.join(current_directory, "../pcos_visuals")

def pcos_info_page():
    # Layout for logo and title
    st.markdown("<div style='text-align: center; margin-bottom: 20px;'>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 4])  

    with col1:
        if os.path.exists(logo_path):
            st.image(logo_path, width=100)  
        else:
            st.error("Logo image not found.")

    with col2:
        st.title("PCOS Care")

    # Section: What is PCOS?
    st.markdown("""
        <div style='background-color: #EAE0F5; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
            <h2 style='color: #6a0dad;'>What is PCOS?</h2>
            <p>Polycystic Ovary Syndrome (PCOS) is a <strong>hormonal disorder</strong> that affects women of reproductive age. It can lead to <strong>irregular periods, excessive hair growth, acne, weight gain, and fertility issues</strong>. PCOS is also linked to insulin resistance and hormonal imbalances.</p>
        </div>
    """, unsafe_allow_html=True)

    # PCOS Symptoms
    st.markdown("""
        <div style='background-color: #EAE0F5; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
            <h2 style='color: #6a0dad;'>Common Symptoms</h2>
            <ul>
                <li><strong>Irregular menstrual cycles</strong></li>
                <li><strong>Unexplained weight gain</strong></li>
                <li><strong>Acne and oily skin</strong></li>
                <li><strong>Thinning hair or hair loss</strong></li>
                <li><strong>Mood swings and fatigue</strong></li>
                <li><strong>Dark patches of skin</strong> (especially around the neck or underarms)</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # Image Section with Centering in 3 Columns
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Create 3 columns, with equal width
    col1, col2, col3 = st.columns([1, 2, 1])  # The middle column (col2) will be wider
    
    # Place the hero image in the center column (col2)
    with col2:
        if os.path.exists(pcos_image_path):
            st.image(pcos_image_path, use_column_width=True, caption="PCOS Effects on Health")
        else:
            st.error("PCOS image not found.")
    
    st.markdown("""
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Section: Why Early Detection Matters
    st.markdown("""
        <div style='background-color: #EAE0F5; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
            <h2 style='color: #6a0dad;'>Why Early Detection Matters?</h2>
            <p>Early detection and lifestyle changes can <strong>help manage symptoms and prevent long-term complications</strong>.</p>
            <p><strong>Without treatment, PCOS can increase the risk of:</strong></p>
            <ul>
                <li><strong>Type 2 Diabetes</strong></li>
                <li><strong>Heart Disease & High Blood Pressure</strong></li>
                <li><strong>Infertility or Pregnancy Complications</strong></li>
                <li><strong>Depression & Anxiety</strong></li>
            </ul>
            <p><em>Taking action early helps improve overall health and quality of life.</em></p>
        </div>
    """, unsafe_allow_html=True)

    # Section: How PCOS Affects Health
    st.markdown("""
        <div style='background-color: #EAE0F5; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
            <h2 style='color: #6a0dad;'>How PCOS Affects Health?</h2>
               <p>PCOS affects multiple systems in the body, leading to:</p>
                    <ul>
                        <li><strong>Hormonal imbalances</strong></li>
                        <li><strong>Metabolic issues (insulin resistance, weight gain)</strong></li>
                        <li><strong>Increased risk of cardiovascular disease</strong></li>
                        <li><strong>Complications in pregnancy and fertility</strong></li>
                    </ul> 
                    """, unsafe_allow_html=True)

    # Section: PCOS Management Tips
    st.markdown("""
        <div style='background-color: #EAE0F5; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
            <h2 style='color: #6a0dad;'>PCOS Management Tips</h2>
            <ul>
                <li><strong>Regular Exercise:</strong> Aim for at least 150 minutes of moderate activity per week.</li>
                <li><strong>Manage Stress:</strong> Practice yoga, meditation, or deep breathing exercises.</li>
                <li><strong>Healthy Sleep:</strong> Maintain a consistent sleep schedule with 7-9 hours of rest.</li>
                <li><strong>Consult a Doctor:</strong> Regular check-ups and medications if prescribed.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # Section: PCOS Diet Tips
    st.markdown("""
        <div style='background-color: #EAE0F5; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
            <h2 style='color: #6a0dad;'>Dietary Recommendations for PCOS</h2>
            <ul>
                <li><strong>Foods to Include:</strong> Whole grains, lean protein, healthy fats, and fiber-rich foods.</li>
                <li><strong>Foods to Avoid:</strong> Refined carbs, processed foods, and excessive sugar intake.</li>
                <li><strong>Hydration:</strong> Drink plenty of water to support metabolism and digestion.</li>
                <li><strong>Meal Timing:</strong> Balanced meals with controlled portions to maintain blood sugar levels.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # **Header Section with Logo**
    st.markdown("<div class='dashboard-container'><h1 class='dashboard-title'>PCOS Dashboard</h1></div>", unsafe_allow_html=True)
    
    # Section Break
    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
            <h2 style='color: #6a0dad;'>Visualizing Key Trends: Insights from PCOS Data Analysis</h2>
            <p style='text-align: center;'>Explore key visualizations that provide insights into PCOS trends and factors.</p>
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
            st.error(f"⚠️ {image_file} not found.")
    
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

    st.markdown("</div>", unsafe_allow_html=True)

    # Section: References & Resources 
    st.markdown("""
        <style>
            .resource-list {
                list-style-type: disc; 
                padding-left: 0;
            }
            .resource-link {
                color: #6a0dad; 
                text-decoration: none; 
                font-weight: bold;
                transition: color 0.3s ease-in-out;
            }
            .resource-link:hover {
                color: #a166c5; /* Lighter shade on hover */
            }
        </style>

        <div style='background-color: #EAE0F5; padding: 20px; border-radius: 10px;'>
            <h3 style='color: #6a0dad; text-align: center;'>References & Resources</h3>
            <ul class='resource-list'>
                <li><a href='https://www.who.int/news-room/fact-sheets/detail/polycystic-ovary-syndrome' target='_blank' class='resource-link'>World Health Organization - PCOS Guidelines</a></li>
                <li><a href='https://www.nhs.uk/conditions/polycystic-ovary-syndrome-pcos/' target='_blank' class='resource-link'>NHS - PCOS Overview</a></li>
                <li><a href='https://www.bda.uk.com/resource/polycystic-ovary-syndrome-pcos-diet.html' target='_blank' class='resource-link'>British Dietetic Association - Polycystic Ovary Syndrome (PCOS) and Diet</a></li>
            </ul>
        </div>
    """, unsafe_allow_html=True)


    st.markdown("<br>", unsafe_allow_html=True)  # Adds spacing
    
    # Disclaimer Section
    st.markdown("""
        <div style='background-color: #EAE0F5; padding: 20px; border-radius: 10px; border: 2px solid #CDC1FF;'>
           <h3 style='text-align: center; color: #b179d9;'>Disclaimer</h3>
            <ul style='list-style-type: disc; padding-left: 20px;'>
                <li>The prediction given on this platform is based on a dataset of <strong>541 patients from Kerala, India</strong>.</li>
                <li><strong>This is not a medical diagnosis.</strong> It is similar to a preliminary assessment and should not be used as a substitute for clinical evaluation.</li>
                <li>The accuracy of predictions is <strong>limited by the dataset's scope and quality</strong>, and results may not generalize to all populations.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# Run the PCOS info page function when the script is executed
if __name__ == "__main__":
    pcos_info_page()