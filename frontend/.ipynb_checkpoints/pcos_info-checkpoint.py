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

def get_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


def pcos_info_page():
    # Layout for logo and title
    # Logo and Title
    st.markdown(
        f"""
        <div style='text-align: center;'>
            <img src='data:image/png;base64,{get_base64(logo_path)}' width='100'/> 
            <h1>PCOS Care</h1>
        </div>
        """,
        unsafe_allow_html=True
    )        

    # Section: What is PCOS?
    st.markdown("""
        <div style='background-color: #EAE0F5; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
            <h2 style='color: #6a0dad;'>What is PCOS?</h2>
            <p>Polycystic Ovary Syndrome (PCOS) is a <strong>hormonal disorder</strong> that affects women of reproductive age. It can lead to <strong>irregular periods, excessive hair growth, acne, weight gain, and fertility issues</strong>. PCOS is also linked to insulin resistance, increasing the risk of diabetes, heart disease, and other metabolic disorders.</p>
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
            <h2 style='color: #6a0dad;'>Why Early Detection Matters</h2>
            <p>Early detection and lifestyle changes can <strong>help manage symptoms and prevent long-term complications</strong>.</p>
            <p><strong>Without treatment, PCOS can increase the risk of:</strong></p>
            <ul>
                <li><strong>Type 2 Diabetes:</strong> Due to insulin resistance.</li>
                <li><strong>Cardiovascular Disease:</strong> Increased risk of high cholesterol and hypertension.</li>
                <li><strong>Infertility & Pregnancy Complications:</strong> Affecting ovulation and hormone balance.</li>
                <li><strong>Mental Health Challenges:</strong> Anxiety and depression are common among those with PCOS.</li>
            </ul>
            <p>Taking action early helps improve overall health and quality of life.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Section: How PCOS Affects Health
    st.markdown("""
        <div style='background-color: #EAE0F5; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
            <h2 style='color: #6a0dad;'>How PCOS Affects Health</h2>
            <p>PCOS affects multiple systems in the body, leading to:</p>
            <ul>
                <li><strong>Hormonal Imbalances:</strong> Excess androgen levels leading to acne and hair growth.</li>
                <li><strong>Metabolic Issues:</strong> Increased insulin resistance, causing weight gain and high blood sugar.</li>
                <li><strong>Fertility Challenges:</strong> Irregular ovulation affecting pregnancy.</li>
                <li><strong>Increased Risk of Chronic Diseases:</strong> Heart disease, diabetes, and depression.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # Section: PCOS Management Tips
    st.markdown("""
        <div style='background-color: #EAE0F5; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
            <h2 style='color: #6a0dad;'>PCOS Management Tips</h2>
            <p>Managing PCOS involves lifestyle modifications, medical treatments, and self-care. Here are some key tips:</p>
            <ul>
                <li><strong>Regular Exercise:</strong> Aim for at least 150 minutes of moderate activity per week.</li>
                <li><strong>Balanced Nutrition:</strong> Focus on whole grains, lean proteins, and healthy fats.</li>
                <li><strong>Stress Management:</strong> Practice yoga, meditation, or deep breathing.</li>
                <li><strong>Quality Sleep:</strong> Ensure 7-9 hours of sleep per night.</li>
                <li><strong>Medical Support:</strong> Consult a doctor for medications and hormone management if needed.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # Section: PCOS Diet Tips
    st.markdown("""
        <div style='background-color: #EAE0F5; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
            <h2 style='color: #6a0dad;'>Dietary Recommendations for PCOS</h2>
            <ul>
                <li><strong>Foods to Include:</strong></li>
                    <ul>
                        <li> Whole grains (quinoa, brown rice)</li>
                        <li> Healthy fats (avocado, olive oil)</li>
                        <li> Lean proteins (chicken, tofu, fish)</li>
                        <li> Fiber-rich vegetables (broccoli, spinach)</li>
                    </ul>  
                <br>
                <li><strong>Foods to Avoid:</strong></li>
                    <ul>
                        <li> Processed foods and sugary snacks</li>
                        <li> Excessive dairy and refined carbohydrates</li>
                        <li> Fried and fast foods</li>
                    </ul>
                <br>
                <li><strong>Hydration:</strong> Drink plenty of water to support metabolism and digestion.</li>
                <li><strong>Meal Timing:</strong> Balanced meals with controlled portions to maintain blood sugar levels.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # Section Break
    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

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
            <p style='text-align: center; font-weight: bold;'>This tool is for informational purposes only and does not provide a medical diagnosis.</p>
            <ul style='list-style-type: disc; padding-left: 20px;'>
                <li>Predictions are based on available data from a specific patient dataset. <a href="https://www.kaggle.com/datasets/prasoonkottarathil/polycystic-ovary-syndrome-pcos" target="_blank">Access the dataset here.</a>.</li>
                <li>The assessment is not a substitute for a professional medical evaluation or diagnosis. Always consult a doctor for diagnosis and treatment.</li>
                <li>The accuracy of predictions is limited by the dataset's scope and quality, and results may not apply to everyone.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
# Run the PCOS info page function when the script is executed
if __name__ == "__main__":
    pcos_info_page()