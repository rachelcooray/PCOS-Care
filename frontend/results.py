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
        st.title("PCOS Risk Assessment Results")

    st.subheader("Your Risk Level")

    # Ensure risk assessment data is available
    if "risk_assessment_data" in st.session_state:
        user_data = st.session_state.risk_assessment_data
        
        # Placeholder for ML-based risk prediction
        predicted_risk = user_data.get("predicted_risk", "Unknown")  # Assume the model prediction is stored
        
        # Display Risk Level
        st.markdown(f"""
            ## Your estimated PCOS risk is **{predicted_risk}**  
            { "⚠️ *We strongly recommend seeking medical advice.*" if predicted_risk == "High" else 
               "🔍 *Consider tracking your symptoms over time.*" if predicted_risk == "Moderate" else
               "✅ *Maintain a healthy lifestyle and monitor symptoms.*"
            }
        """, unsafe_allow_html=True)

        # Section Break
        st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

        # Detailed Breakdown of Factors
        st.subheader("Detailed Breakdown of Factors Contributing to Your Risk")
        st.dataframe(pd.DataFrame(user_data.get("symptom_analysis", [])))

        # Risk Contribution Breakdown (Example Visualization)
        st.subheader("How Your Symptoms Compare to PCOS Risk Levels")
        
        # Example data (Replace with real user data)
        

        # Plot
        

        # Section Break
        st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

        # Next Steps Based on Risk Level
        st.subheader("Next Steps Based on Your Risk Level")
        if predicted_risk == "High":
            st.warning("⚠️ We strongly recommend seeking medical advice as soon as possible.")
        elif predicted_risk == "Moderate":
            st.info("🔍 Consider tracking your symptoms over time and consulting a doctor if symptoms persist.")
        else:
            st.success("✅ Maintain a healthy lifestyle and monitor symptoms.")

        # Call to Action
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📖 Get Lifestyle Recommendations"):
                st.switch_page("PCOS Information")  # Adjust based on routing

    else:
        st.error("No risk assessment data found. Please complete the assessment first.")
