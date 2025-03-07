import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt

# Update paths to be relative to the current file location
current_directory = os.path.dirname(__file__)
logo_path = os.path.join(current_directory, "images/logo.png")
pcos_image_path = os.path.join(current_directory, "images/pcos.jpg")
visuals_directory = os.path.join(current_directory, "../pcos_visuals")


def pcos_info_page():
    # Layout for logo and title
    st.markdown("<div style='text-align: center; margin-bottom: 20px;'>", unsafe_allow_html=True)
    if os.path.exists(logo_path):
        st.image(logo_path, width=120)
    else:
        st.error("Logo image not found.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color: #6a0dad;'>PCOS Care</h1>", unsafe_allow_html=True)

    # Section: What is PCOS?
    st.markdown("""
        <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
            <h2 style='color: #6a0dad;'>What is PCOS?</h2>
            <p>Polycystic Ovary Syndrome (PCOS) is a <strong>hormonal disorder</strong> that affects women of reproductive age. It can lead to <strong>irregular periods, excessive hair growth, acne, weight gain, and fertility issues</strong>. PCOS is also linked to insulin resistance and hormonal imbalances.</p>
        </div>
    """, unsafe_allow_html=True)

    # PCOS Symptoms
    st.markdown("""
        <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
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
        <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
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
        <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
            <h2 style='color: #6a0dad;'>How PCOS Affects Health?</h2>
            <div style='display: flex;'>
                <div style='flex: 1; padding-right: 10px;'>
                    <p>PCOS affects multiple systems in the body, leading to:</p>
                    <ul>
                        <li><strong>Hormonal imbalances</strong></li>
                        <li><strong>Metabolic issues (insulin resistance, weight gain)</strong></li>
                        <li><strong>Increased risk of cardiovascular disease</strong></li>
                        <li><strong>Complications in pregnancy and fertility</strong></li>
                    </ul>
                </div>
                <div style='flex: 1;'>
                    """, unsafe_allow_html=True)


    # Section Break
    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    st.subheader("Dashboard of insights gathered for visualisation")
        
    # Embed the images created with matplotlib using Streamlit's st.image function
    image_files = [
        "exercise_vs_pcos_symptoms.png",
        "fast_food_vs_pcos_symptoms.png",
        "pcos_distribution_donut_chart.png",
        "pcos_symptoms_percentage.png",
        "undiagnosed_pcos_distribution.png"
    ]
    
    for image_file in image_files:
        image_path = os.path.join(visuals_directory, image_file)
        if os.path.exists(image_path):
            st.image(image_path, use_column_width=True, caption=image_file.replace('_', ' ').title())
        else:
            st.error(f"Image {image_file} not found.")
    
    st.markdown("""
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Call to Action
    st.markdown("""
        <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; text-align: center;'>
            <h2 style='color: #6a0dad;'>Take the Next Step</h2>
            <p>Ready to take control of your health? Start by taking the Simple Assessment.</p>
    """, unsafe_allow_html=True)

    # Add space between markdown and button
    st.markdown("<br><br>", unsafe_allow_html=True)  # Adds vertical space

    col1, col2, col3 = st.columns([1, 1, 1])

    # Place the buttons in the center column
    with col2:
        if st.button("Try the Simple Risk Assessment"):
            st.session_state.page = "Simple Risk Assessment"

    st.markdown("</div>", unsafe_allow_html=True)

# Run the PCOS info page function when the script is executed
if __name__ == "__main__":
    pcos_info_page()