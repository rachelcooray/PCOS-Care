import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt

logo_path = "images/logo.png"

def results_page():
    col1, col2 = st.columns([1, 4]) 

    with col1:
        if os.path.exists(logo_path):
            st.image(logo_path, width=100)  
        else:
            st.error("Logo image not found.")

    with col2:
        st.title("PCOS Care")

    st.subheader("Your PCOS Prediction")

    # Ensure risk assessment data is available
    if "risk_assessment_data" in st.session_state:
        user_data = st.session_state.risk_assessment_data
        
        # ML-based prediction: Yes (PCOS) or No (No PCOS)
        predicted_pcos = user_data.get("predicted_pcos", "Unknown")  
        
        # Display Prediction
        st.markdown(f"""
            ## **Prediction: {predicted_pcos}**  
            { "⚠️ *This suggests a possibility of PCOS. Please consult a healthcare professional for further evaluation.*" if predicted_pcos == "Yes" else 
               "✅ *No PCOS detected based on this assessment. However, if symptoms persist, consider consulting a doctor.*"
            }
        """, unsafe_allow_html=True)

        # Section Break
        st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

        # Detailed Breakdown of Factors
        st.subheader("Detailed Breakdown of Your Symptoms")
        st.dataframe(pd.DataFrame(user_data.get("symptom_analysis", [])))

        # Section Break
        st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

        # Next Steps Based on Prediction
        st.subheader("Next Steps")
        if predicted_pcos == "Yes":
            st.warning("⚠️ We strongly recommend seeking medical advice for further evaluation.")
        else:
            st.success("✅ Maintain a healthy lifestyle and monitor symptoms over time.")

        # Disclaimer Section
        st.markdown("### Disclaimer")
        st.info("""
        - This prediction is based on a dataset of **541 patients from Kerala, India**.
        - **This is not a medical diagnosis.** It is a preliminary assessment and should not be used as a substitute for clinical evaluation.
        - The accuracy of predictions is **limited by the dataset's scope and quality**, and results may not generalize to all populations.
        """)

        # Call to Action
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📖 Get Lifestyle Recommendations"):
                st.switch_page("PCOS Information")  

    else:
        st.error("No assessment data found. Please complete the assessment first.")
