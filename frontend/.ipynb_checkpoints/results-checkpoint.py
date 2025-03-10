import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go  # For gauge charts
import altair as alt  # For bar charts
import numpy as np

# Update paths to be relative to the current file location
current_directory = os.path.dirname(__file__)
logo_path = os.path.join(current_directory, "images/logo.png")

def create_gauge(value, title, min_val, max_val, color="blue"):
    """ Creates a simple gauge chart using Plotly. """
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title},
        gauge={'axis': {'range': [min_val, max_val]},
               'bar': {'color': color}}))
    return fig

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

        st.subheader("Insights gathered from your data")

        # **1. Ratio-Based Visuals (BMI, Waist-Hip Ratio, FSH/LH)**
        st.subheader("Key Health Ratios")

        bmi = user_data["symptom_analysis"].get("BMI")
        waist_hip_ratio = user_data["symptom_analysis"].get("Waist:Hip Ratio")
        fsh_lh_ratio = user_data["symptom_analysis"].get("FSH/LH")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.plotly_chart(create_gauge(bmi, "BMI", 10, 50, "green" if bmi < 25 else "red"))
            st.markdown("TO DO - Describe BMI")
        with col2:
            st.plotly_chart(create_gauge(waist_hip_ratio, "Waist:Hip Ratio", 0.4, 1.0, "green" if waist_hip_ratio < 0.85 else "red"))
            st.markdown("TO DO - Describe ratio")
        with col3:
            st.plotly_chart(create_gauge(fsh_lh_ratio, "FSH/LH", 0, 3, "red" if fsh_lh_ratio <= 1 else "green"))
            st.markdown("TO DO - Describe ratio")


        # **2. Cycle Irregularities (If Selected)**
        cycle = user_data["symptom_analysis"].get("Cycle(R/I)")
        if cycle == 4:  # Assuming 4 means Irregular
            st.subheader("Cycle Irregularities")
            
            st.warning("🚨 Irregular cycles are commonly associated with PCOS due to hormonal imbalances.")
            
            # Retrieve FSH and LH values
            fsh = float(user_data["symptom_analysis"].get("FSH(mIU/mL)", 0))
            lh = float(user_data["symptom_analysis"].get("LH(mIU/mL)", 0))
        
            # Create a DataFrame for Altair
            df = pd.DataFrame({
                "Hormone": ["FSH (mIU/mL)", "LH (mIU/mL)"],
                "Value": [fsh, lh]
            })
        
            # Create a slimmer bar chart with Altair
            chart = alt.Chart(df).mark_bar(width=40).encode(
                x=alt.X("Hormone", sort=None),  # Keeps order as given
                y="Value",
                color=alt.Color("Hormone", legend=None)
            ).properties(height=300)
        
            st.altair_chart(chart, use_container_width=True)
        
            # Display additional information based on LH/FSH ratio
            if lh > fsh:
                st.info("💡 Your LH is higher than FSH, which could indicate a hormonal imbalance often associated with PCOS. High LH relative to FSH can lead to anovulation (lack of ovulation). Consider discussing these findings with your healthcare provider.")
            elif lh == fsh:
                st.info("🔍 Your LH and FSH levels are similar. It's important to evaluate other hormonal and clinical factors to get a clearer picture of your health.")
            else:
                st.info("✅ Your FSH is higher than LH, which is generally considered more typical. However, it’s still important to monitor your cycle and overall health.")

        # **3. Lifestyle Factors (Weight Gain, Fast Food, No Exercise)**
        weight_gain = user_data["symptom_analysis"].get("Weight gain(Y/N)", 0)
        fast_food = user_data["symptom_analysis"].get("Fast food (Y/N)", 0)
        reg_exercise = user_data["symptom_analysis"].get("Reg.Exercise(Y/N)", 1)

        if weight_gain == 1 or fast_food == 1 or reg_exercise == 0:
            st.subheader("Lifestyle Factors")
            
            st.warning("⚠️ Lifestyle factors can significantly impact PCOS risk.")
            st.info("""
            - **Weight Gain:** Excess weight can worsen insulin resistance, a key PCOS factor.
            - **Fast Food Consumption:** Processed foods may contribute to hormone imbalances.
            - **Lack of Exercise:** Regular physical activity can help regulate hormones.
            """)

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

    st.markdown("TO ADD - disclaimer, references")
