import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt

# Update paths to be relative to the current file location
current_directory = os.path.dirname(__file__)
logo_path = os.path.join(current_directory, "images/logo.png")
visuals_directory = os.path.join(current_directory, "../pcos_visuals")

def results_page():
    # Layout for logo and title
    col1, col2 = st.columns([1, 4]) 

    with col1:
        if os.path.exists(logo_path):
            st.image(logo_path, width=100)  
        else:
            st.error("Logo image not found.")

    with col2:
        st.title("PCOS Care")

    st.subheader("Dashboard for visualisation")
        
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

    st.subheader("Your PCOS Prediction")

    # Ensure risk assessment data is available
    if "risk_assessment_data" in st.session_state:
        user_data = st.session_state.risk_assessment_data
        
        # ML-based prediction: Yes or No 
        predicted_pcos = user_data.get("predicted_pcos", "Unknown")  # result from assessment
        
        # Display Prediction
        st.markdown(f"""
            <h3 style='text-align: center; color: #6a0dad;'>Prediction: {predicted_pcos}</h3>  
            { "⚠️ This suggests a possibility of PCOS. Please consult a healthcare professional for further evaluation." if predicted_pcos == "You are likely to have PCOS"  else 
               "✅ No PCOS detected based on this assessment. However, if symptoms persist, consider consulting a doctor."
            }
        """, unsafe_allow_html=True)

        # Section Break
        st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

        # Next Steps Based on Prediction
        st.subheader("Next Steps")
        if predicted_pcos == "You are likely to have PCOS":
            st.warning("""
                ⚠️  We strongly recommend seeking medical advice for further evaluation.
                
                ⚠️  You can download your data as a PDF to share with your healthcare provider.
            """)
        else:
            st.success("✅  Maintain a healthy lifestyle and monitor symptoms over time.")

        # Disclaimer Section
        st.markdown("### Disclaimer")
        st.info("""
        - This prediction is based on a dataset of **541 patients from Kerala, India**.
        - **This is not a medical diagnosis.** It is a preliminary assessment and should not be used as a substitute for clinical evaluation.
        - The accuracy of predictions is **limited by the dataset's scope and quality**, and results may not generalize to all populations.
        """)

        st.markdown("""
        <p><em>Data from a sample of 541 PCOS patients in Kerala.</em></p>
        <p><a href='https://www.kaggle.com/datasets/prasoonkottarathil/polycystic-ovary-syndrome-pcos' target='_blank'>Source Link</a></p>
        </div>
    """, unsafe_allow_html=True)

        # Section Break
        st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)


    else:
        st.error("No assessment data found. Please complete the assessment first.")
        
        # Detailed Breakdown 
        st.subheader("Detailed Breakdown of Your Symptoms")
        # st.dataframe(pd.DataFrame(user_data.get("symptom_analysis", [])))

        # Section Break
        st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

        # Call to Action
        st.markdown("<h3 style='text-align: center; margin-top: 40px;'>Explore More</h3>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 1, 1])

        # Place the buttons in the center column
        with col1:
            if st.button("📚 Learn More About PCOS"):
                st.session_state.page = "PCOS Information"
        
        with col2:    
            if st.button("⚠️ Take the Simple Risk Assessment"):
                st.session_state.page = "Simple Risk Assessment"

        with col3:    
            if st.button("⚠️ Take the Enhanced Risk Assessment"):
                st.session_state.page = "Enhanced Risk Assessment"        
